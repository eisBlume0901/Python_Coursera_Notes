# How to import MySQL Connector in PyCharm
# https://youtu.be/elWvom3F2tQ

import mysql.connector as mysql

class Database:


    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.password = ''
        self.conn = None
        # cursor is a pointer to one row in a set of rows. The set of rows the cursor holds is called the active set
        self.cursor = None

    def connect(self, database_name):

        try:
            self.conn = mysql.connect(host=self.host,
                                      port=self.port,
                                      user=self.user,
                                      password=self.password,
                                      database=database_name)
            self.cursor = self.conn.cursor()

            if self.conn.is_connected():
                print('Connected to MySQL Database successfully!')

        except mysql.Error as e:
            print(e.msg)

    def execute_query(self, query):
        if self.conn is None or not self.conn.is_connected():
            print("Connect to the database first")
            return None

        self.cursor.execute(query)
        return self.cursor.fetchall()
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()