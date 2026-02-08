# Propulsion Overview

The propulsion system of a fixed-wing UAV in the Setuav Standard defines the components responsible for generating thrust and providing electrical power. This includes motors, electronic speed controllers (ESCs), propellers, and batteries.

## Core Concepts

The propulsion system is designed with the following principles:

- **Component-Based Definition**: Each propulsion component (motor, ESC, propeller, battery) is defined independently with its technical specifications.
- **Performance Data**: Components include performance characteristics such as thrust curves, efficiency maps, and power consumption.
- **Integration Ready**: All components include mounting specifications and electrical requirements for seamless integration into the airframe.

## Component Types

The propulsion system includes the following component categories:

1. **Motor**: Brushless DC motors with specifications including KV rating, maximum current, resistance, and efficiency data.
2. **ESC (Electronic Speed Controller)**: Electronic controllers that regulate motor speed, including current limits, voltage range, and protocol support.
3. **Propeller**: Fixed-pitch propellers defined by diameter, pitch, and performance data (thrust and torque curves).
4. **Battery**: Battery packs defined from cell-level electrical properties and S/P topology (`cells_series`, `cells_parallel`), plus physical pack data.

## System Integration

Propulsion components are integrated into the UAV design through:

- **Positioning**: Motors are positioned in the airframe using the `SETUAV_BODY` coordinate system (position_x, position_y, position_z).
- **Orientation**: Motor thrust vectors are defined using orientation parameters (pitch_rotation, roll_rotation, yaw_rotation).
- **Power System**: Battery placement and wiring specifications ensure proper weight distribution and electrical connectivity.
- **Performance Analysis**: Combined propulsion data enables thrust-to-weight calculations, endurance estimates, and mission planning.

## Units and Standards

All propulsion specifications use SI units:

- Power: Watts (W)
- Current: Amperes (A)
- Voltage: Volts (V)
- Mass: grams (g) or kilograms (kg)
- Thrust: Newtons (N)
- Speed: RPM (revolutions per minute)
- Capacity: milliamp-hours (mAh), defined per cell (`cell_capacity`)
