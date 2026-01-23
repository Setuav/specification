# Propulsion System

This section defines the propulsion components, including motors, propellers, and electronic speed controllers (ESCs).

## Model Overview
The propulsion system is defined by a combination of physical specifications and performance maps.

## Motor
Motors are defined by their physical constants and performance data.

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **KV** | `RPM/V` | Motor velocity constant. |
| **Mass** | `g` | Weight of the motor. |
| **Internal Resistance** | `ohms` | Phase-to-phase resistance. |
| **No-Load Current** | `A` | Current at zero torque (at specified voltage). |

## Propeller
Propellers are referenced from a library or defined by their geometry and performance coefficients ($C_T$, $C_P$).

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **Diameter** | `inch` | Propeller diameter. |
| **Pitch** | `inch` | Propeller pitch. |
| **Blades** | `int` | Number of blades. |

## Battery
| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **Cells** | `S` | Number of cells in series. |
| **Capacity** | `mAh` | Total capacity. |
| **Voltage** | `V` | Nominal voltage. |

## Example (Conceptual YAML)
```yaml
propulsion:
  motor:
    name: "T-Motor AT2814"
    kv: 900
    mass: 105
  propeller:
    name: "APC 12x6E"
    diameter: 12.0
    pitch: 6.0
  battery:
    cells: 4
    capacity: 5000
```
