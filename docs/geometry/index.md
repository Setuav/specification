# Geometry Overview

The geometry of a fixed-wing UAV in the Setuav Standard is defined through a set of independent but interconnected components. This modular approach allows for complex airframes to be built by combining wings, fuselages, and other structural elements.

## Core Concepts

The geometry system is designed with the following principles:

- **Parametric Definition**: Instead of storing static 3D meshes, we store the parameters required to generate them.
- **Station-Based Lofting**: Most components (wings and fuselages) are defined by cross-sections (stations) that are lofted together to create smooth surfaces.
- **Reference Frame Consistency**: All components are positioned relative to the `SETUAV_BODY` frame.

## Component Types

In the following sections, we will explore:

1. **[Fuselage](fuselage.md)**: Defining the main body using parametric cross-sections (sections) lofted along the longitudinal axis.
2. **[Wing](wing.md)**: Defining lifting surfaces, stabilizers, and control surfaces using a section-based approach with absolute positioning.
3. **[Wing Attachment](wing_attachment.md)**: Positioning and orienting wings on the fuselage, including automatic fairing generation for aerodynamic integration.

## Coordinate Integration

All components are positioned in the `SETUAV_BODY` reference frame (origin at nose tip, X+ aft, Y+ right, Z+ up). Wings use local coordinate systems that are then placed via Wing Attachment parameters (position_x, position_y, position_z, pitch_rotation, roll_rotation, yaw_rotation). This ensures the final model is a cohesive unit ready for aerodynamic and structural analysis.
