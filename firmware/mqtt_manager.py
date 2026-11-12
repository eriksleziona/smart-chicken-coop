# MQTT helper for the chicken coop. This is intentionally kept lightweight.
# It uses the widely available umqtt.robust client for MicroPython.

import json
import utime

from config import (
    MQTT_BROKER,
    MQTT_PORT,
    MQTT_USERNAME,
    MQTT_PASSWORD,
    MQTT_CLIENT_ID,
    MQTT_BASE_TOPIC,
    MQTT_KEEPALIVE_S,
)

try:
    from umqtt.robust import MQTTClient
except ImportError:
    class MQTTClient:
        def __init__(self, *args, **kwargs):
            raise ImportError("umqtt.robust is required for MQTT support")


class MQTTController:
    def __init__(self, logger, callback=None):
        self.logger = logger
        self.callback = callback
        self.client = MQTTClient(
            MQTT_CLIENT_ID,
            MQTT_BROKER,
            MQTT_PORT,
            user=MQTT_USERNAME,
            password=MQTT_PASSWORD,
            keepalive=MQTT_KEEPALIVE_S,
        )
        self.connected = False

    def connect(self):
        try:
            self.client.connect()
            self.connected = True
            self.logger.info("Connected to MQTT broker at %s" % MQTT_BROKER)
            self.client.set_last_will(
                MQTT_BASE_TOPIC + "/system/availability",
                "offline",
                retain=True,
                qos=0,
            )
            self.client.publish(
                MQTT_BASE_TOPIC + "/system/availability",
                "online",
                retain=True,
                qos=0,
            )
            return True
        except Exception as exc:
            self.logger.error("MQTT connect failed: %s" % str(exc))
            self.connected = False
            return False

    def subscribe(self, topic):
        if self.connected:
            self.client.subscribe(topic)

    def publish(self, topic, payload, retain=False):
        if self.connected:
            try:
                self.client.publish(topic, payload, retain=retain, qos=0)
            except Exception as exc:
                self.logger.warn("MQTT publish failed for %s: %s" % (topic, str(exc)))
                self.connected = False

    def publish_json(self, topic, data, retain=False):
        self.publish(topic, json.dumps(data), retain=retain)

    def loop(self):
        if self.connected:
            try:
                self.client.check_msg()
            except Exception as exc:
                self.logger.warn("MQTT loop error: %s" % str(exc))
                self.connected = False

    def handle_incoming(self, topic, msg):
        if self.callback is not None:
            self.callback(topic, msg)

    def disconnect(self):
        try:
            self.client.disconnect()
        except Exception:
            pass
        self.connected = False
