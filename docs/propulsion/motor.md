# Motor

This section defines brushless DC (BLDC) motors used in fixed-wing UAV propulsion systems. Motors are specified by their electrical characteristics, performance parameters, and physical properties.

## Overview

Motors in the Setuav Standard are defined independently from their installation. The motor definition includes all technical specifications needed for performance analysis, power system design, and weight estimation.

## Parameters

### Identification

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **tag** | `str` | Unique identifier for the motor (e.g., "main_motor", "pusher_motor"). |
| **manufacturer** | `str` | Manufacturer name (optional, e.g., "Emax", "T-Motor"). |
| **model** | `str` | Model designation (optional, e.g., "RS2205", "F60 PRO IV"). |

### Electrical Characteristics

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **kv** | `RPM/V` | Motor velocity constant (RPM per volt). |
| **voltage_min** | `V` | Minimum operating voltage. |
| **voltage_max** | `V` | Maximum operating voltage. |
| **current_max** | `A` | Maximum continuous current rating. |
| **resistance** | `Ω` | Phase-to-phase resistance (ohms). |
| **no_load_current** | `A` | Current draw at no load (optional). |

### Physical Properties

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **mass** | `g` | Motor mass including mounting hardware. |
| **diameter** | `mm` | Stator diameter (optional). |
| **length** | `mm` | Motor body length excluding shaft (optional). |
| **shaft_diameter** | `mm` | Output shaft diameter (optional). |
| **shaft_length** | `mm` | Shaft length from motor body (optional). |
| **mounting_screw** | `str` | Mounting screw type (optional, e.g., "M2", "M3"). |
| **mounting_spacing** | `str` | Mounting hole spacing pattern (optional, e.g., "16x16", "12x12", "19x19"). |

## Motor Integration

### Component References

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **esc_ref** | `str` | Reference to the ESC component tag that controls this motor (optional). |
| **propeller_ref** | `str` | Reference to the propeller component tag mounted on this motor (optional). |

### Placement

Motors are positioned in the airframe using the placement object:

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **placement** | `object` | Motor placement in airframe (optional). |
| **placement.position** | `object` | Motor position in SETUAV_BODY frame. |
| **placement.position.x** | `mm` | Longitudinal position (distance from nose tip). |
| **placement.position.y** | `mm` | Lateral position (0 = centerline, positive = right). |
| **placement.position.z** | `mm` | Vertical position (positive = up). |
| **placement.rotation** | `object` | Motor orientation (thrust vector direction). |
| **placement.rotation.x** | `deg` | Rotation around X-axis (roll, optional, default: 0). |
| **placement.rotation.y** | `deg` | Rotation around Y-axis (pitch, optional, default: 0). |
| **placement.rotation.z** | `deg` | Rotation around Z-axis (yaw, optional, default: 0). |

## Example Configuration

```yaml
motors:
  - tag: "main_motor"
    esc_ref: "main_esc"
    propeller_ref: "main_prop"
    manufacturer: "Emax"
    model: "RS2205"
    kv: 2300
    voltage_min: 11.1
    voltage_max: 14.8
    current_max: 25
    resistance: 0.08
    no_load_current: 0.5
    mass: 28
    diameter: 28
    length: 31
    shaft_diameter: 5
    shaft_length: 12
    mounting_screw: "M3"
    mounting_spacing: "16x16"
    placement:
      position:
        x: 0
        y: 0
        z: 0
      rotation:
        x: 0
        y: 0
        z: 0
  
  - tag: "pusher_motor"
    esc_ref: "pusher_esc"
    propeller_ref: "pusher_prop"
    manufacturer: "T-Motor"
    model: "F60 PRO IV"
    kv: 1750
    voltage_min: 14.8
    voltage_max: 22.2
    current_max: 40
    resistance: 0.045
    mass: 62
    diameter: 28
    length: 37.3
    placement:
      position:
        x: 1200
        y: 0
        z: 50
      rotation:
        x: 0
        y: 0
        z: 180  # Pusher configuration
```
