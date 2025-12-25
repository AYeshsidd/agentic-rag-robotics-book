import rclpy
from rclpy.node import Node
from std_msgs.msg import String # Import standard message type

class SimpleSubscriber(Node):

    def __init__(self):
        super().__init__('simple_subscriber')
        # Create a subscription to the 'chatter' topic for String messages
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10) # QoS profile of 10
        self.subscription # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    simple_subscriber = SimpleSubscriber()
    rclpy.spin(simple_subscriber)
    simple_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()