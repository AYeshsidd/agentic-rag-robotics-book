import rclpy
from rclpy.node import Node
from std_msgs.msg import String # Import standard message type

class SimplePublisher(Node):

    def __init__(self):
        super().__init__('simple_publisher')
        # Create a publisher that sends String messages to 'chatter' topic every 0.5 seconds
        self.publisher_ = self.create_publisher(String, 'chatter', 10) # QoS profile of 10
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello ROS 2 from Python: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()