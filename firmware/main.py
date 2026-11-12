# Main application entry point for the Smart Chicken Coop controller.
# The module is designed to run locally even when Wi-Fi or MQTT is unavailable.

import json
import utime

from config import (
    MQTT_BASE_TOPIC,
    LIGHT_ON_HOUR,
    LIGHT_OFF_HOUR,
)
from logger import Logger
from wifi_manager import WifiManager
from mqtt_manager import MQTTController
from sensor_manager import SensorManager
from feeder import FeederMonitor
from water_monitor import WaterMonitor
from ventilation import VentilationController
from lighting import LightingController
from door_controller import DoorController
from safety_manager import SafetyManager

logger = Logger("MAIN")


def on_mqtt_message(topic, message):
    logger.info("MQTT message on %s: %s" % (topic, message))
    if topic.endswith("ventilation/command"):
        if message in (b"on", b"1"):
            logger.info("Manual ventilation enabled")
        else:
            logger.info("Manual ventilation disabled")
    if topic.endswith("lighting/command"):
        if message in (b"on", b"1"):
            logger.info("Manual lighting enabled")
        else:
            logger.info("Manual lighting disabled")
    if topic.endswith("door/command"):
        if message in (b"open", b"OPEN"):
            logger.info("Door command: open")
        elif message in (b"close", b"CLOSE"):
            logger.info("Door command: close")


def publish_telemetry(mqtt, env, feeder, water, vent_state, lighting_state, door_state, health):
    mqtt.publish(MQTT_BASE_TOPIC + "/environment/temperature", str(env["temperature_c"]))
    mqtt.publish(MQTT_BASE_TOPIC + "/environment/humidity", str(env["humidity_pct"]))
    mqtt.publish(MQTT_BASE_TOPIC + "/environment/co2", str(env["co2_ppm"]))
    mqtt.publish(MQTT_BASE_TOPIC + "/environment/ammonia", str(env["ammonia_ppm"]))
    mqtt.publish(MQTT_BASE_TOPIC + "/feeder/level", str(feeder["level_pct"]))
    mqtt.publish(MQTT_BASE_TOPIC + "/feeder/alert", "1" if feeder["low_feed"] else "0")
    mqtt.publish(MQTT_BASE_TOPIC + "/water/flow", str(water["flow_lpm"]))
    mqtt.publish(MQTT_BASE_TOPIC + "/water/consumption", str(water["total_liters"]))
    mqtt.publish(MQTT_BASE_TOPIC + "/ventilation/state", vent_state["mode"])
    mqtt.publish(MQTT_BASE_TOPIC + "/ventilation/speed", str(vent_state["target_pct"]))
    mqtt.publish(MQTT_BASE_TOPIC + "/lighting/state", lighting_state["state"])
    mqtt.publish(MQTT_BASE_TOPIC + "/door/state", door_state["state"])
    mqtt.publish(MQTT_BASE_TOPIC + "/system/health", json.dumps(health))
    mqtt.publish(MQTT_BASE_TOPIC + "/system/availability", "online", retain=True)


def run():
    logger.info("Starting Smart Chicken Coop main loop")

    wifi = WifiManager(logger)
    sensors = SensorManager()
    vent = VentilationController(logger)
    lights = LightingController(logger)
    door = DoorController(logger)
    feeder = FeederMonitor(sensors, logger)
    water = WaterMonitor(sensors, logger)
    safety = SafetyManager(logger)

    mqtt = MQTTController(logger, callback=on_mqtt_message)
    mqtt.subscribe(MQTT_BASE_TOPIC + "/ventilation/command")
    mqtt.subscribe(MQTT_BASE_TOPIC + "/lighting/command")
    mqtt.subscribe(MQTT_BASE_TOPIC + "/door/command")

    wifi_connected = False
    mqtt_connected = False

    while True:
        try:
            if not wifi_connected:
                wifi_connected = wifi.connect()
                if not wifi_connected:
                    utime.sleep(2)
                    continue

            if wifi_connected and not mqtt_connected:
                mqtt_connected = mqtt.connect()
                if mqtt_connected:
                    mqtt.subscribe(MQTT_BASE_TOPIC + "/ventilation/command")
                    mqtt.subscribe(MQTT_BASE_TOPIC + "/lighting/command")
                    mqtt.subscribe(MQTT_BASE_TOPIC + "/door/command")
                else:
                    if wifi.is_connected():
                        wifi.reconnect()
                    wifi_connected = False

            env_temp = sensors.read_temperature_humidity()
            env_co2 = sensors.read_co2()
            env = {
                "temperature_c": env_temp["temperature_c"],
                "humidity_pct": env_temp["humidity_pct"],
                "co2_ppm": env_co2["co2_ppm"],
                "ammonia_ppm": sensors.read_ammonia_ppm(),
            }

            feeder_state = feeder.update()
            water_state = water.update()
            vent_state = vent.update(
                env["temperature_c"],
                env["humidity_pct"],
                env["co2_ppm"],
                env["ammonia_ppm"],
                mqtt_connected,
            )

            hour = utime.localtime()[3]
            lighting_state = lights.update(hour, mqtt_connected)
            door_state = door.update(hour, mqtt_connected)
            health = safety.evaluate(env, feeder_state, water_state, mqtt_connected, wifi_connected)

            if mqtt_connected:
                mqtt.loop()
                publish_telemetry(mqtt, env, feeder_state, water_state, vent_state, lighting_state, door_state, health)
            else:
                logger.warn("MQTT unavailable; continuing with local control logic")

        except Exception as exc:
            logger.error("Runtime error: %s" % str(exc))
            if not wifi.is_connected():
                wifi_connected = False
            mqtt_connected = False

        utime.sleep(2)
