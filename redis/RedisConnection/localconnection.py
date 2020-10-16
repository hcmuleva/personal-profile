import redis


class ConnectRedis:

    def connect(self=None):
        my_host = "127.0.0.1"
        my_port = 6379
        my_db = 1
        r = redis.Redis(host=my_host, port=my_port, db=my_db)
        return r

