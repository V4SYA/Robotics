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

### Про файл.rviz

Rviz2 — это порт Rviz на ROS 2. Он предоставляет пользователям графический интерфейс для просмотра своего робота, данных датчиков, карт и многого другого. Он устанавливается по умолчанию вместе с ROS 2.

Файл.rviz является файлом настройки для инструмента RViz (ROS Visualization), который широко используется в экосистеме ROS (Robot Operating System) для визуализации данных, связанных с роботами и окружающей средой. RViz позволяет визуализировать различные аспекты работы робота, такие как его положение, ориентация, сенсорные данные, трансформации, планирование движения и многое другое.

Этот файл служит для определения, какие данные и элементы интерфейса RViz отображать, чтобы облегчить визуализацию и анализ информации, связанной с роботом или системой.

## Задание ex03
Собираем пакет
### colcon build --packages-select follower_of_turtle
Запускаем среду
### ros2 launch follower_of_turtle turtle_tf2_demo.launch.py
