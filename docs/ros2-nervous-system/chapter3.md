---
sidebar_position: 3
---

# Chapter 3: Humanoid URDF: Robot modeling

## Introduction to URDF

The Unified Robot Description Format (URDF) is an XML file format used in ROS to describe all aspects of a robot. It provides a standardized way to represent a robot's kinematic and dynamic properties, as well as its visual and collision characteristics. For humanoid robots, URDF is crucial for defining their complex structure, allowing for accurate simulation, motion planning, and visualization.

## Fundamental Elements of URDF

URDF models are built from two primary elements: **links** and **joints**.

### Links: The Robot's Rigid Bodies

**Definition**: A `link` represents a rigid body segment of the robot. This could be a torso, an upper arm, a hand, a foot, or any other physical part of the robot that does not deform. Each link has a mass, inertia, visual properties (how it looks), and collision properties (how it interacts with its environment).

**Key Attributes**:
-   **`name`**: Unique identifier for the link.
-   **`inertial`**: Defines the link's mass, center of mass, and inertia matrix.
-   **`visual`**: Describes the appearance of the link (e.g., geometry, material, color).
-   **`collision`**: Defines the geometric shape used for collision detection.

### Joints: Connecting Links

**Definition**: A `joint` connects two `link` elements, defining their relative motion. Each joint has a parent link and a child link. Joints are characterized by their type, which dictates the degrees of freedom (DOF) and how the child link can move relative to its parent.

**Key Attributes**:
-   **`name`**: Unique identifier for the joint.
-   **`type`**: Defines the joint's movement. Common types include:
    -   `revolute`: Rotational joint with a limited range (e.g., elbow).
    -   `continuous`: Rotational joint with unlimited range (e.g., wheel).
    -   `prismatic`: Linear joint with a limited range (e.g., piston).
    -   `fixed`: No movement, rigidly connects two links.
-   **`parent`**: Specifies the name of the parent link.
-   **`child`**: Specifies the name of the child link.
-   **`origin`**: Defines the pose (position and orientation) of the child link relative to the parent.
-   **`axis`**: For revolute and prismatic joints, specifies the axis of motion.

## Humanoid Robot Modeling in URDF

Modeling humanoid robots in URDF involves meticulously defining each body segment as a `link` and specifying how these links are connected via `joints`. The hierarchical structure, starting from a base link (often the torso or hips), branches out to define the limbs, head, and other appendages.

### Example: A Simple Humanoid Arm Segment

For a simplified URDF example of a humanoid arm, refer to:
[examples/ros2-nervous-system/urdf/simple_humanoid_arm.urdf](/examples/ros2-nervous-system/urdf/simple_humanoid_arm.urdf)

In this example:
-   `shoulder_link` and `upper_arm_link` are the rigid body segments.
-   `shoulder_joint` connects them as a `revolute` joint, allowing rotation around the Y-axis.
-   `origin` defines where the `upper_arm_link` starts relative to the `shoulder_link`.

![Simple Humanoid Arm URDF Visualization](/img/simple_humanoid_arm_urdf_visualization.png)
*Figure 3.1: Visualization of a simplified humanoid arm URDF model showing a shoulder and upper arm link connected by a revolute joint.*
(Note: An actual image of the URDF visualization would be embedded here.)

## Basic Kinematic Chains

A kinematic chain is a sequence of rigid bodies (links) connected by joints that form a system, allowing relative motion. In humanoid robots, understanding kinematic chains is crucial for:
-   **Forward Kinematics**: Calculating the position and orientation of an end-effector (e.g., a hand) given the joint angles.
-   **Inverse Kinematics**: Calculating the joint angles required to achieve a desired end-effector pose.

The hierarchical nature of URDF, where each `joint` defines a `parent` and `child` link, inherently describes these kinematic chains.

## Summary

This chapter provided an overview of URDF and its application in modeling humanoid robots. We explored the fundamental elements of links and joints, their attributes, and how they combine to form kinematic chains. Understanding URDF is crucial for simulating, visualizing, and controlling humanoid robots.

## Self-Assessment Questions

1.  What are the two primary elements of a URDF model, and what role does each play in describing a robot?
2.  Describe the purpose of the `inertial`, `visual`, and `collision` properties within a URDF `link` element.
3.  Imagine you need to model a robot's elbow that can only bend (rotate around one axis) and has a limited range of motion. Which URDF joint `type` would you use and why?
4.  Given a `shoulder_link` and an `upper_arm_link`, and assuming the `shoulder_link` is the parent, explain how the `origin` and `axis` attributes of the `shoulder_joint` determine the position and movement of the `upper_arm_link`.
5.  Why is the concept of a kinematic chain important when modeling humanoid robots with URDF?

## References
[1] The ROS 2 Project. (n.d.). *URDF Overview*. Retrieved from https://docs.ros.org/en/humble/Tutorials/Intermediate/URDF/URDF-Main.html
[2] Open Robotics. (n.d.). *URDF XML Schema*. Retrieved from https://docs.ros.org/en/humble/p/urdf/index.html