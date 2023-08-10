import rclpy
from rclpy.node import Node
from my_custom_message.msg import RpmMessage

class RpmSubscriberNode(Node):

    def __init__(self):
        super().__init__("rpm_subscriber")
        self.rpm_subscriber_ = self.create_subscription(RpmMessage, "/rpm",
                                                         self.rpm_callback, 10)
        self.rpm_subscriber_

    def rpm_callback(self, msg: RpmMessage):
        self.get_logger().info(f"I heard for: left rpm: {msg.rpm_left} | right rpm: {msg.rpm_right}")


def main(args=None):
    rclpy.init(args=args)
    rpm_subscriber = RpmSubscriberNode()
    rclpy.spin(rpm_subscriber)
    rclpy.shutdown()