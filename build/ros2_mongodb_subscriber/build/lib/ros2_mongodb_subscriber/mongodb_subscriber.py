import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Imu
from pymongo import MongoClient
import json

class MongodbSubscriber(Node):
    def __init__(self):
        super().__init__('mongodb_subscriber')
        print("here")
        self.subscription = self.create_subscription(Imu,'imu',self.db_listen_insert,10)
        self.mongodb_init()
        self.subscription 
        

    def db_listen_insert(self, msg):
        imu_data = {
            'orientation': {
                'x': msg.orientation.x,
                'y': msg.orientation.y,
                'z': msg.orientation.z,
                'w': msg.orientation.w
            },
            'angular_velocity': {
                'x': msg.angular_velocity.x,
                'y': msg.angular_velocity.y,
                'z': msg.angular_velocity.z
            },
            'linear_acceleration': {
                'x': msg.linear_acceleration.x,
                'y': msg.linear_acceleration.y,
                'z': msg.linear_acceleration.z
            },
        }
        # Serialize the data into JSON
        imu_json = json.dumps(imu_data)

        # Insert the JSON data into MongoDB
        self.get_logger().info('Inserted data "%s"' % imu_json)
        self.db.Imu.insert_one(json.loads(imu_json))


    def mongodb_init(self):
        MONGO_URI = "mongodb://192.168.142.218:27017/"
        DB_NAME = "ros2TopicDB"
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DB_NAME]
        print("mongo initialized")




def main(args=None):
    rclpy.init(args=args)
    mongodb_subscriber = MongodbSubscriber()
    rclpy.spin(mongodb_subscriber)
    mongodb_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
