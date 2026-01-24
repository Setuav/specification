# Fuselage Geometry

The Fuselage model defines the main body of the UAV. It typically uses a section-based approach where several cross-sections are defined along the X-axis and lofted together with parametric surfaces.

## Structure: Sections and Lofting

A fuselage is defined by a series of cross-sections (sections) at specific X-coordinates, which are lofted together using controlled interpolation. Each section includes its position, cross-section shape (profile), and orientation.

## Coordinate Frame

The fuselage sections are defined in the `SETUAV_BODY` frame.

- **X-axis**: Position along the fuselage (x=0 is nose tip).
- **Y-Z plane**: The plane of the cross-section.

## Parameters

The fuselage is defined by a series of **sections** (cross-sections) that are lofted together using controlled interpolation.

### Section Properties

Each section has the following properties:

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **position_x** | `mm` | Longitudinal position from the nose tip (required). |
| **position_y** | `mm` | Lateral offset from the XZ-plane (optional, default: 0). Fixed-wing UAVs typically use 0 (centerline). |
| **position_z** | `mm` | Vertical offset from the XY-plane (optional, default: 0). |
| **profile** | `object` | Cross-section shape definition (required). |
| **pitch** | `deg` | Section tilt relative to X-axis (optional, default: 0). |
| **roll** | `deg` | Profile rotation about X-axis (optional, default: 0). |

### Profile Types

#### Circle

Circular cross-section defined by diameter.

```yaml
profile:
  type: "circle"
  diameter: 80  # mm
```

#### Ellipse

Elliptical cross-section with independent width and height.

```yaml
profile:
  type: "ellipse"
  width: 100   # mm
  height: 120  # mm
```

#### Rectangle

Rectangular cross-section with optional rounded corners.

```yaml
profile:
  type: "rectangle"
  width: 100          # mm
  height: 120         # mm
  corner_radius: 10   # mm (optional, default: 0)
```

### Surface Blending Parameters

These parameters control how sections are blended to create the final surface.

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| **ruled** | `bool` | `false` | `false`: Smooth approximated surface. `true`: Ruled surface (straight lines between sections). |
| **max_degree** | `int` | `3` | Maximum polynomial degree for B-spline approximation. Valid range: `1-8`. Higher values allow smoother curves. |
| **continuity** | `enum` | `G2` | Target surface smoothness: `G0` (positional continuity), `G1` (tangent continuity), `G2` (curvature continuity). |

**Determinism Guarantee**: Given identical sections and blend parameters, all compliant implementations must produce surfaces with equivalent cross-sections at any given x position (within tolerance ±0.1%).

## Example Configuration

```yaml
tag: "main_fuselage"
type: "fuselage"
geometry:
  blending:
    ruled: false      # Smooth approximated surface
    max_degree: 3     # Cubic B-spline
  
  sections:
    - position_x: 0
      position_y: 0
      position_z: 0
      profile:
        type: "circle"  # Nose tip
        diameter: 1
    
    - position_x: 150
      position_y: 0
      position_z: 10     # Raised cockpit
      profile:
        type: "ellipse"
        width: 80
        height: 100
      pitch: 0.0
    
    - position_x: 600
      position_y: 0
      position_z: 0
      profile:
        type: "ellipse"
        width: 80
        height: 100
    
    - position_x: 1200
      position_y: 0
      position_z: 0
      profile:
        type: "circle"
        diameter: 20  # Tail boom
```
