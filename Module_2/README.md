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

## Задание ex03
#### Установка colcon
### sudo apt install python3-colcon-common-extensions

ros2_ws/src существует.
Репозиторий уже клонирован.

### colcon build --symlink-install
Компилируем и устанавливаем ROS пакеты в текущем рабочем пространстве, создавая символические ссылки на установленные файлы вместо копирования их в другой каталог. Это позволяет сократить время компиляции и уменьшить размер установленных файлов.

#### Запускаем тесты:
### colcon test

### Создание пакета
Пакет — это организационная единица вашего кода ROS 2. Если нужно иметь возможность установить свой код или поделиться им с другими, вам понадобится организовать его в пакете.

### Что включает в себя пакет ROS 2?
### CMake
CMakeLists.txtфайл, описывающий, как построить код внутри пакета
include/<package_name>каталог, содержащий общедоступные заголовки пакета
package.xmlфайл, содержащий метаинформацию о пакете
srcкаталог, содержащий исходный код пакета
### Python
package.xmlфайл, содержащий метаинформацию о пакете
resource/<package_name>файл маркера для пакета
setup.cfgтребуется, когда в пакете есть исполняемые файлы, поэтому можно их найтиros2 run
setup.pyсодержащий инструкции по установке пакета
<package_name>- каталог с тем же именем, что и ваш пакет, используемый инструментами ROS 2 для поиска вашего пакета, содержит__init__.py

### Задания
#### Создание пакета
Переход в директорию
### cd ~/ros2_ws/src

Создание пакета
### ros2 pkg create --build-type ament_cmake <package_name>

Создание рабочей области
### source install/local_setup.bash

Запустить исполняемый файл
### ros2 run my_package my_node

Смотрим настройки package.xml

## Задание ex04
Запишем выходные данные сборки нашего пакета colcon build в файл colcon_build.txt
### colcon build --symlink-install > colcon_build.txt

## Задание ex05
#### Запуск ros2 (Turtlesim)
### ros2 run turtlesim turtlesim_node

#### Имена всех работающих узлов
### ros2 node list

#### Открываем новое окно терминала и пишем
### ros2 run turtlesim turtle_teleop_key

#### Информация об узле
### ros2 node info <node_name>

### Выполнение задания ex05
1) Сохраните вывод команды ros2 node list в файл rosnode_list.txt.
### ros2 node list > rosnode_list.txt
2) Сохраните вывод команды ros2 node info вашей ноды в файл rosnode_info.txt.
### ros2 node info <node_name> > rosnode_info.tx

## Задание ex06
Откройте новый терминал и запустите:
ros2 run turtlesim turtlesim_node
Откройте другой терминал и запустите:
ros2 run turtlesim turtle_teleop_key

### rqt_graph
Используется для визуализации узлов и заголовков, а также связи между ними.

Чтобы посмотреть данные, публикуемые по заголовку:
### ros2 topic echo <topic_name>

#### Публиковать данные в теме прямо из командной строки
### ros2 topic pub <topic_name> <msg_type> '<args>'

#### Управляем черепашкой
### ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"

--once— необязательный аргумент, означающий «опубликовать одно сообщение, затем выйти».

## Задание ex07
Создание новой черепашки:
### ros2 service call /spawn turtlesim/srv/Spawn "{x: , y: , theta: , name: ''}"
    
x: Это координата X, в которой будет размещена черепашка в симуляторе Turtlesim.

y: Это координата Y, в которой будет размещена черепашка в симуляторе Turtlesim.

theta: Это угол, задающий начальную ориентацию черепашки. Угол theta указывает направление, в котором черепашка будет смотреть. Обычно угол измеряется в радианах.

name: Это имя, которое будет присвоено новой черепашке. Каждая черепашка в симуляторе Turtlesim может иметь уникальное имя, которое идентифицирует её в системе.

Установите для параметра /turtlesim/background_g значение 124.
### ros2 param set /turtlesim background_r 150

### ros2 service list > rosservice_list.txt
Выходные данные всего сервера параметров
### ros2 param dump parameter_server.txt

## Задание ex08
Код из инструкции вставляем в launch/turtlesim_mimic_launch.py
Добавляем в описание запуска ещё одно окно с черепашкой.
В mimic node прописываем соответствующие зависимости.

### cd launch
### ros2 launch turtlesim_mimic_launch.py

Запуск rqt console
### ros2 run rqt_console rqt_console
