# Troubleshooting plan

This is a living document for the initial architecture phase. It captures the main failure modes and investigation flow expected during commissioning.

## 1. Typical symptoms and checks

### Wi‑Fi not connecting
- verify antenna and local radio conditions
- review power supply quality
- inspect logs for DHCP and authentication issues
- confirm AP credentials and SSID validation

### MQTT unavailable
- check broker availability
- verify credentials and topics
- verify LWT and retention behavior
- confirm that the controller still runs local safety logic

### Humidity too high
- inspect inlet flow and stale air pockets
- verify sensor location and condensation conditions
- evaluate litter moisture and bedding management

### CO₂ too high
- review ventilation run time and intake path
- confirm fan speed is sufficient for duty cycle
- verify sensor placement and drift

### NH₃ too high
- check ventilation mode and emergency logic
- inspect litter and manure management
- confirm sensor calibration and drift

### Door not moving
- inspect end-stop switches
- validate obstacle detection and limit inputs
- check motor power and driver state
- confirm manual override state

## 2. Diagnostic principle

Treat the system as a layered device: power, sensors, logic, actuator, communication. Localize the failure before changing thresholds or hardware.
