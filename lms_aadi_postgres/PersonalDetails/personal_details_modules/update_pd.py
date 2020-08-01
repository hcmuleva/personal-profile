import psycopg2
conn = psycopg2.connect(database="lms", user="postgres", password="Aaditya@1432178", host="127.0.0.1", port="12345")
cur = conn.cursor()


class UpdateDetails:
    def update_details(self):
        cur.execute(""" UPDATE "Personal_details" set academic_details = 'm_tech' where user_id = 1; """)
        return conn.commit()
