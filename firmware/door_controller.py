# Door controller with local fail-safe behavior.

import utime

from config import DOOR_OPEN_HOUR, DOOR_CLOSE_HOUR


class DoorController:
    def __init__(self, logger):
        self.logger = logger
        self.state = "closed"
        self.manual_override = False
        self.open_time = DOOR_OPEN_HOUR
        self.close_time = DOOR_CLOSE_HOUR
        self.has_open_limit = True
        self.has_close_limit = True

    def set_manual_override(self, enabled):
        self.manual_override = enabled

    def open(self):
        self.state = "opening"
        self.logger.info("Door opening")

    def close(self):
        self.state = "closing"
        self.logger.info("Door closing")

    def stop(self):
        self.state = "stopped"
        self.logger.info("Door stopped")

    def update(self, hour, mqtt_connected=True):
        if self.manual_override:
            return {"state": self.state}

        if hour >= self.open_time and hour < self.close_time:
            if self.state != "open":
                self.open()
                self.state = "open"
        else:
            if self.state != "closed":
                self.close()
                self.state = "closed"

        return {"state": self.state}
