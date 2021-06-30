import sqlite3


class BBDD(object):
    """docstring for BBDD"""

    def __init__(self, name='BBDD1.db'):
        self.name_database = name
        self.connection = self.open_connection()
        self.ptr = self.connection.cursor()
        self.create_table()

    def open_connection(self):
        connection = sqlite3.connect(database=self.name_database)
        return connection

    def close_connection(self):
        self.connection.close()

    def create_table(self):
        try:
            self.ptr.execute("CREATE TABLE PERSONAS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(50), APELLIDO VARCHAR(50), PASSWORD VARCHAR(50), DIRECCION VARCHAR(50))")
        except Exception:
            print("create table already exist in database: ", self.name_database)
            pass

    def add_entry(self, data):
        self.ptr.execute("INSERT INTO PERSONAS VALUES(NULL,?,?,?,?)", data)
        self.connection.commit()
        self.close_connection()

    def get_data_from_id(self, id):
        # command = "SELECT * FROM PERSONAS WHERE ID=" + str(id)
        self.ptr.execute("SELECT * FROM PERSONAS WHERE ID=(?)", str(id))
        entry_fields = self.ptr.fetchall()
        self.close_connection()
        return entry_fields

    def update_data_in_field(self, prop, new_data, id_):
        self.connection = self.open_connection()
        self.ptr = self.connection.cursor()
        self.ptr.execute("UPDATE PERSONAS SET '{}'='{}' WHERE ID='{}'".format(prop, new_data, str(id_)))
        self.connection.commit()
        self.close_connection()

    def delete_data_by_id(self, id_):
        # self.connection = self.open_connection()
        # self.ptr = self.connection.cursor()
        self.ptr.execute("DELETE FROM PERSONAS WHERE ID='{}'".format(str(id_)))
        self.connection.commit()
        self.close_connection()
