from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    turtle_controller = Node(
        package="my_robot_controller",
        executable="turtle_controller"
    )

    turtle = Node(
        package="turtlesim",
        # namespace="turtlesim1",
        executable="turtlesim_node"
    )

    ld.add_action(turtle_controller)
    ld.add_action(turtle)

    return ld

#     return LaunchDescription([
#         Node(
#             package='demo_nodes_cpp',
#             executable='talker',
#             name='talker'),
# ])