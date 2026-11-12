# MQTT and connectivity validation plan

## 1. Test cases

- Wi‑Fi reconnect after AP dropout
- MQTT reconnect after broker downtime
- LWT behavior on controller restart or unexpected stop
- retained message update after sensor values change
- HA discovery payload validation
- local safe-state operation when MQTT is unavailable

## 2. Acceptance criteria

- reconnect logic works without manual intervention
- local control continues when MQTT is lost
- no blocked states from a failed broker connection
