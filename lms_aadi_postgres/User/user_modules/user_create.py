import psycopg2
conn = psycopg2.connect(database="lms", user="postgres", password="Aaditya@1432178", host="127.0.0.1", port="12345")
cur = conn.cursor()


class CreateUser:
    def create_user(self, user_name, user_password, age, gender):
        to_insert = """INSERT INTO "User" (user_name, user_password, age, gender) VALUES (%s, %s, %s, %s); """
        my_values = (user_name, user_password, age, gender)
        cur.execute(to_insert, my_values)
        conn.commit()
        return "Data inserted"

    # def login_user(self, user_name, user_password):
    #     data = cur.execute(""" SELECT user_name, user_password from "User" """)
    #     conn.commit()
    #     return data
