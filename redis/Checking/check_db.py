from RedisConnection.localconnection import ConnectRedis
redis = ConnectRedis.connect()


class CheckDatabase:
    def check_key_type(self, key):
        operation = redis.type(key)
        if str(operation) == "b'none'":
            return "This key does not exist"
        else:
            return operation

    def check_key_exist(self, key):
        operation = redis.exists(key)
        if operation == 1:
            return "{} exists in database".format(key)
        elif operation == 0:
            return "{} does not exist in database".format(key)
        else:
            return "Please check code something's fishy".format(key)
