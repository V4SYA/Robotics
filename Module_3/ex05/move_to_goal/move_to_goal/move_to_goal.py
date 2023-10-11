import rclpy
import sys
import math
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from rclpy.node import Node

class TurtleIsMoving(Node):

     def __init__(self):
         super().__init__('move_to_goal')
         
         # Создание публикатора для управления движением черепахи
         self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
         # Создание подписчика для получения информации о позиции черепахи
         self.subscriber = self.create_subscription(Pose, '/turtle1/pose', self.update_pose, 10)
         
         # Хранения информации о позиции черепахи
         self.pose = Pose()
         
         # Настройка таймера
         self.timer = self.create_timer(0.1, self.go_to_goal)
         
         # Определяем параметры командной строки
         self.goal_x = float(sys.argv[1])
         self.goal_y = float(sys.argv[2])
         self.goal_theta = float(sys.argv[3]) * math.pi / 180

     # Вызываем, когда приходит новое сообщение о позиции черепахи, обновляет информацию о позиции в переменной self.pose
     def update_pose(self, data):
         self.pose = data

     # Вычисляем линейную и угловую скорости
     def go_to_goal(self):
         msg = Twist()

         # Расстояние до точки назначения
         lenght_of_path = math.sqrt((self.goal_x - self.pose.x) ** 2 + (self.goal_y - self.pose.y) ** 2)
         
         # Угол до точки назначения
         angle = math.atan2(self.goal_y - self.pose.y, self.goal_x - self.pose.x)

         # Линейная скорость
         linear_vel = 1.0 * lenght_of_path
         # Угловая скорость
         angular_vel = 4.0 * (angle - self.pose.theta)

	 # Установили значения линейной и угловой скоростей
	 # в соответствующих полях сообщения msg, которое будет отправлено черепахе.
         msg.linear.x = linear_vel
         msg.angular.z = angular_vel
         
         self.publisher.publish(msg)
         
         # Если lenght_of_path < 0.1 и angle > 0.1,
         # то это означает, что черепашка приблизилась к цели, но осталась несовпадение угла. 
         # В этом случае, черепашка должна доворачиваться к желаемому углу.
         if lenght_of_path < 0.1 and abs(angle) > 0.1:
            # Устанавили угловую скорость
            msg.angular.z = self.goal_theta
            self.publisher.publish(msg)
            
            # Цикл для доворачивания к углу
            for count in range(9):
            	self.publisher.publish(msg)
            	time.sleep(0.1)
            
            msg.linear.x = 0.0  # Остановка линейного движения
            msg.angular.z = 0.0  # Остановка вращения
            
            self.get_logger().info("We have reached the goal.")
            self.timer.cancel()
            self.publisher.publish(msg)
            quit()

def main(args=None):
    rclpy.init(args=args)
    
    turtle = TurtleIsMoving()
    
    rclpy.spin(turtle)
    turtle.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
