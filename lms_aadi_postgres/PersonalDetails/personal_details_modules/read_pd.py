import psycopg2
conn = psycopg2.connect(database="lms", user="postgres", password="Aaditya@1432178", host="127.0.0.1", port="12345")
cur = conn.cursor()


class ReadDetails:
    def read_details(self):
        # operation = f""" SELECT (%s), (%s), (%s), (%s), (%s), (%s), (%s) from "Address" """
        # values = (my_user_id, my_house_number, my_street, my_city, my_district, my_state, my_pin_code)
        # cur.execute(operation, values)
        cur.execute(""" SELECT user_id, birth_date, blood_group, academic_details, hobbies from "Personal_details" """)
        return cur.fetchall()
