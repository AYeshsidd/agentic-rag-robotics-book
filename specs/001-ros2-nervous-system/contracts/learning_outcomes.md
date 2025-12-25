# Learning Outcomes Contracts: Module 1: The Robotic Nervous System (ROS 2)

This document outlines the expected learning outcomes and interaction patterns for students completing each chapter within Module 1. These serve as "contracts" between the educational content and the learner, defining the skills and knowledge gained.

## Chapter 1: ROS 2 Fundamentals - Learning Contract

**Title**: ROS 2 Fundamentals: Nodes, Topics, Services

-   **Expected Outcome**: Upon successful completion of this chapter, the student will be able to:
    -   Identify and define the core components of ROS 2: Nodes, Topics, Services, and Actions.
    -   Describe the purpose and communication patterns of each component (e.g., publish-subscribe for Topics, request-response for Services).
    -   Articulate the role of a "graph" in ROS 2 architecture and how these components interact within it.
-   **Student Interaction**:
    -   Read and comprehend conceptual explanations of ROS 2 middleware.
    -   Interpret architectural diagrams illustrating Nodes, Topics, and Services.
    -   Engage with self-assessment questions to test understanding of core concepts.
    -   Analyze basic example scenarios to see how these components are applied.

## Chapter 2: Python to ROS Integration - Learning Contract

**Title**: Python to ROS Integration: `rclpy` controllers

-   **Expected Outcome**: Upon successful completion of this chapter, the student will be able to:
    -   Conceptualize the process of creating a ROS 2 node using Python (`rclpy`).
    -   Understand how to publish data to a ROS 2 Topic from a Python script.
    -   Understand how to subscribe to a ROS 2 Topic from a Python script.
    -   Grasp the basic structure of a Python-based ROS 2 controller.
-   **Student Interaction**:
    -   Read and analyze provided `rclpy` code examples for publishing and subscribing.
    -   Examine the structure of a Python ROS 2 node, identifying key elements (`Node` class, timers, callbacks).
    -   Mentally trace the data flow in simple Python-based ROS 2 applications.
    -   Understand the role of message types in data exchange.

## Chapter 3: Humanoid URDF and Basic Control Flow - Learning Contract

**Title**: Humanoid URDF: Robot modeling

-   **Expected Outcome**: Upon successful completion of this chapter, the student will be able to:
    -   Interpret the fundamental elements of a Humanoid URDF file (links, joints, visual, collision, inertial).
    -   Relate the XML structure of URDF to the physical components of a humanoid robot model.
    -   Understand the concept of a kinematic chain as defined by joints and links in URDF.
    -   Grasp basic control flow principles related to commanding robot joints (e.g., publishing joint states).
-   **Student Interaction**:
    -   Read and analyze simplified Humanoid URDF code snippets.
    -   Examine visual representations of URDF models and mentally map them to their textual definitions.
    -   Understand how joint types (e.g., revolute, fixed) influence robot movement.
    -   Analyze conceptual examples of publishing joint commands to influence robot posture.
