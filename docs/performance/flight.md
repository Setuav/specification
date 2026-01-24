# Flight Performance

This module contains metrics defining the aircraft's flight envelope and mission performance.

## V-Speeds

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **stall_speed** | `m/s` | Minimum speed where weight can be supported (at CL_max). |
| **cruise_speed** | `m/s` | Efficient cruise speed (typically around L/D max). |
| **max_speed** | `m/s` | Maximum level flight speed where engine power overcomes drag. |

## Cruise Performance

Expected values at cruise speed (`cruise_speed`):

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **power_required** | `W` | Engine/propeller output power required for cruise. |
| **current_draw** | `A` | Current drawn from the battery. |
| **endurance_hours** | `hours` | Total time aloft. |
| **range_km** | `km` | Total flight range. |

## Performance Curves

Power and thrust requirements calculated for various flight speeds are presented as arrays under the `curves` object. These data are used to plot "Power Required vs Speed" graphs.

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **velocities** | `m/s` | Array of velocities (X-axis). |
| **power_required** | `W` | Power required at each velocity step (Y-axis). |
| **power_available** | `W` | Maximum power available at each velocity step. |
| **thrust_required** | `N` | Thrust required (equal to Drag) at each velocity step. |
| **thrust_available** | `N` | Maximum thrust available at each velocity step. |

## Example Configuration

```yaml
flight:
  stall_speed: 12.0
  cruise_speed: 18.0
  max_speed: 32.0
  max_climb_rate: 6.5
  cruise_performance:
    power_required: 145
    current_draw: 6.5
    endurance_hours: 1.8
    range_km: 110
  curves:
    velocities: [10, 12, 14, 16, 18, 20, 25, 30]
    power_required: [200, 160, 140, 135, 145, 170, 250, 400]
    power_available: [600, 580, 560, 540, 520, 500, 450, 400]
    thrust_required: [15, 11, 9, 8, 8, 9, 12, 18]
    thrust_available: [40, 35, 30, 25, 20, 18, 15, 10]
```
