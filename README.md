# Smart Chicken Coop – Architecture and implementation scaffold

This repository captures the design and implementation foundation for an intelligent laying-hen coop based on the project brief. The first phase defined the system requirements, architecture, ventilation concept, preliminary hardware shortlist and missing-data checklist. The design was accepted, and the second phase introduces the ESP32 firmware module skeleton for the controller.

The project now contains the architecture documentation and the initial implementation-ready MicroPython module structure.

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

## 3. Scope of this phase

This repository includes the initial design stage required by the brief:

- analysis of requirements
- system architecture
- preliminary hardware shortlist
- ventilation concept
- block-level wiring concept
- repository structure for the full project
- list of open questions and missing measurements

## 4. Current status

The system is not yet implemented in firmware. This repository stores the architecture and planning foundations for the next phase.

## 5. Key files

- [requirements.md](./requirements.md) – detailed requirement analysis and missing-data checklist
- [hardware/hardware_list.md](./hardware/hardware_list.md) – preliminary hardware shortlist
- [hardware/wiring_diagram.md](./hardware/wiring_diagram.md) – high-level connection concept
- [hardware/pinout.md](./hardware/pinout.md) – preliminary ESP32 pin planning
- [hardware/electrical_safety.md](./hardware/electrical_safety.md) – safety guidelines
- [documentation/system_architecture.md](./documentation/system_architecture.md) – architecture overview
- [documentation/automation_logic.md](./documentation/automation_logic.md) – initial automation logic concept
- [documentation/calibration.md](./documentation/calibration.md) – required calibration workflow
- [home_assistant/mqtt_entities.yaml](./home_assistant/mqtt_entities.yaml) – MQTT topic and Home Assistant discovery template
- [tests/](./tests) – validation plan for sensors, connectivity and failure modes

## 6. Acceptance gate

The design must be accepted before full firmware implementation begins. The next step is to review and approve the architecture, hardware selection direction, and missing assumptions. Once approved, the implementation will proceed module by module.
