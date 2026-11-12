# Sensor validation plan

## 1. Environmental sensor tests

- verify SHT31 temperature/humidity readings against a calibrated reference
- validate SCD41 CO₂ reading stability over time
- validate NH₃ sensor range and noise behavior
- confirm sensor placement away from direct airflow and heat source effects
- check each sensor against a known-good calibration reference in the real coop environment

## 2. Automated logic validation

The project now includes a lightweight Python validation layer for the local control logic so the basic fail-safe behavior can be checked without live hardware:

- `python -m unittest tests.test_firmware_logic`

This validates the key fail-safe branches for ventilation, sensor scaling and manual override behavior.

## 3. Acceptance criteria

- stable values under normal operation
- no random jumps after startup
- consistent readings across daily cycles
- sensor data remains available when MQTT is offline
- ventilation escalates safely when ammonia or CO₂ thresholds are exceeded
- manual override still respects a safe emergency fallback path
