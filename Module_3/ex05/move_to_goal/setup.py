from setuptools import find_packages, setup

package_name = 'move_to_goal'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Vasya',
    maintainer_email='v.postnykh@g.nsu.ru',
    description='This package is used for task ex05 of Module 3',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move_to_goal = move_to_goal.move_to_goal:main'
        ],
    },
)
