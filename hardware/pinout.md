# Preliminary ESP32 pin planning

This file provides only a preliminary planning template. Final pin assignment must be confirmed after wiring layout, sensor selection and enclosure design are finalized.

## 1. Signal groups

### Power and debug
- 3V3: sensor supply only where appropriate per chip datasheet
- GND: common reference for digital and analog low-voltage logic
- EN: reset or keep high according to design
- GPIO0 / GPIO2 / GPIO4 / GPIO5: reserved or used only after careful review of boot and strapping status
- UART0: reserved for programming and debug unless intentionally repurposed

### I²C sensors
- SCL: GPIO assigned after final layout review
- SDA: GPIO assigned after final layout review
- Sensor supply and pull-up configuration according to module datasheet

### Digital inputs
- door end-stop switches
- obstacle detection input
- feed-level sensor digital state
- water-flow pulse input
- general alarm input or maintenance switch

### Digital outputs
- ventilation relay / fan control output
- lighting relay output
- door motor drive logic
- buzzer or local alarm output
- local status LEDs

### Analog inputs
- optional analog sensor or 0–3.3 V measurement
- calibration and filtering required

## 2. Critical design rule

Do not assign final pins until the actual board layout, sensor cable lengths and power-supply layout are known. Some pins are recommended for specific functions only after boot-state and strapping constraints are checked.

## 3. High-level map

```text
ESP32
├── I²C bus: SHT31, SCD41, optional sensor hub
├── UART: programming / debug
├── GPIO: ventilation relay output
├── GPIO: lighting relay output
├── GPIO: door motor driver / direction logic
├── GPIO: door position input
├── GPIO: door end-stop inputs
├── GPIO: feed-level input
├── GPIO: water-flow pulse input
├── GPIO: local alarm / buzzer
├── ADC: optional analog input or sensor conditioning output
└── GND / 3V3 power rails
```

## 4. Finalization requirements

Before hardware build:

- confirm actual sensor module I²C addresses
- confirm noise immunity for long sensor cables
- verify pull-up resistors and voltage compatibility
- confirm each output is protected for the actual load
- ensure the relay / MOSFET stage is sized correctly for the load current
