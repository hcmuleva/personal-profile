import psycopg2
conn = psycopg2.connect(database="lms", user="postgres", password="Aaditya@1432178", host="127.0.0.1", port="12345")
cur = conn.cursor()


class ReadContact:
    def read_contact(self):
        # operation = f""" SELECT %s, %s, %s from "Contacts" """
        # values = ("name", "email", "contact_number")
        # cur.execute(operation, values)
        cur.execute(""" SELECT name, email, contact_number from "Contacts" """)
        return cur.fetchall()
