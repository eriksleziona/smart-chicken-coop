# Water flow monitoring and anomaly detection.
# This module detects a dry or interrupted drinker line and suspiciously high flow
# that may indicate a leak or failure in the watering system.

import utime

from config import (
    WATER_PULSE_LITERS,
    WATER_ANOMALY_FLOW_LITER_PER_MIN,
    WATER_ANOMALY_WINDOW_S,
)


class WaterMonitor:
    def __init__(self, sensor_manager, logger):
        self.sensor_manager = sensor_manager
        self.logger = logger
        self.last_warning_time = 0

    def update(self):
        water_state = self.sensor_manager.read_water_state()
        flow_lpm = water_state["flow_lpm"]
        total_liters = water_state["total_liters"]
        no_flow = flow_lpm <= 0.0
        abnormal_high_flow = flow_lpm >= WATER_ANOMALY_FLOW_LITER_PER_MIN
        now_ms = utime.ticks_ms()

        if no_flow:
            self.logger.warn("Water flow appears to be zero or interrupted")
        elif abnormal_high_flow:
            if utime.ticks_diff(now_ms, self.last_warning_time) > WATER_ANOMALY_WINDOW_S * 1000:
                self.logger.warn("Potential water leak or abnormal flow: %.2f L/min" % flow_lpm)
                self.last_warning_time = now_ms

        return {
            "flow_lpm": flow_lpm,
            "total_liters": total_liters,
            "no_flow": no_flow,
            "abnormal_high_flow": abnormal_high_flow,
        }

    def reset_warning(self):
        self.last_warning_time = 0
