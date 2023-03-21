import os

current_dir = os.getcwd()


class InitRepository:

    def init_database(self):
        self.create_connection(current_dir+'/myDatabase.db')

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
