# RL rubbble remover robot with wheels and an arm

This project builds a cost-efficient autonomous robot that removes rubble using reinforcement learning (RL). The robot combines a wheeled base and a robotic arm, focusing on sim-to-real transfer.
The system is trained in simulation and deployed on a Raspberry Pi 5.

## Features

- ✅ RL-based decision making (Stable-Baselines3)
- ✅ Sim-to-real pipeline using MuJoCo
- ✅ Runs inference on Raspberry Pi 5
- ✅ Cost-efficient hardware design

## basic hardware
- raspberry pi 5
- raspberry pi camera modeule 3
- VL53L0X ToF distance sensor
- DC motors with wheels
- Robotic arm (mg966r and two sg90s)

## software
- python
- Mujoco
- stable-baseline3
- C++

## installation

## prerequisite
- Mujoco
- stable-baseline3

## goal
- detect rubble
- move toward thetarget
- stop at an appropriate distance
- grasp and remove the object

## future work
- dual-arm system
- improved RL policy
- more robust sim-to-real transfer
- better perception using vision models


