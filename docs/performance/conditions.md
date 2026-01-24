# Analysis Conditions

This section defines the physical and environmental parameters under which the performance report was generated.

## Overview

A UAV's performance (stall speed, climb rate, static margin, etc.) heavily depends on weight, center of gravity position, and atmospheric density. Therefore, the `conditions` section provides mandatory context for every report.

## Physical Conditions

| Parameter | Unit | Required | Description |
| :--- | :--- | :--- | :--- |
| **total_mass** | `g` | Yes | Total flight weight at the time of analysis. |
| **cg_position_x** | `mm` | Yes | Center of Gravity (CG) position from the nose. |

## Atmospheric Conditions

| Parameter | Unit | Default | Description |
| :--- | :--- | :--- | :--- |
| **altitude_msl** | `m` | 0 | Analysis altitude (Above Mean Sea Level). |
| **temperature** | `C` | 15.0 | Ambient temperature. |
| **air_density** | `kg/m³` | 1.225 | Air density. If not provided, it should be calculated from altitude and temperature using the standard atmosphere model. |

## Example Configuration

```yaml
conditions:
  total_mass: 2500       # 2.5 kg flight weight
  cg_position_x: 610.5   # 610.5mm CG position
  altitude_msl: 1000     # 1000m altitude
  temperature: 10.0      # 10 degrees Celsius
  air_density: 1.112     # Approx density at 1000m
```
