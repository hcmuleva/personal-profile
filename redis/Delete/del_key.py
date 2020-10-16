from RedisConnection.localconnection import ConnectRedis
redis = ConnectRedis.connect()


class DelKeys:
    def delete_keys(self, *my_keys):
        redis.delete(*my_keys)
        return "Deleted {}".format(str(my_keys))
