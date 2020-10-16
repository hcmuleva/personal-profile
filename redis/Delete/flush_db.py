from RedisConnection.localconnection import ConnectRedis

redis = ConnectRedis.connect()


class FlushDB:
    def clear_all(self):
        get_input = input("WARNING : This will erase your whole db, please confirm again you want "
                          "to clear whole data in current databases (y/n)")
        if get_input.lower() == "y":
            redis.flushdb()
            return "Current database cleaned"
        elif get_input.lower() == "n":
            return "Operation aborted"
        else:
            return "Incorrect input"
