# Smart Chicken Coop – Architecture, planning and ESP32 firmware

This repository captures the design and implementation foundation for an intelligent laying-hen coop based on the project brief.

The project combines:

- mechanical ventilation based on house volume, flock density and environmental control,
- ESP32-based local automation written in MicroPython,
- MQTT communication to Mosquitto,
- Home Assistant supervision,
- fail-safe operation that remains functional without Wi‑Fi or MQTT availability.

The repository currently contains both the architectural design stage and the first working firmware implementation scaffold for the controller.

## 1. Project summary

- Building footprint: 2.20 m × 2.00 m
- Height: approx. 1.80 m
- Floor area: 4.40 m²
- Volume: approx. 7.92 m³
- Capacity: 10–15 laying hens
- Ventilation: mechanical, controlled intake and exhaust
- Power: 230 V AC
- Controller: ESP32 DevKit / ESP32-WROOM-32
- Firmware: MicroPython
- Communication: MQTT via Mosquitto
- Supervision: Home Assistant
- Target budget: PLN 1500–3000 (without compromising animal safety or electrical safety)

## 2. Design priorities

1. Welfare and safety of the hens
2. Reliable local control even without Wi‑Fi or MQTT
3. Electrical safety
4. Ease of service and maintenance
5. Integration with Home Assistant
6. Reasonable cost
7. Expandability

## 3. Scope covered in this repository

The project includes:

- requirement analysis
- system architecture
- preliminary hardware selection
- ventilation concept and local safety strategy
- block-level wiring concept
- repository structure for deployment and future expansion
- first working MicroPython modules for ESP32
- MQTT connectivity strategy with HA-ready discovery
- lighting, ventilation, door and monitoring logic references

## 4. Firmware status

The firmware exists as a modular baseline and is intentionally local-first. The system keeps critical decisions inside the ESP32, with MQTT and Home Assistant acting as an optional supervisory layer rather than the primary safety control layer.

The current implementation includes modules for:

- Wi‑Fi handling and reconnect
- MQTT broker connection and discovery
- sensor reading for temperature, humidity, CO₂ and ammonia-related analog input
- local ventilation logic with emergency behaviour
- door control and obstacle-safe logic
- lighting schedule logic
- feeder and water anomaly monitoring
- safety aggregation and diagnostic state

## 5. Key files

- [requirements.md](./requirements.md) – requirement analysis and missing-data checklist
- [hardware/hardware_list.md](./hardware/hardware_list.md) – preliminary hardware shortlist
- [hardware/wiring_diagram.md](./hardware/wiring_diagram.md) – high-level connection concept
- [hardware/pinout.md](./hardware/pinout.md) – preliminary ESP32 pin planning
- [hardware/electrical_safety.md](./hardware/electrical_safety.md) – safety guidelines
- [documentation/system_architecture.md](./documentation/system_architecture.md) – architecture overview
- [documentation/automation_logic.md](./documentation/automation_logic.md) – automation logic concept
- [documentation/calibration.md](./documentation/calibration.md) – calibration workflow
- [documentation/troubleshooting.md](./documentation/troubleshooting.md) – failure and service checks
- [firmware/README.md](./firmware/README.md) – MicroPython firmware overview
- [home_assistant/mqtt_entities.yaml](./home_assistant/mqtt_entities.yaml) – MQTT topic and HA discovery template
- [tests/](./tests) – validation plans for sensors, connectivity and failure modes

## 6. Missing data and open points

Before final production deployment, the following should be confirmed on site:

- actual coop orientation and exposure to sun and wind
- final inlet and exhaust geometry
- local outdoor climate and winter conditions
- litter and manure handling method
- exact layout of feeders, drinkers, nest boxes and perch positions
- final fan model and duct dimensions
- exact ammonia sensor model and calibration procedure
- final door actuator and end-stop arrangement
- final GPIO map after enclosure and cable routing confirmation

## 7. Safety note

This project involves 230 V AC mains power, moving door hardware and environmental control. All installation and mains work must be carried out by a qualified electrician or competent person in accordance with local rules and standards.

## 8. Acceptance gate

The design is accepted for extension into production-grade commissioning after the following have been confirmed:

- ventilation dimensioning and local fail-safe logic,
- hardware selection and safe power distribution,
- final sensor placement and calibration plan,
- local control behavior without HA or MQTT,
- key missing measurements and environmental assumptions.

## 9. Next development steps

Recommended next steps:

1. final sensor selection and placement validation,
2. final fan sizing and flow verification,
3. real-world calibration of SHT31, SCD41 and NH₃ sensor,
4. validation of door obstruction and end-stop logic,
5. Home Assistant dashboard tuning,
6. failure-mode testing and production startup checklist.
