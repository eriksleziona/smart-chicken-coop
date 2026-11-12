# Electrical safety and installation notes

## 1. Safety hierarchy

1. Animal welfare and safe operation
2. Electrical protection from shock and fire
3. Reliable local fail-safe logic
4. Serviceability

## 2. Mandatory separation

The design must physically and functionally separate:

- 230 V AC mains circuits
- 12 V DC actuator and power distribution branches
- ESP32 logic domain and sensor signal domain

This separation reduces electrical noise and protects the microcontroller from transients and faults.

## 3. Installation constraints

The following work must be carried out or reviewed by a qualified electrician or competent installer:

- 230 V AC mains wiring
- connection to mains protection devices
- enclosure selection and IP-rated installation
- final fuse and MCB sizing
- surge protection where required by local code
- installation of any mains-powered fan or lighting circuits

## 4. Protection principles

- use appropriately rated fuses and circuit breakers
- use surge protection on the mains side when justified by local conditions
- use terminal blocks with clear labels
- keep cable routing neat and strain-relieved
- avoid breadboard-based mains wiring under any circumstances
- use shielded or twisted sensor wiring where noise sensitivity is expected

## 5. Enclosure strategy

- use an outdoor-rated enclosure for the control cabinet
- reserve space for service access, spare terminal blocks and future expansion
- ensure adequate airflow for electrical components while limiting ingress from dust and moisture
- place the ESP32 in a dry compartment and protect it from condensation and direct water spray

## 6. Fail-safe behavior

A total loss of Wi‑Fi or MQTT must not leave the coop in a dangerous state. The ventilation and lighting logic should be local and deterministic. If the controller fails, the system should degrade to a safe default regime rather than an unsafe one.

## 7. Documentation and labeling

Every final installation should include:

- wiring labels for each conductor
- a one-line power diagram
- a sensor map with names and locations
- emergency shutdown procedure and maintenance notes

## 8. Final responsibility

The project is not a consumer appliance. It is a building system with mains power, moving elements and animal safety implications. Final installation quality and safety verification are the responsibility of a qualified person.
