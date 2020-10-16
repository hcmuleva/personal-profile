from RedisConnection.localconnection import ConnectRedis
redis = ConnectRedis.connect()


class RenameKeys:
    def rename_key(self, old_key, new_key):
        redis.rename(old_key, new_key)
        return "{} is renamed as {}".format(old_key, new_key)

    def move_key_to_another_db(self, key_name, db_number):
        redis.move(key_name, int(db_number))
        return "{} key is now in database number {}".format(key_name, db_number)
