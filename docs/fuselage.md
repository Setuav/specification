# Fuselage Geometry

The Fuselage model defines the main body of the UAV. It typically uses a station-based approach where several cross-sections are defined along the X-axis and lofted together.

## Structure: Stations and Lofting
A fuselage is defined by a series of **Stations** located at specific X-coordinates.

1.  **Station**: A cross-section at a specific longitudinal position.
2.  **Cross-Section**: Can be defined as a simple shape (Circle, Square, Rounded Rectangle) or a complex parametric curve.

## Coordinate Frame
The fuselage stations are defined in the `SETUAV_BODY` frame.
- **X-axis**: Position along the fuselage (0 is nose tip).
- **Y-Z plane**: The plane of the cross-section.

## Parameters
Currently, the standard supports **Parametric Lofting** for the fuselage.

### Station Properties
| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **x** | `mm` | Distance from the nose tip. |
| **width** | `mm` | Maximum width (spanwise) at this station. |
| **height** | `mm` | Maximum height (vertical) at this station. |
| **shape** | `enum` | Type of cross-section (`circle`, `ellipse`, `rectangle`, `box`). |
| **offset_z**| `mm` | Vertical offset of the section center from the centerline. |

## Example (Conceptual YAML)
```yaml
name: "Main Fuselage"
type: "fuselage"
geometry:
  stations:
    - x: 0
      width: 0
      height: 0
      shape: "circle" # Nose tip
    - x: 150
      width: 80
      height: 100
      shape: "ellipse" # Cockpit area
    - x: 600
      width: 80
      height: 100
      shape: "ellipse" # Payload bay end
    - x: 1200
      width: 20
      height: 20
      shape: "circle" # Tail boom exit
```
