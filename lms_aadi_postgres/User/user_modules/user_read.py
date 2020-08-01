import psycopg2
conn = psycopg2.connect(database="lms", user="postgres", password="Aaditya@1432178", host="127.0.0.1", port="12345")
cur = conn.cursor()


class UserRead:
    def user_read(self):
        cur.execute("""SELECT user_id, user_name, user_password, age, gender from "User" """)
        return cur.fetchall()
