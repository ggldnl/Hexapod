# The Hexapod Project

## ⚠️ Work in Progress

This project is actively under development.

## 🦾 Introduction

This repository documents a fully open-source six-legged robotic platform, intended as an end-to-end reference for the design, construction, and control of a hexapod robot, including mechanics, electronics, control software, kinematics, and gait generation.

While many individual resources exist, they are often fragmented or rely on closed components. A representative example is the [Make Your Pet hexapod robot](https://www.makeyourpet.com/), which is very good, with a huge and active community, but depends on a proprietary application for inverse kinematics and gait generation. This project explicitly avoids that approach: everything is implemented in the open and thoroughly documented.

The software stack is split into two layers:
- A high-level controller running on a Raspberry Pi, responsible for computationally intensive tasks (such as body and leg inverse kinematics, gait planning, trajectory generation, ...).
- A low-level firmware running on a Servo2040, responsible for near-real-time tasks (such as servo command execution).

The controller plans motion and behavior, then transmits low-level commands to the Servo2040 for execution. The current version relies on simple position-controlled servos. A more advanced variant will support current-controlled actuators, enabling joint torque estimation via current feedback and allowing more sophisticated control strategies.

## 🔧 Repositories

The project is split into several repositories. Each repository focuses on a specific aspect of the robot:

1. **[Hexapod-Controller](https://github.com/ggldnl/Hexapod-Controller)**
   - Contains the software for the controller, intended to run on a Raspberry Pi.
   - Instructions on how to setup a software environment and deploy the controller.

2. **[Hexapod-Dashboard](https://github.com/ggldnl/Hexapod-Dashboard)**
   - Three.js dashboard to interface with the robot.

3. **[Hexapod-Firmware](https://github.com/ggldnl/Hexapod-Firmware)**
   - Contains the software for the Servo2040 firmware.
   - Handles low-level servo control and communication with the Controller.
   - Details on the HDLC-like protocol I used for the two boards to talk to each other.

4. **[Hexapod-Simulation](https://github.com/ggldnl/Hexapod-Simulation)**
   - Implements a simulation environment using PyBullet where to test the robot.

5. **[Hexapod-Hardware](https://github.com/ggldnl/Hexapod-Hardware)**
   - Includes 3D-printable files for constructing the hexapod body.
   - Contains a Bill of Materials and assembly instructions.

6. **[Hexapod-PCB](https://github.com/ggldnl/Hexapod-PCB)**
   - Files necessary to order an optional PCB that will make assembly easier and cleaner.

A viewer is accessible [here](https://ggldnl.github.io/projects/hexapod_dashboard/dashboard/index.html) without the need to instasll anything. This will let you interact with the robot and see it perform some basic animations. With the dashboard you will instead be able to connect to your robot and check its state real time (joint values, servo voltage, current draw, ...).

## 🤝 Contribution

Feel free to contribute by opening issues or submitting pull requests. 
Give a ⭐️ to this project if you liked the content.
