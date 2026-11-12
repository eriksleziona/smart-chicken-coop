# Safety manager aggregates health, alerts and local fail-safe behavior.

from config import (
    ENVIRONMENT_THRESHOLDS,
    FEED_LOW_THRESHOLD_PCT,
)


class SafetyManager:
    def __init__(self, logger):
        self.logger = logger
        self.status = {
            "mqtt_connected": False,
            "wifi_connected": False,
            "system_ok": True,
            "warnings": [],
            "alarms": [],
        }

    def evaluate(self, environmental_data, feeder_data, water_data, mqtt_connected, wifi_connected):
        warnings = []
        alarms = []

        if environmental_data["ammonia_ppm"] >= ENVIRONMENT_THRESHOLDS["ammonia_critical_ppm"]:
            alarms.append("ammonia_critical")
        elif environmental_data["ammonia_ppm"] >= ENVIRONMENT_THRESHOLDS["ammonia_high_ppm"]:
            warnings.append("ammonia_high")

        if environmental_data["co2_ppm"] >= ENVIRONMENT_THRESHOLDS["co2_critical_ppm"]:
            alarms.append("co2_critical")
        elif environmental_data["co2_ppm"] >= ENVIRONMENT_THRESHOLDS["co2_high_ppm"]:
            warnings.append("co2_high")

        if environmental_data["humidity_pct"] >= ENVIRONMENT_THRESHOLDS["humidity_critical_pct"]:
            alarms.append("humidity_critical")
        elif environmental_data["humidity_pct"] >= ENVIRONMENT_THRESHOLDS["humidity_high_pct"]:
            warnings.append("humidity_high")

        if environmental_data["temperature_c"] >= ENVIRONMENT_THRESHOLDS["temperature_critical_c"]:
            alarms.append("temperature_critical")
        elif environmental_data["temperature_c"] >= ENVIRONMENT_THRESHOLDS["temperature_high_c"]:
            warnings.append("temperature_high")

        if feeder_data["low_feed"]:
            warnings.append("feed_low")

        if water_data["no_flow"]:
            warnings.append("water_no_flow")
        elif water_data["abnormal_high_flow"]:
            warnings.append("water_abnormal")

        if not mqtt_connected:
            warnings.append("mqtt_lost")

        if not wifi_connected:
            warnings.append("wifi_lost")

        self.status = {
            "mqtt_connected": mqtt_connected,
            "wifi_connected": wifi_connected,
            "system_ok": len(alarms) == 0,
            "warnings": warnings,
            "alarms": alarms,
        }

        if alarms:
            self.logger.warn("Safety alarms: %s" % ", ".join(alarms))
        elif warnings:
            self.logger.warn("Safety warnings: %s" % ", ".join(warnings))

        return self.status
