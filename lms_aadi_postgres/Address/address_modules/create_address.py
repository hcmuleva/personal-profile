import psycopg2
conn = psycopg2.connect(database="lms", user="postgres", password="Aaditya@1432178", host="127.0.0.1", port="12345")
cur = conn.cursor()


class CreateAddress:
    def create_address(self, user_id, house_number, street, city, district, state, pin_code):
        to_insert = """INSERT INTO "Address" (user_id, house_number, street, city, district, state, pin_code) VALUES (%s, %s, %s, %s, %s, %s, %s); """
        my_values = (user_id, house_number, street, city, district, state, pin_code)
        cur.execute(to_insert, my_values)
        conn.commit()
        return "Contact_created"
