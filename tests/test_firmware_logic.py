import sys
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIRMWARE_DIR = ROOT / "firmware"
sys.path.insert(0, str(FIRMWARE_DIR))

machine = types.ModuleType("machine")


class FakePin:
    OUT = 1
    IN = 0
    PULL_UP = 2
    IRQ_RISING = 1

    def __init__(self, num, mode=None, pull=None):
        self.num = num
        self.mode = mode
        self.pull = pull
        self.state = 0

    def value(self, val=None):
        if val is None:
            return self.state
        self.state = val
        return val

    def irq(self, trigger, handler):
        self.trigger = trigger
        self.handler = handler
        return True


class FakeADC:
    def __init__(self, pin):
        self.pin = pin
        self._value = 0

    def read(self):
        return self._value


class FakeI2C:
    def __init__(self, bus_id, scl=None, sda=None, freq=100000):
        self.bus_id = bus_id
        self.scl = scl
        self.sda = sda
        self.freq = freq

    def writeto(self, address, data):
        return None

    def readfrom(self, address, count):
        return b"\x00" * count


machine.Pin = FakePin
machine.ADC = FakeADC
machine.I2C = FakeI2C

utime = types.ModuleType("utime")
utime.sleep_ms = lambda ms: None
utime.ticks_ms = lambda: 0
utime.ticks_diff = lambda now, last: now - last

sys.modules["machine"] = machine
sys.modules["utime"] = utime

import config  # noqa: E402
import sensor_manager  # noqa: E402
import ventilation  # noqa: E402


class DummyLogger:
    def warn(self, msg):
        self.last_msg = msg


class FirmwareLogicTests(unittest.TestCase):
    def test_ventilation_emergency_mode_on_high_ammonia(self):
        logger = DummyLogger()
        controller = ventilation.VentilationController(logger)

        result = controller.update(24.0, 58.0, 1200, 18.0, True)

        self.assertEqual(result["mode"], "high")
        self.assertEqual(result["target_pct"], 70)

        result = controller.update(24.0, 58.0, 1200, 26.0, True)
        self.assertEqual(result["mode"], "emergency")
        self.assertEqual(result["target_pct"], 100)

    def test_ventilation_local_safe_mode_without_mqtt(self):
        logger = DummyLogger()
        controller = ventilation.VentilationController(logger)

        result = controller.update(24.0, 50.0, 1000, 5.0, False)

        self.assertEqual(result["mode"], "local_safe")
        self.assertEqual(result["target_pct"], 15)

    def test_sensor_feed_and_ammonia_calibration(self):
        sensor = sensor_manager.SensorManager.__new__(sensor_manager.SensorManager)
        sensor.feed_adc = types.SimpleNamespace(read=lambda: 1760)
        sensor.nh3_adc = types.SimpleNamespace(read=lambda: 1024)
        sensor.ammonia_offset = 0.0
        sensor.temp_offset = 0.0
        sensor.humidity_offset = 0.0
        sensor.co2_offset = 0

        self.assertAlmostEqual(sensor.read_feed_level_pct(), 32.0, places=2)
        self.assertAlmostEqual(sensor.read_ammonia_ppm(), 25.0, places=2)

    def test_manual_override_forces_full_ventilation(self):
        logger = DummyLogger()
        controller = ventilation.VentilationController(logger)
        controller.set_manual_override(True)

        result = controller.update(20.0, 40.0, 700, 2.0, True)

        self.assertEqual(result["mode"], "manual")
        self.assertEqual(result["target_pct"], 100)


if __name__ == "__main__":
    unittest.main()
