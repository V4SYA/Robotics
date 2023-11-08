import os
import launch_ros

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.actions import TimerAction


def generate_launch_description():
    # Configure ROS nodes for launch

    # Настройка путей и параметров
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    
    pkg_share = launch_ros.substitutions.FindPackageShare(package='ex03').find('ex03')
    
    urdf_path  =  os.path.join(pkg_share, 'description', 'robot.urdf.xacro')
    robot_desc = ParameterValue(Command(['xacro ', urdf_path]), value_type=str)
    
    
    # Запускаем симуляцию Gazebo
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={'gz_args': "-r empty.sdf"}.items(),
    )

    # Spawn robot
    create = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-name', 'robot',
                   '-topic', 'robot_description',
                   '-x', '0.0',
                   '-y', '0.0',
                   '-z', '0.45',
                ],
        output='screen',
    )

    # Принимаем описание и углы сочленений в качестве входных данных и публикуем трехмерные позы звеньев робота.
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='both',
        parameters=[
            {'robot_description': robot_desc},
            {'frame_prefix': "robot/"}
        ]
    )

    # Visualize in RViz
    rviz = Node(
       package='rviz2',
       executable='rviz2',
       arguments=['-d', os.path.join(pkg_share, 'config', 'diff_drive.rviz')],
       condition=IfCondition(LaunchConfiguration('rviz'))
    )

    # Устанавливаем мост для передачи сообщений между ROS и Gazebo для обеспечения коммуникации между симуляцией и контролем робота.
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters=[{
            'config_file': os.path.join(pkg_share, 'config', 'robot_bridge.yaml'),
            'qos_overrides./tf_static.publisher.durability': 'transient_local',
        }],
        output='screen'
    )
    
    # Запуск инструмента RQT Robot Steering для управления роботом
    rqt_robot_steering = Node(
        package='rqt_robot_steering',
        executable='rqt_robot_steering'
        )

    ''' Определяем порядок запуска узлов и приложений, включая зависимости между ними.
    Лаунч-файл будет запускать симуляцию Gazebo, создавать робота,
    публиковать его состояние, запускать RViz,
    настраивать мост между ROS и Gazebo и запускать инструмент RQT Robot Steering.'''
    return LaunchDescription([
        gz_sim,
        DeclareLaunchArgument('rviz', default_value='true',
                              description='Open RViz.'),
        bridge,
        robot_state_publisher,
        rviz,
        rqt_robot_steering,
        TimerAction(
            period=5.0,
            actions=[create])
    ])
