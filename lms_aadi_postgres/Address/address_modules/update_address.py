import psycopg2
conn = psycopg2.connect(database="lms", user="postgres", password="Aaditya@1432178", host="127.0.0.1", port="12345")
cur = conn.cursor()


class UpdateAddress:
    def update_address(self):
        cur.execute(""" UPDATE "Address" set city = 'Barwani' where user_id = 1; """)
        return conn.commit()
