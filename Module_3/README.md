# Здесь находятся решения задач модуля 3.

## Задание ex01
### source install/setup.bash
### ros2 run service_full_name service
### ros2 run service_full_name client Я Есть Грут

## Задание ex02

Запускаем черепашку
## ros2 run turtlesim turtlesim_node

Создаём среду
## source install/setup.bash

Запускаем ROS 2 узел с именем "server" из пакета "python_turtle_commands"
## ros2 run python_turtle_commands server
Запускаем ROS 2 узел с именем "client" из пакета python_turtle_commands
## ros2 run python_turtle_commands client

## Задание ex03

### ros2 bag record -o turtle_cmd_vel /turtle1/cmd_vel

### ros2 bag play turtle_cmd_vel

### ros2 topic echo /turtle1/pose >> pose_speed_x1.yaml

### ros2 bag play turtle_cmd_vel --rate 2.0

### ros2 topic echo /turtle1/pose >> pose_speed_x2.yaml

## Задание ex04
Если ваша программа установки ROS 2 работает не так, как ожидалось, вы можете проверить ее настройки с помощью инструмента ros2 doctor.

ros2 doctor проверяет все аспекты ROS 2, включая платформу, версию, сеть, среду, запущенные системы и многое другое, и предупреждает вас о возможных ошибках и причинах неполадок.

#### ros2 doctor --report > doctor.txt

## Задание ex05

### ros2 run turtlesim turtlesim_node
### ros2 run move_to_goal move_to_goal x, y, theta
### ros2 run move_to_goal move_to_goal 2 3 90
