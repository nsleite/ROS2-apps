import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int32
from my_custom_message.msg import PwmMessage
import random

class MultiPwmPublisher(Node):
    def __init__(self):
        super().__init__("pwm_publisher")
        self.time_ms = 500 / 1000
        self.left_pwm_publisher_ = self.create_publisher(Int32, "pwm_left", 10)
        self.left_pwm_timer_ = self.create_timer(self.time_ms, self.publish_left_pwm)

        self.right_pwm_publisher_ = self.create_publisher(Int32, "pwm_right", 10)
        self.right_pwm_timer_ = self.create_timer(self.time_ms, self.publish_right_pwm)

    def publish_left_pwm(self):
        pwm_left = random.randint(0, 4095)
        pwm = Int32()
        pwm.data = pwm_left
        self.left_pwm_publisher_.publish(pwm)

    def publish_right_pwm(self):
        pwm_right = random.randint(0, 4095)
        pwm = Int32()
        pwm.data = pwm_right
        self.right_pwm_publisher_.publish(pwm)

class PwmPublisher(Node):
    def __init__(self):
        super().__init__("pwm_publisher")
        self.time_ms = 500 / 1000
        self.pwm_publisher_ = self.create_publisher(PwmMessage, "pwm", 10)
        self.pwm_timer_ = self.create_timer(self.time_ms, self.publish_pwm)

    def publish_pwm(self):
        msg = PwmMessage()
        msg.pwm_left = random.randint(0, 255)
        msg.pwm_right = random.randint(0, 255)
        self.pwm_publisher_.publish(msg)    

def main(args=None):
    rclpy.init(args=args)
    pwm_node = PwmPublisher()
    rclpy.spin(pwm_node)
    rclpy.shutdown

