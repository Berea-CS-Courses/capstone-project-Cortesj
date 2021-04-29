import mysql.connector
from mysql.connector import errorcode
import random # TEMP
import pandas


class Database:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def connect(self):
        try:
            self.conn = mysql.connector.connect(user=self.user,
                                                password=self.user,
                                                host=self.host,
                                                database=self.database
                                                )
            print("Connection Success!") # Test Line
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Username/Password could not Authenticate!")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist!")
            else:
                print(err)


    def new_plant(self, name, desc="", stock=0, temp=0, hum=0):
        self.cur = self.conn.cursor()
        add_plant = ("INSERT INTO plants_inventory "
                     "(name, description, stock, temp, hum) "
                     "VALUES (%s, %s, %s, %s, %s)")
        plant_data = (name, desc, stock, temp, hum)

        self.cur.execute(add_plant, plant_data)

        self.conn.commit()
        self.cur.close()

    def update_plant(self, id, name, desc="", stock=0, temp=0, hum=0):
        self.cur = self.conn.cursor()
        update_old = (
            "UPDATE plants_inventory "
            "SET name =%s, description=%s, stock=%s, temp=%s, hum=%s "
            "WHERE id =%s"
        )
        plant_data = (name, desc, stock, temp, hum, id)

        self.cur.execute(update_old, plant_data)
        
        self.conn.commit()
        self.cur.close()

    def view_plants(self):

        query = pandas.read_sql_query(
            '''
            SELECT *
            FROM plants_inventory
            ''', self.conn, index_col='id'
            )

        df = pandas.DataFrame(query)

    def find_plant(self, user_input=None):

        if user_input.isdigit() is True:

            query = pandas.read_sql_query(
                '''
                SELECT *
                FROM plants_inventory
                WHERE id=%s
                ''' % (user_input), self.conn, index_col='id'
            )
        else:
            query = pandas.read_sql_query(
                '''
                SELECT *
                FROM plants_inventory
                WHERE name='%s'
                ''' % (user_input), self.conn, index_col='id'
            )

        df = pandas.DataFrame(query)



test = Database(user='root', password='root', host='localhost', port='3306', database='inventory')
test.connect()
test.find_plant("modified_plant")
#test.view_plant()
#test.new_plant("test_plant", "test desc", random.randrange(0,1000), round(random.uniform(0,212), 2), round(random.uniform(0,100), 2))
#test.update_plant(2, "modified_plant", "lol desc", random.randrange(0,1000), round(random.uniform(0,212), 2), round(random.uniform(0,100), 2))