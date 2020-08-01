import psycopg2
conn = psycopg2.connect(database="lms", user="postgres", password="Aaditya@1432178", host="127.0.0.1", port="12345")
cur = conn.cursor()


class DeleteDetails:
    def delete_details(self, my_id):
        my_operation = f""" DELETE from "Personal_details" where user_id = (%s); """
        cur.execute(my_operation, my_id)
        return conn.commit()
