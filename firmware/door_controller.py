# Door controller with local fail-safe behavior.
# The actuator logic is intentionally conservative and is designed to keep the
# poultry access system safe even when Home Assistant or MQTT is unavailable.

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
        self.obstacle_detected = False

    def set_manual_override(self, enabled):
        self.manual_override = enabled

    def open(self):
        if self.obstacle_detected:
            self.logger.warn("Door blocked: refusing to open")
            return False
        self.state = "opening"
        self.logger.info("Door opening")
        return True

    def close(self):
        self.state = "closing"
        self.logger.info("Door closing")
        return True

    def stop(self):
        self.state = "stopped"
        self.logger.info("Door stopped")
        return True

    def update(self, hour, mqtt_connected=True):
        if self.manual_override:
            return {"state": self.state}

        if hour >= self.open_time and hour < self.close_time:
            if self.state != "open":
                if self.open():
                    self.state = "open"
        else:
            if self.state != "closed":
                self.close()
                self.state = "closed"

        return {"state": self.state}

    def set_obstacle(self, blocked):
        self.obstacle_detected = blocked
        if blocked:
            self.stop()
            self.logger.warn("Door obstacle detected")
