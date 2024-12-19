# The Hexapod Project 🤖

## ⚠️ Work in Progress

This project is actively under development. Features are being added, refined, and tested continuously.

---

## 🦾 Introduction

The Hexapod Robot Project aims to create a completely open source six-legged robotic platform. I've always been fascinated by this kind of robots and I wanted to explore and experiment with a hexapod but I found that, even with a lot of resources available out there, I could not find a comprehensive guide from start to finish that showed how to deal with the electronics, code, the underlying mathematical model and so on. A great example is [Make Your Pet](https://www.makeyourpet.com/)'s hexapod robot (from which I took inspiration) which is very good, with a huge community, but with a closed source app that handles the inverse kinematics and the gait generation strategies. This project is my effort to democratize what I learned.

- **Software**: The software consists of two parts: a Controller and an Operator. The Controller does the heavy lifting, computing the inverse kinematics for each leg and the body, generating gait sequences, running machine learning/reinforcement learning models and so on; the commands required to set the computed joint values are then sent to the Operator for execution. 
- **Hardware**: I used a Raspberry Pi as Controller and a Servo2040 board as Operator. Other boards can potentially be used with proper adjustments to the code and configuration.

---

## 🔧 Repositories

The project is split into several repositories. Each repository focuses on a specific aspect of the robot:

1. **[Hexapod-Controller](https://github.com/ggldnl/Hexapod-Controller)**
   - Contains the software for Controller and everything related to it.
   - Responsible for high-level computations such as inverse kinematics and machine learning/reinforcement learning models execution.

2. **[Hexapod-Operator](https://github.com/ggldnl/Hexapod-Operator)**
   - Contains the software for the Operator and everything related to it.
   - Handles low-level servo control and communication with the Controller.
   - Contains details on the communication protocol I developed for the two boards to talk.

3. **[Hexapod-Simulation](https://github.com/ggldnl/Hexapod-Simulation)**
   - Implements a simulation environment using PyBullet.
   - Useful for testing gaits without requiring on the actual robot.

4. **[Hexapod-Hardware](https://github.com/ggldnl/Hexapod-Hardware)**
   - Includes 3D-printable files for constructing the hexapod body (and the link to the MakerWorld model page for print profiles).
   - Contains a Bill of Materials and assembly guides.

---

## 🎯 Goals

- Experiment with my robot and annotate everything I do.
- Offering detailed guides for replicating the project.
- Providing accessible resources for everyone to build their own hexapod robots.

---

## Contribution

Feel free to contribute by opening issues or submitting pull requests. 