# Smart Chicken Coop firmware

This folder contains the MicroPython firmware for the ESP32-based poultry controller.

## 1. Overview

The firmware is designed around a local-first control model:

- sensors are read locally on the ESP32,
- decisions are made locally,
- Wi‑Fi and MQTT are used as communication overlays,
- any loss of network connectivity must not disable the safety logic.

## 2. Controller responsibilities

The firmware includes the following modules:

- `boot.py` – device boot and startup safety path
- `main.py` – main loop, orchestration and telemetry publishing
- `config.py` – hardware, MQTT and threshold configuration
- `wifi_manager.py` – Wi‑Fi connection and reconnection logic
- `mqtt_manager.py` – MQTT broker connection, discovery and command handling
- `sensor_manager.py` – temperature, humidity, CO₂, ammonia and water/feeder inputs
- `ventilation.py` – local ventilation control and emergency fan logic
- `lighting.py` – local lighting schedule and manual override
- `door_controller.py` – poultry door actuator safety and schedule logic
- `feeder.py` – feed-level monitoring and low-feed alert logic
- `water_monitor.py` – water flow diagnostics and anomaly detection
- `safety_manager.py` – health aggregation and alarm state tracking
- `logger.py` – unified logging helper

## 3. Safety model

The important operating principle is:

- remote automation may assist,
- but it must never be the only layer that protects the birds.

Therefore:

- ventilation responds locally to safety thresholds,
- lighting still follows the local schedule,
- door timing remains local and controlled by local conditions,
- network outages do not disable critical logic.

## 4. Firmware configuration

Before deployment, update the values in `config.py`:

- Wi‑Fi SSID and password
- MQTT broker address and credentials
- ESP32 GPIO assignments
- threshold values for environment and local safety
- door schedule hours
- light schedule hours

## 5. Operational notes

- The project uses MicroPython on ESP32.
- Final hardware pin assignments must be validated against the real PCB or wiring layout.
- All 230 V AC work must be performed by a qualified person.
- This firmware is a solid baseline for real-world commissioning, not a finished substitute for equipment-specific calibration.

## 6. Planned next stages

The following are the recommended next implementation steps:

1. final hardware pin validation,
2. real sensor calibration against reference instruments,
3. precise fan sizing and local ventilation tuning,
4. door end-stop and obstruction validation,
5. HA dashboard and automation refinement,
6. production-testing and failure-mode validation.
