# Wing Geometry

This section defines the parametric model for wings. The Wing model is versatile enough to represent main wings, horizontal stabilizers, and vertical stabilizers.

## Structure: Profiles and Sections
In this standard, a wing is not a single geometric block but a series of **Stations (Profiles)** connected by **Segments (Sections)**.

1.  **Station (Profile)**: Defines the 2D cross-section at a specific point along the span. It includes the **Airfoil**, **Chord**, and **Twist**.
2.  **Segment (Section)**: Defines the 3D geometry between two adjacent profiles. It includes the **Span**, **Sweep**, and **Dihedral**, which describe how the next profile is positioned relative to the current one.

## Coordinate Frame and Placement
Each wing's **Root Profile** is placed relative to the `SETUAV_BODY` frame origin (nose tip).

- **Root Offset (`x`, `y`, `z`)**: Position of the leading edge at the root chord.
- **Symmetry**: Wings are assumed to be mirrored across the XZ-plane ($Y=0$) unless specified otherwise.

## Parameters
A wing is defined by a list of sections. The first entry defines the **Root Profile**, and subsequent entries define segments leading to the next profile.

### Profile Properties (at each station)
| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **Chord** | `mm` | Chord length at the current station. |
| **Twist** | `deg` | Absolute incidence angle relative to the X-axis. |
| **Airfoil** | `ref` | Reference to an airfoil profile (NACA, DAT, or coordinate file). |

### Section Properties (the segment connecting to the next profile)
| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **Span** | `mm` | Spanwise distance (extension) of the segment. |
| **Sweep** | `deg` | Aft-ward angle of the quarter-chord line (25% chord) for this segment. |
| **Dihedral** | `deg` | Upward angle of the quarter-chord line for this segment. |

## Control Surfaces
Wings typically host control surfaces like Ailerons or Flaps, which are mapped to specific spanwise regions of the wing assembly.

## Example (Conceptual YAML)
```yaml
name: "Main Wing"
type: "wing"
geometry:
  root_offset: [500, 0, 0]
  mirror: true
  sections:
    - chord: 240
      twist: 2.0
      airfoil: "naca2412" # Root Profile
    - span: 400
      sweep: 0.0
      dihedral: 0.0
      chord: 240
      twist: 2.0
      airfoil: "naca2412" # Inner Section Tip
    - span: 400
      sweep: 5.0
      dihedral: 5.0
      chord: 180
      twist: -1.0
      airfoil: "naca0012" # Outer Section Tip (Outer Wing)
```
