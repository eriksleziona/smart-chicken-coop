# System architecture

## 1. High-level architecture

The coop controller follows a layered architecture, with local automation at the center and Home Assistant as a supervisory interface.

```text
┌───────────────────────────────┐
│ Home Assistant / MQTT UI    │
│ dashboards / automations     │
└──────────────┬────────────────
               │ MQTT / discovery
               ▼
┌───────────────────────────────┐
│ ESP32 controller             │
│ - Wi‑Fi manager             │
│ - MQTT manager              │
│ - safety manager            │
│ - local state machine       │
└───────┬─────────────┬────────┘
        │             │
        ▼             ▼
┌───────────────┐ ┌────────────────────┐
│ Sensors       │ │ Actuation          │
│ temp/humidity │ │ fan                │
│ CO₂ / NH3     │ │ lighting           │
│ flow / feeder │ │ door controller    │
└───────────────┘ └────────────────────┘
```

## 2. Module responsibilities

### Core logic
- maintain real-time state and local timers
- evaluate threshold conditions using hysteresis and dwell time
- enforce safe fallback modes when communication is unavailable
- keep all critical safety logic in the local ESP32, not in Home Assistant

### Sensor layer
- collect environmental data from dedicated sensors
- sanitize values and detect invalid readings
- apply calibration offset and drift handling

### Actuation layer
- fan control
- lighting control
- door actuation and position monitoring
- feed and water monitoring

### Connectivity layer
- Wi‑Fi management with reconnection
- MQTT connection handling, LWT and retained message strategy
- discovery payload publication for Home Assistant entities

## 3. Local decision-making model

The controller should implement priority-based control:

1. safety conditions (e.g., critical ammonia or ventilation failure)
2. environmental health conditions (humidity, CO₂, temperature)
3. daily schedule / automation (lighting, door)
4. remote HA commands when valid and safe

This ordering keeps the coop safe even when cloud or MQTT connectivity is lost.

## 4. Required local states

- normal
- managed ventilation mode
- emergency ventilation mode
- lighting schedule mode
- manual override
- maintenance mode
- fault or alarm state

## 5. Major design recommendation

The ventilation system should be treated as the primary safety system for the coop. If the house is too hot, too humid or overloaded with gases, the controller must increase airflow locally without waiting for HA to react.
