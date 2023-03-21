import os
import sqlite3
from sqlite3 import Error

current_dir = os.getcwd()
myDatabasePath = current_dir+'/myDatabase.db'


class PersonRepository:

    def __init__(self):
        self.conn = None
        pass

    def getConnection(self):
        if self.conn is None:
            self.conn = sqlite3.connect(myDatabasePath)

        return self.conn

    def findAll(self):
        try:
            itemList = []

            sql = """ SELECT * from personnes """

            c = self.getConnection().cursor()
            res = c.execute(sql)
            rows = res.fetchall()

            for row in rows:
                itemList.append({"firstname": row[1], "lastname": row[2]})

            return itemList

        except Error as e:
            print(e)

    def insert(self, form):
        try:

            sql = """ INSERT INTO personnes (firstname,lastname) VALUES (:firstname,:lastname );"""

            c = self.getConnection().cursor()
            c.execute(sql, form)
            self.conn.commit()

        except Error as e:
            print(e)

    def __del__(self):
        if self.conn:
            self.conn.close()
