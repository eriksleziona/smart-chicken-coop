# Feed monitoring logic.

from machine import Pin

from config import FEED_LOW_THRESHOLD_PCT


class FeederMonitor:
    def __init__(self, sensor_manager, logger):
        self.sensor_manager = sensor_manager
        self.logger = logger
        self.low_feed_alert_sent = False

    def update(self):
        level_pct = self.sensor_manager.read_feed_level_pct()
        low_feed = level_pct <= FEED_LOW_THRESHOLD_PCT
        if low_feed and not self.low_feed_alert_sent:
            self.logger.warn("Low feed level detected: %.1f%%" % level_pct)
            self.low_feed_alert_sent = True
        elif not low_feed:
            self.low_feed_alert_sent = False
        return {
            "level_pct": level_pct,
            "low_feed": low_feed,
        }
