# Sensor validation plan

## 1. Environmental sensor tests

- verify SHT31 temperature/humidity readings against a calibrated reference
- validate SCD41 CO₂ reading stability over time
- validate NH₃ sensor range and noise behavior
- confirm sensor placement away from direct airflow and heat source effects

## 2. Acceptance criteria

- stable values under normal operation
- no random jumps after startup
- consistent readings across daily cycles
- sensor data remains available when MQTT is offline
