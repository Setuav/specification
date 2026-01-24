# Setuav Standard — Introduction

## Purpose

The Setuav Standard defines a tool-agnostic format for describing UAV designs.

This repository contains only:

- the standard text,
- JSON Schemas,
- YAML examples,
- validation guidance.

Plugin APIs and any application-specific details are out of scope for this repository.

## Scope

The Setuav Standard targets **fixed-wing UAV** designs and provides a comprehensive data model covering the entire design lifecycle:

- **Geometry**: Parametric definition of airframe components including fuselage, wings, tails, and control surfaces.
- **Propulsion**: Specifications for propulsion systems (motors, ESCs, propellers) and power systems (batteries).
- **Mass**: Direct mass specifications for geometry and propulsion components, plus tracking of additional parts (electronics, landing gear, etc.).
- **Performance**: Standardized format for storing flight performance analysis, stability results, and mission simulation data.

## Out of scope

To maintain focus on the design definition, the following areas are out of scope:

- **Rotorcraft**: Multirotor and helicopter configurations, and their specific parameters (rotor disks, collective/cyclic pitch, etc.).
- **Avionics Internal Logic**: Detailed control laws, PID gains, or specific autopilot firmware code.
- **Detailed Structural Analysis**: Raw FEA mesh data or internal stress/strain tensors (the standard focuses on high-level material properties and mass distribution).
- **Operational Data**: Maintenance logs, flight logs, operator licensing, and real-time mission telemetry.

## Key Principles

The standard is designed around several key principles:

- **Modularity**: Large designs can be split into smaller, reusable component files.
- **Human-Readable**: YAML format ensures that the data is easy to read and edit by humans.
- **Strict Validation**: JSON Schemas provide clear rules for data structure and types.
