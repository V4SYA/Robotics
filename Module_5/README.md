# Здесь находятся решения задач модуля 5.

## Задание ex01

### colcon build --packages-select robot

### ros2 launch robot robot_display.launch.py

## Задание ex03

### colcon build --packages-select ex03

### ros2 launch ex03 diff_drive.launch.py

Запускаем пакет teleop_twist_keyboard.
Этот пакет предоставляет интерфейс управления с клавиатуры для управления роботом.
Задаём аргументы ROS:
-r для перенаправления темы /cmd_vel на /robot/cmd_vel.
Все сообщения, отправленные в /cmd_vel, будут перенаправлены в /robot/cmd_vel
### ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/robot/cmd_vel
