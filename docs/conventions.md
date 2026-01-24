# Conventions

This section defines the technical standards used throughout the Setuav Standard to ensures consistency across different implementations.

## Terminology: Normative vs Non-normative
- **Normative**: Mandatory rules that must be followed for a file to be considered compliant with the standard.
- **Non-normative**: Explanatory notes, examples, or implementation advice that provide context but are not strictly required.

## Coordinate System
Setuav uses a fixed-body coordinate frame (often referred to as `SETUAV_BODY` in documentation):

| Axis | Direction | Description |
| :--- | :--- | :--- |
| **Origin** | Nose Tip | The very front point of the fuselage (x=0, y=0, z=0). |
| **+X** | Aft | Increases from the nose tip toward the tail. |
| **+Y** | Right | Starboard side (right-hand rule). |
| **+Z** | Up | Increases vertically upward. |

**Mirroring**: By default, symmetry is assumed across the **XZ-plane** (Y = 0).

## Position and Rotation Structure

Throughout the standard, component positions and rotations are defined using a consistent nested structure:

```yaml
position:
  x: 0    # mm, position along X-axis
  y: 0    # mm, position along Y-axis
  z: 0    # mm, position along Z-axis

rotation:
  x: 0    # deg, rotation around X-axis (roll)
  y: 0    # deg, rotation around Y-axis (pitch)
  z: 0    # deg, rotation around Z-axis (yaw)
```

**Rotation Convention**: Rotations are specified as angles around each axis:

- **rotation.x** (roll): Rotation around the X-axis (longitudinal)
- **rotation.y** (pitch): Rotation around the Y-axis (lateral)
- **rotation.z** (yaw): Rotation around the Z-axis (vertical)

All rotations follow the right-hand rule.

## Units
To avoid ambiguity, all numeric values in a standard file must use the following units unless explicitly specified otherwise in the schema:

| Quantity | Unit | Symbol |
| :--- | :--- | :--- |
| Length | Millimeters | `mm` |
| Angle | Degrees | `deg` |
| Mass | Grams | `g` |
| Force | Newtons | `N` |
| Velocity | Meters per second | `m/s` |

## Modular Files and References
Projects can be split into multiple files for reusability.

- **Reference Property**: The key `ref` is used to point to an external file.
- **Path Resolution**: The path is always resolved **relative to the directory of the file containing the reference**.

Example:
```yaml
geometry:
  fuselage:
    ref: "./parts/fuselage_v1.yaml"
```
