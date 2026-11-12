# Requirements analysis

## 1. Project brief summary

The project is a compact, mechanically ventilated laying-hen coop with the following operating envelope:

- 2.20 m x 2.00 m footprint
- approx. 1.80 m average height
- 4.40 m² floor area
- 7.92 m³ usable volume
- 10–15 laying hens
- 230 V AC power distribution
- ESP32-based automation
- MicroPython firmware
- MQTT communication with Mosquitto
- Home Assistant as the supervisory system

This project is not a generic smart barn; it is a purpose-built poultry environment where thermal balance, air quality, and local fail-safe operation are the highest priorities.

## 2. Functional requirements

### Environmental monitoring
The system must monitor at least:

- indoor temperature
- relative humidity
- CO₂ concentration
- ammonia (NH₃) if feasible using a dedicated sensor
- optional second temperature measurement at a secondary location

### Ventilation control
The ventilation system must:

- provide an adjustable minimum airflow rate
- provide a higher-flow emergency or summer mode
- respond to temperature, humidity, CO₂ and NH₃
- remain operational locally if Wi‑Fi, MQTT or Home Assistant is unavailable
- offer a safe emergency response rather than full shutdown

### Feeding and water monitoring
The controller should support:

- feed-level detection (capacitive or analog detection concept)
- low-feed alarm
- water-flow measurement
- consumption tracking
- anomaly detection for abnormal water use or flow loss
- maintenance-friendly diagnostics

### Door control
The system must support automated poultry access control with:

- safe travel limits
- obstruction detection
- end-stop sensing
- manual override
- fail-safe safe-state behavior with interlock logic

### Lighting
The lighting system must:

- control a safe daily light cycle
- use a schedule aligned with welfare and laying performance expectations
- permit manual override
- support gradual dimming if implemented without excessive complexity

### Power and safety
The design must:

- separate 230 V mains protection from low-voltage ESP32 domain
- protect against overloads and surges as appropriate
- include proper enclosure selection and cable management
- avoid unsafe prototyping practices on breadboards when mains wiring is involved

## 3. Non-functional requirements

- reliability under dust, humidity and temperature variation
- maintainability with replaceable sensors and standard terminal blocks
- local autonomy during connectivity loss
- data traceability via MQTT payloads, logs and HA entities
- simple expansion path for future modules

## 4. Assumptions and design constraints

The following assumptions are considered valid for the first design stage:

- The static ventilation demand depends on family flock density, bedding quality, litter moisture, local climate and winter conditions.
- The final ventilation strategy should not be based on building volume alone.
- Fresh air intake must avoid direct drafts at hen height.
- The controller must keep local logic independent from centralized cloud logic.
- The design must be serviceable without needing to remove the complete enclosure.

## 5. Missing technical data to confirm before implementation

The following data needs confirmation before final component selection and final threshold values:

1. Actual poultry house orientation and exposure to sun and wind
2. Exact location of the coop and seasonal outdoor climate
3. Presence of a roof overhang, ridge vent or insulated wall assembly
4. Litter type and moisture management strategy
5. Internal layout: nesting boxes, perches, feeder, drinker, door and inspection access
6. Number of birds and likely seasonal variation in flock size
7. Whether the coop is free-running or linked to a larger barn system
8. Preferred position for intake and exhaust vents relative to the floor and roofline
9. Exact fan mounting space and available shaft clearance
10. Requirements for noise reduction or a low-noise intake design
11. Preference for manual override vs fully automated operations
12. Whether the system needs to support remote maintenance or only local and Home Assistant control

## 6. Design decisions already made at phase 1

- Controller: ESP32-WROOM-32 on a stable devkit / breakout board
- Firmware: MicroPython
- Communications: MQTT over Wi‑Fi with HA discovery
- Local fail-safe behavior remains mandatory even when MQTT is unavailable
- Ventilation must be the primary controlled environmental system
- Safety-critical electrical work must be performed by qualified persons

## 7. Risk areas

The main risk areas are:

- ammonia and CO₂ sensors requiring calibration and placement strategy
- ventilation design being underestimated for winter or summer extremes
- stale air pockets created by poor intake distribution
- drafts at hen level
- over-automation without proper animal welfare thresholds

## 8. Preliminary recommendation

The first implementation should prioritize a robust, modular architecture with:

- a dedicated environmental sensing module
- a standalone ventilation controller with local logic
- an independent safety state machine
- MQTT telemetry and HA discovery as an overlay, not the core safety layer
- modular sensor input interfaces to allow calibration and replacement

## 9. Acceptance gate for architecture

Architecture may proceed to implementation only after the following are accepted:

1. ventilation concept and control philosophy
2. initial hardware list and high-level power architecture
3. key environmental sensors and placement strategy
4. local fail-safe strategy with no dependency on HA or MQTT
5. list of missing building measurements and assumptions

This repository is intentionally limited to the architecture and requirement analysis stage until these points are acknowledged.
