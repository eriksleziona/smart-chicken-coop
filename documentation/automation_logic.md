# Automation logic (preliminary)

This document defines the control philosophy only. Threshold values and exact timings are intentionally left as design inputs pending source review and final acceptance.

## 1. Control principles

- Use hysteresis to avoid rapid on/off switching.
- Use minimum dwell time before action changes.
- Maintain local fail-safe logic independent of Home Assistant.
- Distinguish between warnings, alarms and emergency states.
- Prefer staged response over binary extremes.

## 2. Control hierarchy

### Environmental control
- temperature control: mild increase of ventilation when high temperature is detected
- humidity control: increase airflow to reduce condensation and dampness
- CO₂ control: increase ventilation when a gas buildup threshold is crossed
- NH₃ control: emergency ventilation and alarm if gas exceeds a critical threshold

### Daily schedule logic
- lighting schedule aligned with welfare and flock rest requirements
- manual override accepted only within safe bounds
- door schedule based on daylight or a configured wall-clock schedule

### Device health logic
- feed-low detection triggers alert
- flow or water anomalies trigger health warnings
- communication and controller health status reported to MQTT and HA

## 3. Preliminary alarm categories

- warning: monitor and report, but no immediate harm
- alarm: create clear notification and control action
- emergency: immediate increase airflow and local system response

## 4. Required data before final thresholds

The following are required before locking final setpoints:

- actual local climate and winter conditions
- measured building leakage and intake quality
- flock and litter conditions
- final sensor placement and ventilation geometry
- animal welfare guidance and any specific farm policy

## 5. Design stance

Thresholds may be based on recommended poultry guidance, but the final implementation must avoid arbitrary values. Values should be marked as:

- recommended by source or standard
- temporary for validation in the field
- requiring consultation with a veterinarian or poultry specialist

This is especially important for ammonia, CO₂, humidity and door operation timing.
