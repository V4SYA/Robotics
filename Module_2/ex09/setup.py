from setuptools import setup
import os

package_name = 'ex09_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vasya',
    maintainer_email='your_email@example.com',
    description='A ROS 2 package with a custom message and service',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service_node = my_python_package.service_node:main',
        ],
    },
)

