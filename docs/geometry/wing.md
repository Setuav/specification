# Wing Geometry

This section defines the parametric model for wings. The Wing model is versatile enough to represent main wings, horizontal stabilizers, and vertical stabilizers.

## Structure: Station-based Profiles

In this standard, a wing is defined by a series of **Stations (Profiles)** at specific spanwise positions. Each station defines the airfoil shape, chord, and orientation at that location.

1. **Station (Profile)**: Defines the 2D cross-section at a specific point along the span. It includes position, orientation, geometric properties (chord, airfoil), and rotations.

Stations are connected by lofting to create the 3D wing surface.

## Coordinate Frame and Placement

Each wing's stations are defined in a **wing-local coordinate system** where:

- **Origin**: Wing attachment point (leading edge of root)
- **X+**: Aft (toward trailing edge direction)
- **Y+**: Outboard (toward wing tip)
- **Z+**: Up (perpendicular to wing reference plane)

The entire wing is then positioned in the airframe using Wing Attachment parameters (see Wing Attachment section).

- **Root Offset**: Specified in Wing Attachment (position relative to fuselage nose)
- **Symmetry**: Wings are mirrored using the `mirror` parameter in Wing Attachment.

## Parameters

### Identification and Mass

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **tag** | `str` | Unique identifier for the wing (e.g., "main_wing", "v_tail_left"). |
| **mass** | `g` | Total wing mass for a single wing (optional). Note: if mirror is true in wing attachment, total mass will be 2 × mass. |

### Geometry

A wing geometry is defined by a list of stations (profiles). Each station fully specifies its position and orientation.

### Station Properties

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **position** | `object` | Station position (required). |
| **position.x** | `mm` | Longitudinal position in wing-local frame (typically 0 for leading edge with no sweep angle, positive = aft). |
| **position.y** | `mm` | Spanwise position from wing root (0 = root, increases toward tip). |
| **position.z** | `mm` | Vertical position from wing reference plane (0 = reference, positive = up). |
| **chord** | `mm` | Chord length at this station. |
| **airfoil** | `str\|obj` | Airfoil definition. Supports simple string format (e.g., `"naca2412"`) or detailed object format. See Airfoil Definition section for details. |
| **rotation** | `object` | Station rotation (optional). |
| **rotation.x** | `deg` | Rotation around X-axis (roll, optional, default: 0). |
| **rotation.y** | `deg` | Rotation around Y-axis (pitch/incidence/twist angle at this station, optional, default: 0). |
| **rotation.z** | `deg` | Rotation around Z-axis (yaw, optional, default: 0). |

### Airfoil Definition

Airfoils can be defined in two formats:

**1. Simple Format (String)**:
For backward compatibility and simplicity, NACA airfoils can be specified directly as strings:

```yaml
airfoil: "naca2412"
```

**2. Detailed Format (Object)**:
For greater flexibility and different source types, use the object format:

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **type** | `enum` | Airfoil type: `naca`, `file`, `coordinates`. |
| **code** | `str` | NACA code (required for `type: naca`). E.g., `"2412"`, `"0012"`. |
| **path** | `str` | DAT file path (required for `type: file`). Relative path from project root. |
| **points** | `array` | Coordinate array (required for `type: coordinates`). Normalized coordinates (0-1 range) in `[[x, y], ...]` format. |

**Examples**:

```yaml
# NACA airfoil
airfoil:
  type: "naca"
  code: "2412"

# DAT file
airfoil:
  type: "file"
  path: "profiles/custom_airfoil.dat"

# Coordinate table
airfoil:
  type: "coordinates"
  points: [[1.0, 0.0], [0.95, 0.012], [0.90, 0.018], ...]
```

### Surface Generation Parameters

These parameters control how adjacent profiles are blended to create the wing surface.

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| **ruled** | `bool` | `false` | `false`: Smooth approximated surface. `true`: Ruled surface (straight lines between profiles). |
| **max_degree** | `int` | `3` | Maximum polynomial degree for B-spline approximation. Valid range: `1-8`. Higher values allow smoother curves. |
| **continuity** | `enum` | `G2` | Target surface smoothness: `G0` (positional continuity), `G1` (tangent continuity), `G2` (curvature continuity). |

## Control Surfaces

Control surfaces are movable surfaces mapped to specific spanwise regions of the wing geometry. Ailerons, Flaps, Elevators, and similar surfaces are defined this way.

### Control Surface Parameters

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **tag** | `str` | Unique identifier for the control surface (e.g., "left_aileron", "flap"). |
| **type** | `enum` | Control surface type: `aileron`, `flap`, `elevator`, `rudder`. |
| **span_start** | `mm` | Spanwise position where the control surface starts (corresponds to position_y coordinate). |
| **span_end** | `mm` | Spanwise position where the control surface ends (corresponds to position_y coordinate). |
| **chord** | `mm` | Chord length of the control surface. Measured from trailing edge at each station. |

**Note**: The hinge line is implicitly defined at the control surface start (at `chord` mm distance from the trailing edge).

### Example Control Surface Definition

```yaml
control_surfaces:
  - tag: "left_aileron"
    type: "aileron"
    span_start: 500    # Starts at 500mm from root
    span_end: 800      # Ends at 800mm from root
    chord: 60          # 60mm chord length
  
  - tag: "flap"
    type: "flap"
    span_start: 100
    span_end: 450
    chord: 75
```

## Example Configuration

```yaml
tag: "main_wing"
mass: 180  # optional
type: "wing"
geometry:
  blending:
    ruled: false
    max_degree: 3
    continuity: "G2"
  
  profiles:
    - position:            # Root profile at leading edge
        x: 0
        y: 0
        z: 0
      chord: 240
      rotation:
        y: 2.0
      airfoil: "naca2412"  # Simple format
    
    - position:            # Mid-span profile
        x: 0
        y: 400
        z: 0
      chord: 240
      rotation:
        y: 2.0
      airfoil:              # Detailed format
        type: "naca"
        code: "2412"
    
    - position:            # Tip profile (swept and dihedral)
        x: 35
        y: 800
        z: 35
      chord: 180
      rotation:
        y: -1.0  # Washout
      airfoil:
        type: "naca"
        code: "0012"
  
  control_surfaces:
    - tag: "left_aileron"
      type: "aileron"
      span_start: 500
      span_end: 800
      chord: 60
    
    - tag: "flap"
      type: "flap"
      span_start: 100
      span_end: 450
      chord: 75
```
