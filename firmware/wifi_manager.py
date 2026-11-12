# Wi-Fi manager for ESP32. Keeps the connection logic isolated from other modules.

import network
import utime

from config import WIFI_SSID, WIFI_PASSWORD, WIFI_RETRY_DELAY_S


class WifiManager:
    def __init__(self, logger):
        self.logger = logger
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.connected = False

    def connect(self):
        if self.is_connected():
            self.connected = True
            self.logger.info("Wi-Fi already connected")
            return True

        self.logger.info("Connecting to Wi-Fi: %s" % WIFI_SSID)
        self.wlan.connect(WIFI_SSID, WIFI_PASSWORD)

        for _ in range(40):
            if self.is_connected():
                self.connected = True
                self.logger.info("Wi-Fi connected: %s" % self.wlan.ifconfig()[0])
                return True
            utime.sleep_ms(250)

        self.connected = False
        self.logger.warn("Wi-Fi connection timeout")
        return False

    def reconnect(self):
        self.logger.warn("Initiating Wi-Fi reconnect")
        try:
            self.wlan.disconnect()
        except Exception:
            pass
        utime.sleep_ms(500)
        return self.connect()

    def is_connected(self):
        status = self.wlan.isconnected()
        self.connected = status
        return status

    def disconnect(self):
        self.connected = False
        self.wlan.disconnect()

    def status(self):
        try:
            return self.wlan.ifconfig()
        except Exception:
            return ("0.0.0.0", "0.0.0.0", "0.0.0.0", "0.0.0.0")
