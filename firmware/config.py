# Configuration for the ESP32-based chicken coop controller.
# These values are deliberately conservative and require on-site validation.

from machine import Pin, ADC, I2C

# Wi-Fi configuration
WIFI_SSID = "CHANGE_ME"
WIFI_PASSWORD = "CHANGE_ME"
WIFI_RETRY_DELAY_S = 5

# MQTT configuration
MQTT_BROKER = "192.168.1.50"
MQTT_PORT = 1883
MQTT_USERNAME = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = "smart_chicken_coop_esp32"
MQTT_BASE_TOPIC = "chicken_coop"
MQTT_DISCOVERY_PREFIX = "homeassistant"
MQTT_KEEPALIVE_S = 60
MQTT_RETRY_DELAY_S = 5

# ESP32 GPIO assignments
# These are realistic default mappings for a development board. Final pin allocation
# must be validated during wiring and enclosure layout.
I2C_SDA_PIN = 21
I2C_SCL_PIN = 22

FAN_RELAY_PIN = 25
LIGHT_RELAY_PIN = 26
DOOR_MOTOR_OPEN_PIN = 32
DOOR_MOTOR_CLOSE_PIN = 33
DOOR_LIMIT_OPEN_PIN = 34
DOOR_LIMIT_CLOSE_PIN = 35
DOOR_POSITION_PIN = 36
FEED_LEVEL_PIN = 27
WATER_FLOW_PIN = 14
BUZZER_PIN = 4

# Recommended provisional thresholds for the initial commissioning phase.
# These are NOT final safety-critical values and must be tuned against real-world
# house conditions, flock density and bird welfare guidance.
ENVIRONMENT_THRESHOLDS = {
    "temperature_high_c": 28.0,
    "temperature_critical_c": 32.0,
    "humidity_high_pct": 70.0,
    "humidity_critical_pct": 80.0,
    "co2_high_ppm": 1500,
    "co2_critical_ppm": 2500,
    "ammonia_high_ppm": 15.0,
    "ammonia_critical_ppm": 25.0,
    "min_ventilation_pct": 15,
    "max_ventilation_pct": 100,
}

# Feed and water calibration
FEED_LOW_THRESHOLD_PCT = 15.0
WATER_PULSE_LITERS = 0.01
WATER_ANOMALY_FLOW_LITER_PER_MIN = 2.0
WATER_ANOMALY_WINDOW_S = 90

# Lighting schedule
LIGHT_ON_HOUR = 6
LIGHT_OFF_HOUR = 21

# Door schedule (local safe default)
DOOR_OPEN_HOUR = 7
DOOR_CLOSE_HOUR = 20

# Pin helpers used by modules.
def i2c_bus():
    return I2C(0, scl=Pin(I2C_SCL_PIN, Pin.OUT), sda=Pin(I2C_SDA_PIN, Pin.OUT), freq=100000)


def read_adc_pin(pin_num):
    return ADC(Pin(pin_num, Pin.IN))
