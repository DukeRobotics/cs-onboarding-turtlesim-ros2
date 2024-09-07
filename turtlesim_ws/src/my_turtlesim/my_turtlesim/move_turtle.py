import sys

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class MoveTurtle(Node):
    def __init__(self):
        super().__init__('move_turtle')

        # Initialize publisher for turtle velocity
        self.vel_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)

        self.rate = self.create_rate(20)

    def run(self):
        # Publish velocity to move turtle forward
        twist = Twist()
        twist.linear.x = 1.0

        while rclpy.ok():
            self.vel_publisher.publish(twist)
            rclpy.spin_once(self)
            self.rate.sleep()


def main():
    """
    Main function to create and run MoveTurtle node. Called by `ros2 run my_turtlesim move_turtle`.
    """
    rclpy.init(args=sys.argv)
    move_turtle = MoveTurtle()

    try:
        move_turtle.run()
    except KeyboardInterrupt:
        pass
    finally:
        move_turtle.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
