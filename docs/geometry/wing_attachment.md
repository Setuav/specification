# Wing Attachment

This section defines how wings are attached to the fuselage, including their position, orientation, and symmetry.

## Overview

A **Wing Attachment** combines the wing geometry with its placement in the airframe. It specifies where the wing root connects to the fuselage and how it is oriented.

## Coordinate System

All attachment coordinates are relative to the `SETUAV_BODY` frame (origin at fuselage nose tip):

- **X+**: Aft (toward tail)
- **Y+**: Right (starboard)
- **Z+**: Up

## Attachment Parameters

### Position

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **position** | `object` | Wing attachment position (required). |
| **position.x** | `mm` | Longitudinal position along fuselage (distance from nose tip). |
| **position.y** | `mm` | Lateral offset from centerline. Typically non-zero for V-tail or asymmetric configurations. |
| **position.z** | `mm` | Vertical offset from fuselage reference line. Positive values raise the wing. |

### Orientation

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **rotation** | `object` | Wing attachment rotation (optional). |
| **rotation.x** | `deg` | Rotation around X-axis (longitudinal axis, roll). Used for dihedral angle or V-tail configurations. Positive rotation tilts the right wing upward (optional, default: 0). |
| **rotation.y** | `deg` | Rotation around Y-axis (lateral axis, pitch). Adjusts wing incidence angle (optional, default: 0). |
| **rotation.z** | `deg` | Rotation around Z-axis (vertical axis, yaw). Creates a global sweep effect for the entire wing (optional, default: 0). |

### Symmetry

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **mirror** | `bool` | If `true`, the wing is mirrored across the XZ-plane (Y=0) to create a symmetric pair. If `false`, only a single wing is placed. |

## Example Configuration

```yaml
wings:
  - tag: "main_wing"
    attachment:
      position:
        x: 450    # 450mm from nose
        y: 0      # Centerline
        z: 50     # 50mm above reference
      rotation:
        x: 2.0    # 2° dihedral
        y: 0      # No incidence offset
        z: 0      # No global sweep
      mirror: true       # Symmetric pair

    geometry:
      blending:
        ruled: false
        max_degree: 3
        continuity: "G2"
      profiles:
        - position:
            x: 0
            y: 0
            z: 0
          chord: 240
          rotation:
            y: 2.0
          airfoil: "naca2412"
        # Additional profiles...

  - tag: "horizontal_stabilizer"
    attachment:
      position:
        x: 1200   # Near tail
        y: 0
        z: 120
      rotation:
        x: 0
        y: 0
        z: 0
      mirror: true       # Symmetric pair

    geometry:
      blending:
        ruled: false
        max_degree: 3
        continuity: "G2"
      profiles:
        - position:
            x: 0
            y: 0
            z: 0
          chord: 150
          rotation:
            y: 0
          airfoil: "naca0012"
        # Additional profiles...
```
