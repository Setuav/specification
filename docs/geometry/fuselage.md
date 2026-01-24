# Fuselage Geometry

The Fuselage model defines the main body of the UAV. It typically uses a section-based approach where several cross-sections are defined along the X-axis and lofted together with parametric surfaces.

## Structure: Sections and Lofting

A fuselage is defined by a series of cross-sections (sections) at specific X-coordinates, which are lofted together using controlled interpolation. Each section includes its position, cross-section shape (profile), and orientation.

## Coordinate Frame

The fuselage sections are defined in the `SETUAV_BODY` frame.

- **X-axis**: Position along the fuselage (x=0 is nose tip).
- **Y-Z plane**: The plane of the cross-section.

## Parameters

### Identification and Mass

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **tag** | `str` | Unique identifier for the fuselage (e.g., "main_fuselage"). |
| **mass** | `g` | Total fuselage mass (optional). |

### Geometry

The fuselage geometry is defined by a series of **sections** (cross-sections) that are lofted together using controlled interpolation.

### Section Properties

Each section has the following properties:

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **position** | `object` | Section position (required). |
| **position.x** | `mm` | Longitudinal position from the nose tip. |
| **position.y** | `mm` | Lateral offset from the XZ-plane (optional, default: 0). Fixed-wing UAVs typically use 0 (centerline). |
| **position.z** | `mm` | Vertical offset from the XY-plane (optional, default: 0). |
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
mass: 250  # optional
type: "fuselage"
geometry:
  blending:
    ruled: false      # Smooth approximated surface
    max_degree: 3     # Cubic B-spline
  
  sections:
    - position:
        x: 0
        y: 0
        z: 0
      profile:
        type: "circle"  # Nose tip
        diameter: 1
    
    - position:
        x: 150
        y: 0
        z: 10     # Raised cockpit
      profile:
        type: "ellipse"
        width: 80
        height: 100
      pitch: 0.0
    
    - position:
        x: 600
        y: 0
        z: 0
      profile:
        type: "ellipse"
        width: 80
        height: 100
    
    - position:
        x: 1200
        y: 0
        z: 0
      profile:
        type: "circle"
        diameter: 20  # Tail boom
```
