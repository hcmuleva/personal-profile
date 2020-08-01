import psycopg2
conn = psycopg2.connect(database="lms", user="postgres", password="Aaditya@1432178", host="127.0.0.1", port="12345")
cur = conn.cursor()


class UserUpdate:
    def user_update(self):
        # values = (table_name, column_key, column_value, user_id_key, user_id_value)
        # cur.execute(operation, values)
        cur.execute(""" UPDATE "User" set user_name = 'aaditya_muleva' where user_id = 1; """)
        conn.commit()
        return "Updated"
