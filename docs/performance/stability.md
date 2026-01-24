# Stability

This module contains **numerical derivatives** and equilibrium points defining the static and dynamic stability characteristics of the aircraft.

## Longitudinal Stability

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **neutral_point_x** | `mm` | Position of the neutral point (aerodynamic center) from the nose. |
| **static_margin** | `%` | Static margin ((X_np - X_cg) / MAC). Positive values indicate stability, negative values indicate instability. |
| **trim_alpha** | `deg` | Angle of attack at equilibrium (pitch moment = 0). |
| **trim_elevator** | `deg` | Elevator angle at equilibrium. |

## Stability Derivatives

These coefficients determine the vehicle's response to disturbances (changes in alpha or beta angles).

| Derivative | Definition | Meaning | Desired Sign |
| :--- | :--- | :--- | :--- |
| **cm_alpha** | `dCm/dα` | Change in pitching moment with alpha. (Pitch stiffness) | Negative (< 0) |
| **cn_beta** | `dCn/dβ` | Change in yawing moment with beta. (Directional stability - Weathercock) | Positive (> 0) |
| **cl_beta** | `dCl/dβ` | Change in rolling moment with beta. (Dihedral effect) | Negative (< 0) |

## Example Configuration

```yaml
stability:
  static_margin: 15.5
  neutral_point_x: 650.0
  derivatives:
    cm_alpha: -0.85
    cn_beta: 0.12
    cl_beta: -0.05
```
