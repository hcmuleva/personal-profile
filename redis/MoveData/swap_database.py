from RedisConnection.localconnection import ConnectRedis
redis = ConnectRedis.connect()


class SwapDatabase:
    def move_data(self, db_1, db_2):
        redis.swapdb(int(db_1), int(db_2))
        return "Data was swapped succesfully from database {} to database {}".format(db_1, db_2)


# my_obj = SwapDatabase()
# res = my_obj.move_data(1, 3)
# print(res)
