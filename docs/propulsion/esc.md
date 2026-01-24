# ESC (Electronic Speed Controller)

This section defines electronic speed controllers (ESCs) used to regulate motor speed in UAV propulsion systems. ESCs are specified by their electrical characteristics, communication protocols, and physical properties.

## Overview

ESCs in the Setuav Standard are defined independently and referenced by motors. The ESC definition includes electrical specifications, protocol support, and placement information needed for power system design and weight distribution.

## Parameters

### Identification

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **tag** | `str` | Unique identifier for the ESC (e.g., "main_esc", "pusher_esc"). |
| **manufacturer** | `str` | Manufacturer name (optional, e.g., "Hobbywing", "Castle Creations"). |
| **model** | `str` | Model designation (optional, e.g., "XRotor 40A", "Phoenix Edge 80"). |

### Electrical Characteristics

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **current_max** | `A` | Maximum continuous current rating. |
| **current_burst** | `A` | Maximum burst current (optional, typically 10-30 seconds). |
| **voltage_min** | `V` | Minimum operating voltage. |
| **voltage_max** | `V` | Maximum operating voltage. |
| **resistance** | `Ω` | Internal resistance (optional). |
| **bec_voltage** | `V` | Battery Eliminator Circuit output voltage (optional, 0 if no BEC). |
| **bec_current** | `A` | BEC maximum current output (optional). |

### Communication

| Parameter | Type | Description |
| :--- | :--- | :--- |
| **protocol** | `enum` | Control protocol (optional): `PWM`, `OneShot125`, `OneShot42`, `MultiShot`, `DShot150`, `DShot300`, `DShot600`, `DShot1200`. |
| **firmware** | `str` | Firmware type (optional, e.g., "BLHeli_S", "BLHeli_32", "AM32"). |
| **telemetry** | `bool` | Telemetry support (optional, default: false). |

### Physical Properties

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **mass** | `g` | ESC mass including wires. |
| **dimensions** | `object` | Physical dimensions (optional). |
| **dimensions.length** | `mm` | Length. |
| **dimensions.width** | `mm` | Width. |
| **dimensions.height** | `mm` | Height/thickness. |

### Placement

ESCs are positioned in the airframe using the placement object:

| Parameter | Unit | Description |
| :--- | :--- | :--- |
| **placement** | `object` | ESC placement in airframe (optional). |
| **placement.position** | `object` | ESC position in SETUAV_BODY frame. |
| **placement.position.x** | `mm` | Longitudinal position (distance from nose tip). |
| **placement.position.y** | `mm` | Lateral position (0 = centerline, positive = right). |
| **placement.position.z** | `mm` | Vertical position (positive = up). |
| **placement.rotation** | `object` | ESC orientation. |
| **placement.rotation.x** | `deg` | Rotation around X-axis (roll, optional, default: 0). |
| **placement.rotation.y** | `deg` | Rotation around Y-axis (pitch, optional, default: 0). |
| **placement.rotation.z** | `deg` | Rotation around Z-axis (yaw, optional, default: 0). |

## Example Configuration

```yaml
escs:
  - tag: "main_esc"
    manufacturer: "Hobbywing"
    model: "XRotor 40A"
    current_max: 40
    current_burst: 55
    voltage_min: 7.4
    voltage_max: 25.2
    resistance: 0.003
    bec_voltage: 5.0
    bec_current: 3.0
    protocol: "DShot600"
    firmware: "BLHeli_32"
    telemetry: true
    mass: 12
    dimensions:
      length: 45
      width: 25
      height: 8
    placement:
      position:
        x: 50
        y: 0
        z: -20
      rotation:
        x: 0
        y: 0
        z: 0
  
  - tag: "pusher_esc"
    manufacturer: "Castle Creations"
    model: "Phoenix Edge 80"
    current_max: 80
    current_burst: 100
    voltage_min: 11.1
    voltage_max: 25.2
    protocol: "PWM"
    firmware: "Castle_Link"
    telemetry: true
    mass: 28
    placement:
      position:
        x: 1150
        y: 0
        z: 30
      rotation:
        x: 0
        y: 0
        z: 0
```
