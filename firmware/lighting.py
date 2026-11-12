# Lighting control for poultry welfare and local schedule maintenance.
# The schedule is intentionally conservative and local-first: it keeps the daily
# light cycle working without depending on Home Assistant.

import utime

from config import LIGHT_ON_HOUR, LIGHT_OFF_HOUR


class LightingController:
    def __init__(self, logger):
        self.logger = logger
        self.manual_mode = False
        self.state = "off"
        self.output = None

    def set_manual(self, enabled):
        self.manual_mode = enabled

    def update(self, hour, mqtt_connected=True):
        if self.manual_mode:
            self.state = "on"
        elif hour >= LIGHT_ON_HOUR and hour < LIGHT_OFF_HOUR:
            self.state = "off"
        else:
            self.state = "on"

        if self.state == "on":
            self.logger.info("Lighting enabled")
        else:
            self.logger.info("Lighting off by schedule")
        return {"state": self.state}

    def force_on(self):
        self.manual_mode = True
        self.state = "on"

    def force_off(self):
        self.manual_mode = False
        self.state = "off"
