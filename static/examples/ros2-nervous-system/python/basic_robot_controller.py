import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan # Example sensor message
from geometry_msgs.msg import Twist # Example motor command message

class BasicRobotController(Node):

    def __init__(self):
        super().__init__('basic_robot_controller')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.laser_callback,
            10)
        self.linear_speed = 0.2
        self.angular_speed = 0.0

    def laser_callback(self, msg):
        # Simple logic: if an obstacle is close, turn
        if min(msg.ranges) < 0.5: # If anything closer than 0.5m
            self.angular_speed = 0.5 # Turn left
            self.linear_speed = 0.0
        else:
            self.angular_speed = 0.0 # Go straight
            self.linear_speed = 0.2
        self.send_velocity_command()

    def send_velocity_command(self):
        cmd_vel_msg = Twist()
        cmd_vel_msg.linear.x = self.linear_speed
        cmd_vel_msg.angular.z = self.angular_speed
        self.publisher_.publish(cmd_vel_msg)
        self.get_logger().info(f"Sending velocity: Linear.x={self.linear_speed}, Angular.z={self.angular_speed}")

def main(args=None):
    rclpy.init(args=args)
    controller = BasicRobotController()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()