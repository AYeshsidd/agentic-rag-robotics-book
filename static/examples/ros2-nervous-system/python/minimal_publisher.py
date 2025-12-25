import rclpy
from rclpy.node import Node

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        # Node initialization logic here

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher) # Keep node alive
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()