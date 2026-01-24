# Mass and Additional Parts

This section defines how to specify mass information for UAV components and track additional parts that are not captured in the geometry or propulsion systems.

## Overview

The Setuav Standard uses a simple approach for mass management:

- **Geometry Components**: Fuselage and wings can have an optional `mass` parameter (in grams)
- **Propulsion Components**: Motors, ESCs, propellers, and batteries all include `mass` parameters
- **Additional Parts**: Components outside geometry and propulsion (electronics, landing gear, etc.) are specified separately with mass and placement

## Geometry Mass

Geometry components (Fuselage, Wing) can specify mass directly:

```yaml
airframe:
  fuselage:
    tag: "main_fuselage"
    mass: 250  # grams (optional)
    geometry:
      sections: ...
  
  wings:
    - tag: "main_wing"
      mass: 180  # grams per wing (optional)
      geometry:
        profiles: ...
```

**Note**: If a wing has `mirror: true` in its attachment, the total wing mass contribution will be 2 × mass.

## Additional Parts

Parts not represented in geometry or propulsion systems are specified as additional parts:

```yaml
additional_parts:
  - tag: "landing_gear"
    description: "Carbon fiber landing gear assembly"
    mass: 120  # grams
    placement:  # optional, for CG calculation
      position: {x: 500, y: 0, z: -50}
```

### Additional Part Parameters

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **tag** | `str` | Unique part identifier. |
| **description** | `str` | Human-readable part description (optional). |
| **mass** | `g` | Part mass. |
| **placement** | `object` | Part placement in SETUAV_BODY frame (optional). |
| **placement.position** | `object` | Position: {x, y, z} in mm. |

## Example Configuration

```yaml
setuav: '1.0'

airframe:
  fuselage:
    tag: "main_fuselage"
    mass: 250
    geometry:
      sections: ...
  
  wings:
    - tag: "main_wing"
      mass: 180
      geometry:
        profiles: ...

propulsion:
  motors:
    - tag: "main_motor"
      mass: 28
      # ... other motor parameters
  
  batteries:
    - tag: "main_battery"
      mass: 185
      # ... other battery parameters

additional_parts:
  - tag: "motor_mount"
    description: "3D printed motor mount"
    mass: 12
    placement:
      position: {x: 0, y: 0, z: 0}
      
  - tag: "landing_gear"
    description: "Carbon fiber landing gear assembly"
    mass: 120
    placement:
      position: {x: 500, y: 0, z: -50}
      
  - tag: "electronics_bay"
    description: "Flight controller, receiver, GPS, wiring"
    mass: 85
    placement:
      position: {x: 400, y: 0, z: -10}
```

## Center of Gravity Calculation

With placement information for all components, the overall center of gravity can be computed:

$$
\vec{r}_{\text{CG}} = \frac{\sum_{i} m_i \cdot \vec{r}_i}{\sum_{i} m_i}
$$

Where:

- $m_i$ is the mass of component $i$
- $\vec{r}_i$ is the position vector of component $i$ in SETUAV_BODY frame

**Components contributing to CG:**

- Fuselage (if mass specified)
- Wings (position from wing attachment, mass × 2 if mirrored)
- Motors (from placement)
- ESCs (from placement)
- Batteries (from placement)
- Additional parts (from placement)
- Propellers (mounted on motors, use motor position)

This calculation should be performed by analysis tools, not stored in the specification.
