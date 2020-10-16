import sys
from RedisConnection.localconnection import ConnectRedis
sys.path.append('/home/aaditya/Aaditya_Develop/redis')
redis = ConnectRedis.connect()


class CreateKeyValue:
    def single_key_value(self, my_key, my_value):
        redis.set(my_key, my_value)
        return "Inserted ({} {})".format(my_key, my_value)

    def multiple_key_value(self, json_data):
        redis.mset(json_data)
        return "Inserted {}".format(json_data)
