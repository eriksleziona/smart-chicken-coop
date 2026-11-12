# ESP32 pin planning baseline

This file defines a more realistic baseline pin allocation for the current build concept. It is intended to approach a practical installation layout rather than remain purely conceptual.

## 1. Design baseline

The current baseline assumes:

- ESP32 DevKit / WROOM-32 on a clean, stable breakout board
- SHT31 and SCD41 on the I²C bus
- dedicated analog ammonia channel
- feed-level analog sensor on a separate ADC channel
- door actuation with two motor outputs and limit switches
- a local buzzer for alarm events

## 2. Pin map

```text
ESP32 GPIO 21  -> I2C SDA   (SHT31 / SCD41)
ESP32 GPIO 22  -> I2C SCL   (SHT31 / SCD41)
ESP32 GPIO 25  -> Vent fan relay / output
ESP32 GPIO 26  -> Light relay / output
ESP32 GPIO 32  -> Door motor OPEN
ESP32 GPIO 33  -> Door motor CLOSE
ESP32 GPIO 34  -> Door position / feedback input
ESP32 GPIO 27  -> Door close limit input
ESP32 GPIO 14  -> Water flow pulse input
ESP32 GPIO 36  -> Feed level analog input (ADC)
ESP32 GPIO 39  -> NH3 analog input (ADC)
ESP32 GPIO 15  -> Local buzzer or alarm output
ESP32 GND      -> common logic reference
ESP32 3V3       -> regulator to low-voltage sensors as required
```

## 3. Notes on real-world use

- GPIO34 and GPIO39 are input-only analog-friendly channels on many ESP32 variants; verify the exact board details before final wiring.
- GPIO14 is a useful pulse input for a water flow sensor, but the final wiring and signal conditioning should be verified against the chosen sensor output type.
- Keep analog and digital sensor lines away from relay drivers and fan power wiring.
- Use pull-ups or pull-downs only according to the device datasheet and final schematic.

## 4. Reserved or sensitive pins

Avoid using the following for routine digital outputs unless required during final bench testing:

- GPIO0
- GPIO2
- GPIO4 (used here for door open limit in a simpler direct-switch arrangement)
- GPIO5
- UART0 programming pins

## 5. Final installation rules

Before physical wiring is finalized:

- confirm module compatibility with the exact ESP32 board revision,
- confirm sensor cable lengths and available shielding,
- verify actual signal polarity for limit and flow sensors,
- confirm that all relay outputs are sized for the real loads,
- re-check the final enclosure layout and wiring routing before energizing the system.

This pinout is a realistic baseline and should be treated as a production-prep map, not as a guarantee for every PCB variant.
