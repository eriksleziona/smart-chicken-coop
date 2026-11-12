# Preliminary hardware shortlist

This list is not a final purchase specification. It is a candidate list for architecture review and supplier validation before purchase.

## 1. Essential hardware

### Controller and networking
- ESP32 DevKit / ESP32-WROOM-32 module
- 5 V regulated supply for ESP32 logic domain
- USB-UART programming interface or CP2102/CH340-based board if needed
- 2.4 GHz Wi‑Fi antenna and enclosure provision

### Environment sensing
- SHT31 temperature and humidity sensor
- SCD41 CO₂ sensor
- dedicated NH₃ sensor, such as a suitable electrochemical ammonia sensor module
- optional secondary temperature probe in a second area of the coop

### Ventilation
- ventilation fan selected after actual airflow and duct sizing review
- intake vent with damper or adjustable louvres
- exhaust fan with wiring and control device compatible with the selected fan type
- fan control hardware appropriate to the chosen motor type

### Power and protection
- 230 V AC to 12 V DC power supply with appropriate headroom and safety rating
- 12 V to 5 V buck converter for ESP32 logic domain
- fuses, MCB or fuse protection for mains side
- transient protection and surge protection where justified
- IP-rated enclosure for control box
- terminal blocks and labelled wiring

### Actuation
- linear actuator or lifting mechanism for poultry access door
- end-stop switches
- obstacle detection sensor or force-based limit detection
- door position sensor
- relay driver or motor driver board

### Lighting
- LED strip or panel luminaire suitable for poultry housing environment
- relay or MOSFET-based switching stage
- dimming control if a practical design is selected

### Feed and water monitoring
- capacitive or analog feed-level sensing approach with calibration support
- flow sensor for water line, if used in final design
- fittings and connectors for serviceability

## 2. Recommended hardware

- higher-quality terminal blocks and labelled cable glands
- industrial-grade enclosure with DIN rail or panel mount sections
- protected power distribution arrangement
- local status indicators (LEDs) for fan, door, power and alarm states
- real-time clock module if scheduling must persist during outages

## 3. Optional hardware

- additional temperature sensor at secondary zone
- extra environmental sensors for north/south wall differences
- dedicated UPS for ESP32 or RTC retention
- filtration or inlet duct silencers
- service log or data capture extension

## 4. Supplier validation checklist

Before purchase, validate the following for each candidate item:

- supply voltage and tolerance
- current consumption and inrush behaviour
- environmental rating and humidity tolerance
- sensor calibration requirements
- communication interface (I²C, UART, analog, PWM, relay)
- compatibility with ESP32 pins and electrical isolation needs
- maintainability and spare part availability
- EMC and noise immunity in the expected installation environment

## 5. Preliminary selection note

At this stage, it is recommended to retain flexibility on the final fan and ammonia sensor model until the actual coop layout, intake geometry and winter ventilation requirement are reviewed. This is the major factor influencing the final bill of materials.
