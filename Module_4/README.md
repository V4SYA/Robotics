# Здесь находятся решения задач модуля 4.

## Задание ex01
### source install/setup.bash
### ros2 launch turtle_tf2_py turtle_tf2_demo.launch.py

Создаём диаграмму кадров, транслируемых tf2 через ROS.
### ros2 run tf2_tools view_frames

Сохраните вывод результатов трансформации координат между фреймами turtle1 и turtle2 в файл transform.txt 
### ros2 run tf2_ros tf2_echo turtle1 turtle2 > transform.txt

## Задание ex02
Собираю пакет
### colcon build --packages-select my_carrot

Выполняю запуск launch file
### ros2 launch my_carrot dynamic.launch.py

Управление черепашкой
### ros2 run turtlesim turtle_teleop_key
