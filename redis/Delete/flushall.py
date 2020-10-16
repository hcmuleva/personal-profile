from RedisConnection.localconnection import ConnectRedis
redis = ConnectRedis.connect()


class FlushAllDb:
    def flush_all_data(self):
        get_input = input("WARNING : This will erase your whole db, please confirm again you want "
                          "to clear whole data in all databases (y/n)")
        if get_input.lower() == "y":
            redis.flushall()
            return "Whole database cleaned"
        elif get_input.lower() == "n":
            return "Operation aborted"
        else:
            return "Incorrect input"
