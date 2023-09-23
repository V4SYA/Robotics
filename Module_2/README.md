# Здесь находятся решения задач модуля 2.

## Задание ex01
#### Источник установочных файлов.

Нужно будет запускать эту команду в каждом новом источнике, который я открываю, чтобы получить доступ к командам ROS 2:

### source /opt/ros/humble/setup.bash

Можно заменить ".bash" на другой: setup.bash, setup.sh, setup.zsh

#### Создание нового каталога.

### mkdir -p ~/ros2_ws/src
### cd ~/ros2_ws/src

#### Клонирование образца репозитория.

### git clone https://github.com/ros/ros_tutorials.git -b humble

#### Разрешение зависимостей.

Возвращаемся в каталог ros2_ws и пишем:
### rosdep install -i --from-path src --rosdistro humble -y

Если всё хорошо, консоль выведет соответствующее сообщение.

#### Создание рабочего пространства с помощью colcon.
Собираем пакеты:
### colcon build

## Задание ex02
Команда
### ros2 pkg prefix ros2topic
выводит путь к ROS пакету «ros2topic».

Команда
### ros2 pkg prefix action_tutorials_py
выводит список выполняемых файлов в каталоге пакета «action_tutorials_py».
## Пункт 3

# Заголовок 2
