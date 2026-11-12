# Sensor manager for environmental readings and local monitoring.
# The hardware design uses SHT31 for temperature/humidity, SCD41 for CO2 and an
# analog ammonia sensor input for air quality.

import utime
from machine import ADC, Pin, I2C

from config import (
    I2C_SDA_PIN,
    I2C_SCL_PIN,
    FEED_LEVEL_PIN,
    WATER_FLOW_PIN,
)


class SHT31:
    def __init__(self, i2c):
        self.i2c = i2c
        self.address = 0x44

    def read(self):
        try:
            self.i2c.writeto(self.address, b"\x2C\x06")
            utime.sleep_ms(20)
            raw = self.i2c.readfrom(self.address, 6)
            if len(raw) != 6:
                return None
            temp_raw = (raw[0] << 8) | raw[1]
            hum_raw = (raw[3] << 8) | raw[4]
            temp_c = -45 + (175 * (temp_raw / 65535))
            rh_pct = 100 * (hum_raw / 65535)
            return {"temperature_c": temp_c, "humidity_pct": rh_pct}
        except Exception:
            return None


class SCD41:
    def __init__(self, i2c):
        self.i2c = i2c
        self.address = 0x62

    def start_periodic_measurement(self):
        try:
            self.i2c.writeto(self.address, b"\x21\xB1")
            return True
        except Exception:
            return False

    def read(self):
        try:
            self.i2c.writeto(self.address, b"\xEC\x05")
            utime.sleep_ms(10)
            raw = self.i2c.readfrom(self.address, 9)
            if len(raw) < 9:
                return None
            co2 = ((raw[0] << 8) | raw[1])
            return {"co2_ppm": co2}
        except Exception:
            return None


class SensorManager:
    def __init__(self):
        self.i2c = I2C(0, scl=Pin(I2C_SCL_PIN, Pin.OUT), sda=Pin(I2C_SDA_PIN, Pin.OUT), freq=100000)
        self.sht31 = SHT31(self.i2c)
        self.scd41 = SCD41(self.i2c)
        self.scd41.start_periodic_measurement()

        self.feed_adc = ADC(Pin(FEED_LEVEL_PIN, Pin.IN))
        self.water_flow_pin = Pin(WATER_FLOW_PIN, Pin.IN, Pin.PULL_UP)
        self.water_pulses = 0
        self.last_pulse_ms = 0
        self.total_liters = 0.0
        self.last_flow_lpm = 0.0

    def read_temperature_humidity(self):
        return self.sht31.read() or {"temperature_c": 0.0, "humidity_pct": 0.0}

    def read_co2(self):
        return self.scd41.read() or {"co2_ppm": 0}

    def read_ammonia_ppm(self):
        # Typical ammonia sensor strategy: analog output representing ppm via an
        # electrochemical module. Calibration is required on site.
        adc_value = self.feed_adc.read()
        # Conversion is intentionally conservative and high-level.
        # The final design must use the actual sensor transfer function.
        return max(0, adc_value / 40.96)

    def read_feed_level_pct(self):
        raw = self.feed_adc.read()
        # Approximate mapping for a simple analog feed sensor. Final values require
        # calibration to actual sensor geometry.
        raw_min = 800
        raw_max = 3800
        if raw <= raw_min:
            return 0.0
        if raw >= raw_max:
            return 100.0
        return (raw - raw_min) * 100 / (raw_max - raw_min)

    def handle_water_pulse(self, pin):
        self.water_pulses += 1
        now = utime.ticks_ms()
        self.total_liters += 0.01
        if self.last_pulse_ms:
            delta_ms = utime.ticks_diff(now, self.last_pulse_ms)
            if delta_ms > 0:
                self.last_flow_lpm = (60 * 0.01) / (delta_ms / 1000.0)
        self.last_pulse_ms = now

    def read_water_state(self):
        current_time_ms = utime.ticks_ms()
        if self.last_pulse_ms and utime.ticks_diff(current_time_ms, self.last_pulse_ms) > 15000:
            self.last_flow_lpm = 0.0
        return {
            "flow_lpm": self.last_flow_lpm,
            "total_liters": self.total_liters,
        }
