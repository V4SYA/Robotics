import rclpy
import sys
from rclpy.node import Node
from ex09_package.srv import FullNameSumService

class ClientName(Node):

    def __init__(self):
        super().__init__('client_name')
        self.client = self.create_client(FullNameSumService, 'summ_full_name')

        # ожидаем, пока сервис FullNameSumService не станет доступным. 
        # Если сервис не становится доступным в течение 1 секунды, 
        # выводится сообщение "I can't wait any more"
        while not self.client.wait_for_service(timeout_sec=1.0):
        	self.get_logger().info('I can't wait any more')
         
        # объект запроса для сервиса, 
        # который будет использоваться для отправки запроса сервису
        self.request = FullNameSumService.Request()

    # принимаем аргументы last_name, name и first_name, 
    # устанавливаем их в объекте запроса, а затем вызываем сервис асинхронно
    def give_request(self, last_name, name, first_name):
        self.request.last_name = last_name
        self.request.name = name
        self.request.first_name = first_name
        
        res = self.client.call_async(self.request)
        # ожидаем завершения асинхронного вызова сервиса
        rclpy.spin_until_future_complete(self, res)
        
        return res.result()

def main():
    rclpy.init()
    client_name = ClientName()
    res = client_name.give_request(sys.argv[1], sys.argv[2], sys.argv[3])

    # если получен результат, выводим полное имя
    if res:
    	client_name.get_logger().info('Full name: %s' % res.full_name)
        
    client_name.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
