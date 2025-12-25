---
sidebar_position: 2
---

# Chapter 2: Python to ROS Integration: `rclpy` controllers

## Introduction to `rclpy`

`rclpy` is the Python client library for ROS 2, providing a clean and intuitive interface for Python developers to interact with the ROS 2 graph. It wraps the core C++ `rcl` (ROS Client Library) functionalities, allowing for the creation of nodes, publishers, subscribers, services, and actions entirely in Python. Leveraging `rclpy` enables rapid prototyping and development of robotic behaviors, particularly for AI agents and higher-level control logic.

## The `rclpy` Node

In `rclpy`, a node is typically implemented as a class that inherits from `rclpy.node.Node`. This class provides the fundamental functionalities for a ROS 2 node, such as initialization, cleanup, and access to communication primitives.

### Creating a Basic Node

For a minimal `rclpy` node structure, refer to:
[examples/ros2-nervous-system/python/minimal_publisher.py](/examples/ros2-nervous-system/python/minimal_publisher.py)
*Code Example 2.1: A minimal `rclpy` node structure.*

The `rclpy.init()` and `rclpy.spin()` functions are crucial. `rclpy.init()` initializes the ROS 2 client library, and `rclpy.spin()` keeps the node running, processing callbacks from timers, subscriptions, service calls, etc.

## `rclpy` Publishers: Sending Data

Publishers are used to send data asynchronously to topics. In `rclpy`, you create a publisher by calling the `create_publisher` method of your node.

### Implementing a Publisher Node

For an `rclpy` node publishing String messages to a topic, refer to:
[examples/ros2-nervous-system/python/simple_publisher.py](/examples/ros2-nervous-system/python/simple_publisher.py)
*Code Example 2.2: An `rclpy` node publishing String messages to a topic.*

This example demonstrates creating a publisher for `std_msgs.msg.String` messages on the `chatter` topic with a Quality of Service (QoS) depth of 10. A timer is used to trigger the `timer_callback` method every 0.5 seconds, where a new message is created and published.

## `rclpy` Subscribers: Receiving Data

Subscribers are used to receive data asynchronously from topics. You create a subscriber by calling the `create_subscription` method of your node.

### Implementing a Subscriber Node

For an `rclpy` node subscribing to String messages from a topic, refer to:
[examples/ros2-nervous-system/python/simple_subscriber.py](/examples/ros2-nervous-system/python/simple_subscriber.py)
*Code Example 2.3: An `rclpy` node subscribing to String messages from a topic.*

This subscriber node listens to the `chatter` topic. Whenever a new `String` message arrives, the `listener_callback` method is invoked, printing the received data.

## Implementing a Simple `rclpy` Controller

An `rclpy` controller often combines publishers and subscribers, along with logic to process incoming data and send out commands. Consider a simple controller that reads sensor data (via subscription) and sends motor commands (via publishing).

### Conceptual Controller Structure

For a conceptual structure of a basic `rclpy` robot controller, refer to:
[examples/ros2-nervous-system/python/basic_robot_controller.py](/examples/ros2-nervous-system/python/basic_robot_controller.py)
*Code Example 2.4: Conceptual structure of a basic `rclpy` robot controller.*

This example shows a controller that subscribes to `LaserScan` messages (simulated sensor data) and publishes `Twist` messages (velocity commands) to a robot. The `laser_callback` processes the sensor data and adjusts linear and angular speeds, which are then published.

This example shows a controller that subscribes to `LaserScan` messages (simulated sensor data) and publishes `Twist` messages (velocity commands) to a robot. The `laser_callback` processes the sensor data and adjusts linear and angular speeds, which are then published.

## Summary

This chapter provided a practical guide to integrating Python with ROS 2 using `rclpy`. We covered the creation of basic nodes, implementing publishers for sending data, subscribers for receiving data, and finally, outlined the structure of a simple Python-based robot controller that combines these communication primitives. This foundational knowledge is crucial for developing sophisticated robotic behaviors and AI agents.

## Self-Assessment Questions

1.  Explain the purpose of `rclpy.init()` and `rclpy.spin()` in the lifecycle of a Python ROS 2 node.
2.  How would you create an `rclpy` publisher for a custom message type, assuming the message definition exists?
3.  Describe the role of the `listener_callback` function in an `rclpy` subscriber node.
4.  In the conceptual `BasicRobotController` example, how could you modify the `laser_callback` to prioritize avoiding an obstacle over moving forward, even if the obstacle is far but directly in front?
5.  What are the key benefits of using `rclpy` for developing ROS 2 applications, especially for AI agents and high-level control?

## References
[1] The ROS 2 Project. (n.d.). *ROS 2 Documentation*. Retrieved from https://docs.ros.org/en/humble/index.html
[2] Open Robotics. (n.d.). *rclpy API Reference*. Retrieved from https://docs.ros.org/en/humble/p/rclpy/index.html