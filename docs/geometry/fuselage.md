# Fuselage Geometry

The Fuselage model defines the main structural bodies of the UAV. A fuselage is defined as one or more "segments," each consisting of a series of cross-sections connected together.

## Structure: Segments and Lofts

The fuselage structure is modular. Multiple "Segments" can be defined under a single fuselage definition. For instance, a fuselage might consist of three separate segments: "Nose Cone", "Main Tube", and "Motor Tower".

Each segment contains a series of cross-sections defined along the X-axis (or any direction in space), which are connected via controlled interpolation (lofting).

## Coordinate Frame

Fuselage segments and sections are defined in the `SETUAV_BODY` frame.

- **X-axis**: Longitudinal axis.
- **Y-Z plane**: The plane of the cross-section.

## Parameters

### Identification and Mass

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **tag** | `str` | Unique identifier for the fuselage (e.g., "main_fuselage"). |
| **mass** | `g` | Total fuselage mass. |

### Geometry: Segments

The fuselage geometry is the sum of parts defined under the `segments` array. Each segment has the following properties:

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **tag** | `str` | Segment-specific tag (e.g., "nose_cone"). |
| **sections** | `list` | List of cross-sections forming the segment (min 2). |
| **blending** | `object` | Surface generation parameters specific to this segment (optional). |

### Section Properties

Each section has the following properties:

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **position** | `object` | Section position (required). |
| **position.x** | `mm` | Longitudinal position from the nose. |
| **position.y** | `mm` | Lateral offset from the XZ-plane (optional, default: 0). |
| **position.z** | `mm` | Vertical offset from the XY-plane (optional, default: 0). |
| **profile** | `object` | Cross-section shape definition (required). |
| **rotation** | `object` | Section properties (optional). |
| **rotation.x** | `deg` | Rotation around X-axis (roll, optional, default: 0). |
| **rotation.y** | `deg` | Rotation around Y-axis (pitch, optional, default: 0). |
| **rotation.z** | `deg` | Rotation around Z-axis (yaw, optional, default: 0). |

## Profile Types

Each section under `sections` must have a specific profile.

#### Circle
```yaml
profile: {type: "circle", diameter: 80}
```

#### Ellipse
```yaml
profile: {type: "ellipse", width: 100, height: 120}
```

#### Rectangle
```yaml
# Can be rounded with optional 'corner_radius'
profile: {type: "rectangle", width: 100, height: 120, corner_radius: 10}
```

## Surface Blending

These parameters control how sections within a segment are connected.

| Parameter | Default | Description |
| :--- | :--- | :--- |
| **ruled** | `false` | If `true`, connects sections with straight lines (ruled surface). |
| **max_degree** | `3` | Degree of the B-spline surface (1-8). |
| **continuity** | `G2` | Surface continuity target: `G0`, `G1`, `G2`. |

## Example Configuration

This example defines a Skywalker-style fuselage in two segments: Main tube and motor tower.

```yaml
tag: "skywalker_X8"
mass: 450
type: "fuselage"
geometry:
  segments:
    # Segment 1: Main Fuselage Line
    - tag: "main_body"
      blending: {ruled: false}
      sections:
        - {position: {x: 0}, profile: {type: "circle", diameter: 5}}  # Pointy nose
        - {position: {x: 200}, profile: {type: "ellipse", width: 150, height: 90}} # Wide body
        - {position: {x: 800}, profile: {type: "circle", diameter: 20}} # Thin tail

    # Segment 2: Motor Tower (Extends from top of fuselage)
    - tag: "motor_tower"
      blending: {ruled: true}
      sections:
        - {position: {x: 600, z: 50}, profile: {type: "ellipse", width: 40, height: 80}} # Tower base
        - {position: {x: 650, z: 120}, profile: {type: "circle", diameter: 40}} # Firewall
```
