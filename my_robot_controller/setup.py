import os
from glob import glob
from setuptools import setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # ('share/' + package_name, ['launch/launch.py']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*_launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nivaldo',
    maintainer_email='nivaldosleite@hotmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
         # "executable_name = package_name.file_name:main"
            "test_node = my_robot_controller.first_node:main",
            "draw_circle = my_robot_controller.draw_circle:main",
            "pose_subscriber = my_robot_controller.pose_subscriber:main",
            "turtle_controller = my_robot_controller.turtle_controller:main",
            "rpm_subscriber = my_robot_controller.rpm_subscriber:main",
            "pwm_publisher = my_robot_controller.pwm_publisher:main",
            "driver = my_robot_controller.driver:main"
            
        ],
    },
)
# ('share/' + package_name + '/webots_simulation/worlds',['worlds/adboxtra_2022_simplified.wbt'])
# ('share/' + package_name + '/webots_simulation/worlds',['adboxtra_2022_simplified.wbt'])