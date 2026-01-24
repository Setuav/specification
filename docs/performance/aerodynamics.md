# Aerodynamic Performance

This module contains numerical data defining the aerodynamic characteristics of the aircraft.

## Parameters

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **cl_max** | `-` | Maximum lift coefficient (stall condition). |
| **cl_max_alpha** | `deg` | Angle of attack where maximum lift is achieved. |
| **cd_min** | `-` | Minimum drag coefficient (typically at zero lift). |
| **ld_max** | `-` | Maximum lift-to-drag ratio. |
| **ld_max_alpha** | `deg` | Angle of attack where maximum L/D is achieved. |

## Reference Values

Reference values used for non-dimensionalizing coefficients:

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **span** | `mm` | Reference wingspan. |
| **area** | `mm²` | Reference wing area. |
| **mean_chord** | `mm` | Mean aerodynamic chord (MAC). |
| **reynolds_number** | `-` | Approximate Reynolds number used in the analysis. |

## Polars

The variation of aerodynamic coefficients with respect to angle of attack (alpha) is stored as arrays.

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **alphas** | `deg` | Array of angle of attack values. |
| **cl_values** | `-` | Lift coefficients (CL) at corresponding alphas. |
| **cd_values** | `-` | Drag coefficients (CD) at corresponding alphas. |
| **ld_values** | `-` | Lift-to-drag ratios (L/D) at corresponding alphas. |

## Example Configuration

```yaml
aerodynamics:
  cl_max: 1.45
  # ...
  polars:
    alphas: [-5, 0, 5, 10, 15]
    cl_values: [-0.2, 0.4, 0.9, 1.3, 1.45]
    cd_values: [0.03, 0.025, 0.04, 0.08, 0.15]
    ld_values: [-6.6, 16.0, 22.5, 16.25, 9.6]
```
