# Block-level wiring concept

This is a preliminary block diagram for architecture review. Final detailed pin assignments and wiring paths will be defined after the layout, sensor placement and fan selection are approved.

```text
                                 ┌──────────────────────────────┐
                                 │      230 V AC mains         │
                                 │  breaker / RCD / surge      │
                                 └──────────────┬───────────────┘
                                                │
                                                ▼
                                 ┌──────────────────────────────┐
                                 │  Main distribution / fuse    │
                                 │  and contactor / relay      │
                                 └───────┬──────────────┬──────┘
                                         │              │
                ┌────────────────────────┘              └────────────────────────┐
                ▼                                                                 ▼
      ┌──────────────────────┐                                            ┌──────────────────────┐
      │  Ventilation fan     │                                            │  Lighting circuit     │
      │  230 V AC actuator   │                                            │  230 V AC load       │
      └──────────┬───────────┘                                            └──────────┬───────────┘
                 │                                                                    │
                 │                                                                    │
                 ▼                                                                    ▼
      ┌──────────────────────┐                                            ┌──────────────────────┐
      │  Fan control stage   │                                            │  Relay / switch      │
      │  relay / drive /     │                                            │  driver / contactor  │
      │  protection          │                                            └──────────┬───────────┘
      └──────────┬───────────┘                                                       │
                 │                                                                   │
                 └───────────────────────────────┬───────────────────────────────┘
                                                 │
                                                 ▼
                                 ┌──────────────────────────────┐
                                 │  12 V DC power supply       │
                                 │  230 VAC -> 12 VDC          │
                                 └──────────────┬───────────────┘
                                                │
                                                ▼
                                 ┌──────────────────────────────┐
                                 │  12 V -> 5 V buck converter │
                                 │  ESP32 logic domain         │
                                 └──────────────┬───────────────┘
                                                │
                                                ▼
                                 ┌──────────────────────────────┐
                                 │       ESP32 controller       │
                                 │  Wi‑Fi / MQTT / HA bridge   │
                                 └──────┬───────────────┬───────┘
                                        │               │
                        ┌───────────────┘               └───────────────┐
                        ▼                                               ▼
              ┌──────────────────┐                            ┌────────────────────┐
              │ Environmental    │                            │ Actuator / door    │
              │ sensors: SHT31    │                            │ driver + limit     │
              │ SCD41 / NH3      │                            │ switches           │
              └──────────────────┘                            └────────────────────┘
                        │
                        ▼
              ┌──────────────────┐
              │ Feed / water     │
              │ monitoring       │
              └──────────────────┘
```

## Wiring principles

- 230 V AC mains must be physically separated from the ESP32 low-voltage domain.
- Use appropriate cable glands, strain relief and labelled terminals.
- Route sensor signal wires away from fan motor power cables and high-current relays.
- Keep the ESP32 enclosure in a dry, accessible location with proper ventilation.
- Use opto-isolation or galvanic isolation when signal integrity or sensor noise demands it.
- Any direct mains wiring must be completed by a qualified person in line with local laws.

## Notes

- The fan control logic should be local and fail-safe. The controller should not depend on Home Assistant to keep the system in a safe state.
- The door controller will require dedicated limit switches and likely a torque or current-based stop strategy.
- The diagram is intentionally conceptual; it is not a final manufacturing drawing.
