import psycopg2
conn = psycopg2.connect(database="lms", user="postgres", password="Aaditya@1432178", host="127.0.0.1", port="12345")
cur = conn.cursor()


class UpdateContacts:
    def update_contacts(self):
        cur.execute(""" UPDATE "Contacts" set name = 'aaditya_muleva' where user_id = 1; """)
        conn.commit()
        return "Contact updated"
