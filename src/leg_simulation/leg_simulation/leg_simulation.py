import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rclpy.qos import QoSProfile
from std_msgs.msg import String
import argparse

class LegIKTester(Node):

    def __init__(self, args):
        super().__init__('LegIKTester')

        # Declare parameters
        self.declare_parameters(
            namespace='',
            parameters=[
                ('x', args.x),
                ('y', args.y),
                ('z', args.z)
            ]
        )

        # Retrieve parameters
        self.x = self.get_parameter('x').value
        self.y = self.get_parameter('y').value
        self.z = self.get_parameter('z').value

        self.get_logger().info("Target x: %s" % self.x)
        self.get_logger().info("Target y: %s" % self.y)
        self.get_logger().info("Target z: %s" % self.z)


def main(args=None):
    rclpy.init(args=args)

    parser = argparse.ArgumentParser(description='ROS2 Node to test leg inverse kinematics')
    parser.add_argument('-x', type=float, default=0.0, help='x coordinate')
    parser.add_argument('-y', type=float, default=0.0, help='y coordinate')
    parser.add_argument('-z', type=float, default=0.0, help='z coordinate')
    parsed_args = parser.parse_args()

    node = LegIKTester(parsed_args)

    try:
        rclpy.spin_once(node, timeout_sec=1.0)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
