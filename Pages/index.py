import os
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect


import sqlite3
from sqlite3 import Error

import json

app = Flask(__name__)

current_dir = os.getcwd()

myDatabasePath = current_dir+'/myDatabase.db'


@app.route("/", methods=["GET"])
def indexPage():
    # init_database()

    personsList = findAllPersons()

    return render_template('index.html', personsList=personsList, linkAdd=url_for('addPersonPage'))


@app.route("/add", methods=["GET"])
def addPersonPage():
    return render_template('add.html')


@app.route("/add", methods=["POST"])
def processAddPersonPage():
    sql = """ INSERT INTO personnes (firstname,lastname) VALUES (:firstname,:lastname );"""

    conn = None
    try:
        conn = sqlite3.connect(myDatabasePath)

        c = conn.cursor()
        c.execute(sql, request.form)
        conn.commit()

        return redirect(url_for('indexPage'))

    except Error as e:
        print(e)
        return str(e)
    finally:
        if conn:
            conn.close()


def findAllPersons():

    itemList = []

    sql = """ SELECT * from personnes """

    conn = None
    try:
        conn = sqlite3.connect(myDatabasePath)

        c = conn.cursor()
        res = c.execute(sql)
        return res.fetchall()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def init_database():
    create_connection(current_dir+'/myDatabase.db')

    sql_create_persons_table = """ CREATE TABLE IF NOT EXISTS personnes (
                                        id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text
                                        ); """

    conn = None
    try:
        conn = sqlite3.connect(myDatabasePath)

        c = conn.cursor()
        c.execute(sql_create_persons_table)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
