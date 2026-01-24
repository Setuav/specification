# Propulsion Performance

This module contains **static (ground test)** performance data and overall system efficiency for the motor-propeller combination.

## Static Performance (Full Throttle)

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **static_thrust_max** | `g` | Total thrust produced at maximum throttle. |
| **static_power_max** | `W` | Total power consumed at maximum throttle. |
| **static_current_max** | `A` | Total current drawn at maximum throttle. |
| **static_efficiency** | `g/W` | Thrust produced per unit power (efficiency) at full throttle. |

## System Metrics

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **thrust_to_weight** | `-` | Thrust / Weight ratio. Values >1 indicate unlimited vertical climb capability. |
| **pitch_speed** | `m/s` | Theoretical air speed based on propeller pitch. typically limits the maximum flight speed. |

## Example Configuration

```yaml
propulsion:
  static_thrust_max: 2500
  static_power_max: 450
  thrust_to_weight: 0.8
  curves:
    rpm: [1000, 5000, 10000]
    thrust: [50, 600, 2500]
```
