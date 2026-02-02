# Propeller

Fixed-pitch propeller specification for UAV propulsion systems.

## Parameters

### Identification

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **tag** | `str` | Unique identifier for the propeller (e.g., "main_prop", "pusher_prop"). |
| **manufacturer** | `str` | Manufacturer name (optional, e.g., "APC", "GemFan"). |
| **model** | `str` | Model designation (optional, e.g., "10x4.5MR", "10x7E"). |

### Geometric Properties

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **diameter** | `inches` | Propeller diameter (tip to tip). |
| **pitch** | `inches` | Propeller pitch (theoretical advance per revolution). |
| **blade_count** | `int` | Number of blades. |
| **direction** | `enum` | Rotation direction: `CW` or `CCW` when viewed from behind. |
| **hub_diameter** | `mm` | Hub diameter (optional). |
| **hub_thickness** | `mm` | Hub thickness (optional). |

### Physical Properties

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **mass** | `g` | Propeller mass. |
| **material** | `str` | Material type (optional, e.g., "Carbon Fiber", "Plastic", "Wood"). |

## Example Configuration

```yaml
propellers:
  - tag: "main_prop"
    manufacturer: "APC"
    model: "10x4.5MR"
    diameter: 10.0
    pitch: 4.5
    blade_count: 2
    direction: "CW"
    mass: 12
    material: "Plastic"

  - tag: "pusher_prop"
    manufacturer: "GemFan"
    model: "10x7"
    diameter: 10.0
    pitch: 7.0
    blade_count: 2
    direction: "CCW"
    mass: 15
    material: "Carbon Fiber"
    hub_diameter: 8
    hub_thickness: 6
```
