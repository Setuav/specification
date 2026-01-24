# Battery

This section defines batteries used to power UAV propulsion and avionics systems. Batteries are specified by their electrical characteristics, chemistry type, and physical properties.

## Overview

Batteries in the Setuav Standard are defined independently with their electrical specifications and placement information. The battery definition includes capacity, voltage characteristics, discharge capabilities, and physical properties needed for power system design and weight distribution.

## Parameters

### Identification

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **tag** | `str` | Unique identifier for the battery (e.g., "main_battery", "aux_battery"). |
| **manufacturer** | `str` | Manufacturer name (optional, e.g., "Tattu", "Turnigy", "GensAce"). |
| **model** | `str` | Model designation (optional, e.g., "R-Line 4S 1550mAh", "Graphene 3S 5000mAh"). |

### Electrical Characteristics

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **chemistry** | `enum` | Battery chemistry: `LiPo`, `LiHV`, `LiFe`, `Li-ion`, `NiMH`, `NiCd`. |
| **cells** | `int` | Number of cells in series (e.g., 3 for 3S, 4 for 4S). |
| **voltage_nominal** | `V` | Nominal voltage (typically cells × 3.7V for LiPo, cells × 3.8V for LiHV). |
| **voltage_full** | `V` | Fully charged voltage (typically cells × 4.2V for LiPo, cells × 4.35V for LiHV). |
| **voltage_cutoff** | `V` | Minimum safe discharge voltage (typically cells × 3.0V for LiPo). |
| **capacity** | `mAh` | Battery capacity in milliamp-hours. |
| **discharge_rate** | `C` | Maximum continuous discharge rate (e.g., 75 for 75C). |
| **discharge_burst** | `C` | Maximum burst discharge rate (optional, typically 10-30 seconds). |
| **charge_rate** | `C` | Maximum charge rate (optional, default: 1C). |
| **resistance** | `mΩ` | Internal resistance (optional). |

### Physical Properties

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **mass** | `g` | Battery mass. |
| **dimensions** | `object` | Physical dimensions. |
| **dimensions.length** | `mm` | Length. |
| **dimensions.width** | `mm` | Width. |
| **dimensions.height** | `mm` | Height/thickness. |

### Placement

Batteries are positioned in the airframe using the placement object:

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **placement** | `object` | Battery placement in airframe (optional). |
| **placement.position** | `object` | Battery position in SETUAV_BODY frame. |
| **placement.position.x** | `mm` | Longitudinal position (distance from nose tip). |
| **placement.position.y** | `mm` | Lateral position (0 = centerline, positive = right). |
| **placement.position.z** | `mm` | Vertical position (positive = up). |
| **placement.rotation** | `object` | Battery orientation. |
| **placement.rotation.x** | `deg` | Rotation around X-axis (roll, optional, default: 0). |
| **placement.rotation.y** | `deg` | Rotation around Y-axis (pitch, optional, default: 0). |
| **placement.rotation.z** | `deg` | Rotation around Z-axis (yaw, optional, default: 0). |

## Example Configuration

```yaml
batteries:
  - tag: "main_battery"
    manufacturer: "Tattu"
    model: "R-Line 4S 1550mAh"
    chemistry: "LiHV"
    cells: 4
    voltage_nominal: 15.2
    voltage_full: 17.4
    voltage_cutoff: 12.0
    capacity: 1550
    discharge_rate: 95
    discharge_burst: 190
    charge_rate: 5
    resistance: 12
    mass: 185
    dimensions:
      length: 78
      width: 36
      height: 36
    placement:
      position:
        x: 350
        y: 0
        z: -15
      rotation:
        x: 0
        y: 0
        z: 0
  
  - tag: "long_range_battery"
    manufacturer: "Turnigy"
    model: "Graphene 3S 5000mAh"
    chemistry: "LiPo"
    cells: 3
    voltage_nominal: 11.1
    voltage_full: 12.6
    voltage_cutoff: 9.0
    capacity: 5000
    discharge_rate: 45
    discharge_burst: 90
    mass: 382
    dimensions:
      length: 138
      width: 43
      height: 29
    placement:
      position:
        x: 420
        y: 0
        z: -25
      rotation:
        x: 0
        y: 0
        z: 0
```
