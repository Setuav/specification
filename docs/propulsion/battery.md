# Battery

This section defines batteries used to power UAV propulsion and avionics systems. Battery electrical data is specified at **cell level** and combined with series/parallel topology.

## Overview

In the Setuav Standard, battery electrical properties are defined per cell, then pack behavior is derived from:

- `cells_series` (S)
- `cells_parallel` (P)

This avoids inconsistent pack-level voltage/capacity combinations.

## Parameters

### Identification

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **tag** | `str` | Unique identifier for the battery (e.g., `main_battery`). |
| **manufacturer** | `str` | Manufacturer name (optional). |
| **model** | `str` | Model designation (optional). |

### Cell-Level Electrical Characteristics

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **chemistry** | `enum` | Cell chemistry: `LiPo`, `LiHV`, `LiFe`, `Li-ion`, `NiMH`, `NiCd`. |
| **cells_series** | `int` | Number of cells in series (S). |
| **cells_parallel** | `int` | Number of cells in parallel (P). |
| **cell_voltage_nominal** | `V` | Nominal voltage per cell. |
| **cell_voltage_full** | `V` | Fully charged voltage per cell. |
| **cell_voltage_cutoff** | `V` | Minimum safe voltage per cell. |
| **cell_capacity** | `mAh` | Capacity per cell. |
| **cell_discharge_rate** | `C` | Continuous discharge rate per cell. |
| **cell_discharge_burst** | `C` | Burst discharge rate per cell (optional). |
| **cell_charge_rate** | `C` | Maximum charge rate per cell (optional, default: 1C). |
| **cell_resistance** | `mΩ` | Internal resistance per cell (optional). |

### Physical Properties

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **mass** | `g` | Battery pack mass. |
| **dimensions** | `object` | Physical pack dimensions. |
| **dimensions.length** | `mm` | Length. |
| **dimensions.width** | `mm` | Width. |
| **dimensions.height** | `mm` | Height/thickness. |

### Placement

Batteries are positioned in the airframe using the placement object:

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **placement** | `object` | Battery placement in airframe (optional). |
| **placement.position.x/y/z** | `mm` | Battery position in `SETUAV_BODY` frame. |
| **placement.rotation.x/y/z** | `deg` | Battery orientation (optional). |

## Derived Pack Values (Informative)

These are derived by analysis tools and should not be stored as primary battery fields:

- `pack_voltage_nominal = cells_series * cell_voltage_nominal`
- `pack_voltage_full = cells_series * cell_voltage_full`
- `pack_voltage_cutoff = cells_series * cell_voltage_cutoff`
- `pack_capacity = cells_parallel * cell_capacity`

## Example Configuration

```yaml
batteries:
  - tag: "main_battery"
    manufacturer: "Tattu"
    model: "R-Line LiHV"
    chemistry: "LiHV"
    cells_series: 4
    cells_parallel: 1
    cell_voltage_nominal: 3.8
    cell_voltage_full: 4.35
    cell_voltage_cutoff: 3.0
    cell_capacity: 1550
    cell_discharge_rate: 95
    cell_discharge_burst: 190
    cell_charge_rate: 5
    cell_resistance: 12
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
    model: "Graphene LiPo"
    chemistry: "LiPo"
    cells_series: 3
    cells_parallel: 1
    cell_voltage_nominal: 3.7
    cell_voltage_full: 4.2
    cell_voltage_cutoff: 3.0
    cell_capacity: 5000
    cell_discharge_rate: 45
    cell_discharge_burst: 90
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
