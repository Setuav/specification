# Propeller

This section defines fixed-pitch propellers used in UAV propulsion systems. Propellers are specified by their geometric properties and performance characteristics.

## Overview

Propellers in the Setuav Standard are defined independently and referenced by motors. The propeller definition includes geometric specifications needed for performance analysis and compatibility verification.

## Parameters

### Identification

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **tag** | `str` | Unique identifier for the propeller (e.g., "main_prop", "pusher_prop"). |
| **manufacturer** | `str` | Manufacturer name (optional, e.g., "APC", "Graupner"). |
| **model** | `str` | Model designation (optional, e.g., "9x4.5", "10x7E"). |

### Geometric Properties

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **diameter** | `mm` | Propeller diameter (tip to tip). |
| **pitch** | `mm` | Propeller pitch (theoretical advance per revolution). |
| **blade_count** | `int` | Number of blades (typically 2, 3, or 4). |
| **direction** | `enum` | Rotation direction: `CW` (clockwise) or `CCW` (counter-clockwise) when viewed from behind. |
| **hub_diameter** | `mm` | Hub diameter (optional). |
| **hub_thickness** | `mm` | Hub thickness (optional). |

### Physical Properties

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **mass** | `g` | Propeller mass. |
| **material** | `str` | Material type (optional, e.g., "carbon_fiber", "nylon", "wood"). |

### Performance Data

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **thrust_data** | `array` | Thrust curve data points (optional). Array of `{rpm, thrust_n, torque_nm, power_w}` objects. |
| **efficiency_data** | `array` | Efficiency data points (optional). Array of `{velocity_ms, efficiency, advance_ratio}` objects. |

#### Thrust Data Structure

Each thrust data point contains:

| Field | Unit | Description |
| :--- | :--- | :--- |
| **rpm** | `RPM` | Rotational speed. |
| **thrust_n** | `N` | Thrust force produced. |
| **torque_nm** | `Nm` | Torque required. |
| **power_w** | `W` | Power consumption. |

#### Efficiency Data Structure

Each efficiency data point contains:

| Field | Unit | Description |
| :--- | :--- | :--- |
| **velocity_ms** | `m/s` | Flight velocity. |
| **efficiency** | `-` | Propulsive efficiency (0-1). |
| **advance_ratio** | `-` | Advance ratio (J = V / (n * D)). |

## Propeller Mounting

Propellers are mounted on motors and do not have independent placement. The propeller position and orientation are determined by its parent motor's placement.

## Example Configuration

```yaml
propellers:
  - tag: "main_prop"
    manufacturer: "APC"
    model: "9x4.5"
    diameter: 228.6  # 9 inches = 228.6mm
    pitch: 114.3     # 4.5 inches = 114.3mm
    blade_count: 2
    direction: "CW"
    mass: 8
    material: "nylon"
  
  - tag: "pusher_prop"
    manufacturer: "Graupner"
    model: "10x7E"
    diameter: 254
    pitch: 177.8
    blade_count: 2
    direction: "CCW"
    mass: 12
    material: "carbon_fiber"
    hub_diameter: 8
    hub_thickness: 6
  
  - tag: "efficiency_prop"
    manufacturer: "APC"
    model: "11x5.5E"
    diameter: 279.4
    pitch: 139.7
    blade_count: 2
    direction: "CW"
    mass: 15
    material: "carbon_fiber"
    thrust_data:
      - rpm: 5000
        thrust_n: 2.5
        torque_nm: 0.08
        power_w: 41.9
      - rpm: 6000
        thrust_n: 3.6
        torque_nm: 0.11
        power_w: 69.1
      - rpm: 7000
        thrust_n: 4.9
        torque_nm: 0.15
        power_w: 110.0
```
