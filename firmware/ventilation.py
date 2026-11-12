# Mechanical ventilation controller with local fail-safe logic.

import utime
from machine import Pin, PWM

from config import ENVIRONMENT_THRESHOLDS


class VentilationController:
    def __init__(self, logger):
        self.logger = logger
        self.fan_relay = Pin(25, Pin.OUT)
        self.fan_pin = self.fan_relay
        self.target_pct = 0
        self.mode = "idle"
        self.manual_override = False

    def set_manual_override(self, enabled):
        self.manual_override = enabled

    def update(self, temperature_c, humidity_pct, co2_ppm, ammonia_ppm, mqtt_connected):
        thresholds = ENVIRONMENT_THRESHOLDS
        # Local emergency logic takes precedence over MQTT or HA state.
        if ammonia_ppm >= thresholds["ammonia_critical_ppm"]:
            self.target_pct = thresholds["max_ventilation_pct"]
            self.mode = "emergency"
            self.logger.warn("Emergency ventilation: ammonia %.1f ppm" % ammonia_ppm)
        elif co2_ppm >= thresholds["co2_critical_ppm"] or humidity_pct >= thresholds["humidity_critical_pct"]:
            self.target_pct = thresholds["max_ventilation_pct"]
            self.mode = "boost"
        elif ammonia_ppm >= thresholds["ammonia_high_ppm"]:
            self.target_pct = 70
            self.mode = "high"
        elif co2_ppm >= thresholds["co2_high_ppm"]:
            self.target_pct = 60
            self.mode = "co2"
        elif humidity_pct >= thresholds["humidity_high_pct"]:
            self.target_pct = 50
            self.mode = "humidity"
        elif temperature_c >= thresholds["temperature_high_c"]:
            self.target_pct = 45
            self.mode = "temperature"
        elif not mqtt_connected:
            self.target_pct = thresholds["min_ventilation_pct"]
            self.mode = "local_safe"
        else:
            self.target_pct = thresholds["min_ventilation_pct"]
            self.mode = "idle"

        if self.manual_override:
            self.target_pct = 100
            self.mode = "manual"

        self.apply()
        return {
            "mode": self.mode,
            "target_pct": self.target_pct,
        }

    def apply(self):
        self.fan_pin.value(1 if self.target_pct > 0 else 0)
        return self.target_pct
