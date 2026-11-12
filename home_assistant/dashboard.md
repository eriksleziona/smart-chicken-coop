# Home Assistant dashboard concept

## 1. Core cards

- environmental overview: temperature, humidity, CO₂, NH₃
- local ventilation state and fan-speed indicator
- lighting schedule and manual override
- door state and last command
- feeder level and water consumption
- system health and communication status

## 2. Design principles

- clear status colors for normal, warning and alarm
- local system status always visible
- manual override controls available only in a safe UI pattern
- alerts should remain readable on a phone and on a wall tablet

## 3. Layout idea

- top row: environment metrics
- middle row: ventilation and air quality
- lower row: feeder, water and door status
- footer: health, MQTT availability and last update timestamps
