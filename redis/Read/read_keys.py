from RedisConnection.localconnection import ConnectRedis
redis = ConnectRedis.connect()


class GetValues:
    def get_single_value(self, key):
        operation = redis.get(key)
        return operation

    def get_multiple_values(self, *data):
        many_operation = redis.mget(data)
        return many_operation

    def get_all_keys(self):
        return redis.keys("*")

    def get_random_key(self):
        return redis.randomkey()
