# Здесь находятся решения задач модуля 3.

## Задание ex01
### source install/setup.bash
### ros2 run service_full_name service
### ros2 run service_full_name client Я Есть Грут

## Задание ex03

### ros2 bag record -o turtle_cmd_vel /turtle1/cmd_vel

### ros2 bag play turtle_cmd_vel

### ros2 topic echo /turtle1/pose >> pose_speed_x1.yaml

### ros2 bag play turtle_cmd_vel --rate 2.0

### ros2 topic echo /turtle1/pose >> pose_speed_x2.yaml
