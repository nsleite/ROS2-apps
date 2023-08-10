#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class MyNode(Node):

    def __init__(self):
        super().__init__("my_first_node")
        self.counter_ = 0
        self.create_timer(1.5, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("hello " + str(self.counter_))
        self.counter_ += 1



def main(args=None):
    rclpy.init(args=args)       # initializes ros2 communication   args send = args received from call

    node = MyNode()

    rclpy.spin(node)            # keeps node alive till we killit with ctrl c

    rclpy.shutdown()            # Ends communication

if __name__ == "__main__":
    main()