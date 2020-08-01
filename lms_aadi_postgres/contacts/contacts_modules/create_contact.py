import psycopg2
conn = psycopg2.connect(database="lms", user="postgres", password="Aaditya@1432178", host="127.0.0.1", port="12345")
cur = conn.cursor()


class CreateContact:
    def create_contact(self, user_id, user_name, user_email, user_phone):
        to_insert = """INSERT INTO "Contacts" (user_id, name, email, contact_number) VALUES (%s, %s, %s, %s); """
        my_values = (user_id, user_name, user_email, user_phone)
        cur.execute(to_insert, my_values)
        conn.commit()
        return "Contact created"
