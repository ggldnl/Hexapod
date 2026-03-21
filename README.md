# The Hexapod Project

## ⚠️ Work in Progress

This project is actively under development.

## 🦾 Introduction

This repository documents a fully open-source six-legged robotic platform, intended as an end-to-end reference for the design, construction, and control of a hexapod robot, including mechanics, electronics, control software, kinematics, and gait generation.

While many individual resources exist, they are often fragmented or rely on closed components. A representative example is the [Make Your Pet hexapod robot](https://www.makeyourpet.com/), which is very good, with a huge and active community, but depends on a proprietary application for inverse kinematics and gait generation. This project explicitly avoids that approach: everything is implemented in the open and thoroughly documented.

The software stack is split into two layers:
- A high-level controller running on a Raspberry Pi, responsible for computationally intensive tasks (such as body and leg inverse kinematics, gait planning, ...).
- A low-level firmware running on a Servo2040, responsible for near-real-time tasks (such as servo command execution).

The controller plans motion and behavior, then transmits low-level commands to the Servo2040 for execution. The current version relies on simple position-controlled servos. A more advanced variant will support current-controlled actuators, enabling joint torque estimation via current feedback and allowing more sophisticated control strategies.

## 🔧 Repositories

The project is split into several repositories. Each repository focuses on a specific aspect of the robot.

- **[Hexapod-Controller](https://github.com/ggldnl/Hexapod-Controller)** is the high-level software stack running on the Raspberry Pi. It manages the full robot lifecycle — startup, idle, walking and shutdown — and lets you command body pose, individual leg positions, which gait is used, and locomotion velocity. Setup instructions for deploying the controller in a Python environment are included.

- **[Hexapod-Firmware](https://github.com/ggldnl/Hexapod-Firmware)** is the low-level firmware for the Servo2040. It manages near-real-time servo execution and communicates with the Controller over a custom HDLC-like serial protocol, documented in detail within the repository.

- **[Hexapod-Simulation](https://github.com/ggldnl/Hexapod-Simulation)** provides two environments for testing the robot without hardware: a PyBullet physics simulation and a viser-based 3D visualizer for inspecting kinematics and motion interactively.

- **[Hexapod-Hardware](https://github.com/ggldnl/Hexapod-Hardware)** contains everything needed to physically build the robot, including 3D-printable body parts, a full bill of materials, and step-by-step assembly instructions.

- **[Hexapod-PCB](https://github.com/ggldnl/Hexapod-PCB)** provides the design files for an optional custom PCB that simplifies wiring and makes the final assembly significantly cleaner.

A viewer is accessible [here](https://ggldnl.github.io/projects/hexapod_dashboard/dashboard/index.html). This will let you interact with the robot and see it perform a basic standup animation.

While the Hexapod-Controller gives you Python-level APIs, two ROS2 nodes are also available for those working in a ROS2 ecosystem:

- **[Hexapod-ROS-Python](https://github.com/ggldnl/Hexapod-ROS-Python)** wraps the Python controller as a ROS2 node, exposing the robot's functionality through a set of topics, actions, and services.

- **[Hexapod-ROS-CPP](https://github.com/ggldnl/Hexapod-ROS-CPP)** is a ground-up C++ reimplementation of the full stack as a ROS2 node (Hexapod-Controller + Hexapod-ROS-Python). By avoiding the Python runtime entirely, it should to offer significantly lower latency and higher control-loop throughput.

## 🤝 Contribution

Feel free to contribute by opening issues or submitting pull requests. 
Give a ⭐️ to this project if you liked the content.
