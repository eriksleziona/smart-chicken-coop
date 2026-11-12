# Wi-Fi manager for ESP32. Keeps the connection logic isolated from other modules.

import network
import utime

from config import WIFI_SSID, WIFI_PASSWORD, WIFI_RETRY_DELAY_S


class WifiManager:
    def __init__(self, logger):
        self.logger = logger
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    def connect(self):
        if self.is_connected():
            self.logger.info("Wi-Fi already connected")
            return True

        self.logger.info("Connecting to Wi-Fi: %s" % WIFI_SSID)
        self.wlan.connect(WIFI_SSID, WIFI_PASSWORD)

        for _ in range(20):
            if self.is_connected():
                self.logger.info("Wi-Fi connected: %s" % self.wlan.ifconfig()[0])
                return True
            utime.sleep_ms(500)

        self.logger.warn("Wi-Fi connection timeout")
        return False

    def is_connected(self):
        return self.wlan.isconnected()

    def disconnect(self):
        self.wlan.disconnect()

    def status(self):
        return self.wlan.ifconfig()
