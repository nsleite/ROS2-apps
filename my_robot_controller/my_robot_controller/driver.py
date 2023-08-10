import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from my_custom_message.msg import PwmMessage, RpmMessage


class Driver(Node):
    def __init__(self):
        super().__init__("driver")
        self.time_ms = 250 / 1000
        self.cmd_vel_subscriber_ = self.create_subscription(Twist, "/cmd_vel", 
                                                        self.publish_pwm, 10)
        # self.rpm_subscriber_ = self.create_subscription(RpmMessage, "/rpm", 
        #                                                 self.rpm_callback, 10)
        self.pwm_publisher_ = self.create_publisher(PwmMessage, "/pwm",10)
        # self.driver_timer_ = self.create_timer(self.time_ms, self.publish_pwm)

    # def cmd_vel_callback(self, msg: Twist):
    #     pass
    
    def rpm_callback(self, rpm: RpmMessage):
        pass

    def publish_pwm(self, cmd: Twist):
        pwm = PwmMessage()
        left_vel = cmd.linear.x - cmd.angular.z * track / 2
        right_vel = cmd.linear.x + cmd.angular.z * track / 2
        # pwm.pwm_left = int(3395 * left_vel + 700)
        # pwm.pwm_right = int(3395 * right_vel + 700)
        # if left_vel < 0:
        #     pwm.pwm_left = int(3395 * left_vel - 700)
        # if right_vel < 0:
        #     pwm.pwm_right = int(3395 * right_vel - 700)
        pwm.pwm_left = int(limit_value(factor * left_vel))
        pwm.pwm_right = int(limit_value(factor * right_vel))

        self.pwm_publisher_.publish(pwm)

        
def limit_value(value):
    if value > 4095:
        return 4095
    if value < -4095:
        return -4095
    return value

# print(limit_value(6587))

def main(args=None):
    global track, factor, gain
    track, factor, gain = 1, 4095 / 2, 1
    rclpy.init(args=args)
    driver = Driver()
    rclpy.spin(driver)
    rclpy.shutdown()