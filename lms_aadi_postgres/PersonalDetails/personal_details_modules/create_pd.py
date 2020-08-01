import psycopg2
conn = psycopg2.connect(database="lms", user="postgres", password="Aaditya@1432178", host="127.0.0.1", port="12345")
cur = conn.cursor()


class CreateDetails:
    def create_details(self, user_id, birth_date, blood_group, academic_details, hobbies):
        to_insert = """INSERT INTO "Personal_details" (user_id, birth_date, blood_group, academic_details, hobbies) VALUES (%s, %s, %s, %s, %s); """
        my_values = (user_id, birth_date, blood_group, academic_details, hobbies)
        cur.execute(to_insert, my_values)
        return conn.commit()
