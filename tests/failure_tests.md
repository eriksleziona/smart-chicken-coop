# Failure-mode validation plan

## 1. Failure modes to test

- fan failure or stalled motor
- power drop and recovery
- sensor disconnect or invalid reading
- water-flow anomaly
- door obstruction or end-stop failure
- ESP32 crash or watchdog reset
- loss of Home Assistant or MQTT

## 2. Acceptance criteria

- system degrades to a safe state
- local alarms remain active
- watchdog and startup recovery works reliably
- safe fallback rules remain effective without external systems
