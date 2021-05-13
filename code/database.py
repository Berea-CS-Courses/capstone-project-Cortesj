import mysql.connector
from mysql.connector import errorcode
import pandas
from pandas.core.frame import DataFrame


class Database:
    def __init__(self, user, password, host, port, database):
        """
        Initialize class with appropriate connection
        details for mySQL DB

        Args:
            user ([string]): [User of DB]
            password ([string]): [Password of DB]
            host ([string]): [Host of DB]
            port ([string]): [Port of DB]
            database ([string]): [Specific DB/Schema]
        """
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def connect(self):
        """
        Function to attempt a connection to the DB
        and catch any errors to be reported to the
        user.
        """
        try:
            self.conn = mysql.connector.connect(
                user=self.user,
                password=self.user,
                host=self.host,
                database=self.database
                )
            print("Connection Success!")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Username/Password could not Authenticate!")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist!")
            else:
                print(err)

    def new_plant(self, name, desc="", stock=0, temp=0, hum=0):
        """
        Function that sents a Query to DB to create new Plant
        entry with appropriate parameters.

        Args:
            name ([str]): [Name of Plant]
            desc (str, optional): [Description of Plant]. Defaults to "".
            stock (int, optional): [Amt of specifc plant]. Defaults to 0.
            temp (int, optional): [Temp pref. of plant]. Defaults to 0.
            hum (int, optional): [humid pref of plant]. Defaults to 0.
        """
        self.cur = self.conn.cursor()
        add_plant = ("INSERT INTO plants_inventory "
                     "(name, description, stock, temp, hum) "
                     "VALUES (%s, %s, %s, %s, %s)")
        plant_data = (name, desc, stock, temp, hum)

        self.cur.execute(add_plant, plant_data)

        self.conn.commit()
        self.cur.close()

    def update_plant(self, id, name, desc="", stock=0, temp=0, hum=0):
        """
        Function to make a Query to DB that update a specific
        plant via ID

        Args:
            id ([type]): [description]
            name ([type]): [description]
            desc (str, optional): [description]. Defaults to "".
            stock (int, optional): [description]. Defaults to 0.
            temp (int, optional): [description]. Defaults to 0.
            hum (int, optional): [description]. Defaults to 0.
        """
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
        """
        Grabs a copy of entire Inventory DB into a Dataframe
        for UI widget.

        Returns:
            [dataframe]: [copy of Inventory DB]
        """
        query = pandas.read_sql_query(
            '''
            SELECT *
            FROM plants_inventory
            ''', self.conn, index_col='id'
            )

        df = pandas.DataFrame(query)

        return df

        # print(df)
        # print(df.index.to_list())

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

        print(df)

    def del_plant(self, id=None):
        """
        Executes a Query to delete a certain inventory entry
        via their ID.

        Args:
            id ([int], optional): [ID of Plant]. Defaults to None.
        """
        self.cur = self.conn.cursor()

        sql_query = "DELETE FROM plants_inventory WHERE id=%s" % (id)

        try:
            self.cur.execute(sql_query)
            self.conn.commit()
            self.cur.close()
        except Exception as e:
            self.conn.rollback()

    def grab_sensor(self):
        """
        Function to grab the current week's sensor data and
        packaged into a Dataframe to be used for a visualization
        widget in UI.

        Returns:
            [dataframe]: [dataframe of all entries for the current week]
        """
        try:
            query = pandas.read_sql_query(
                '''
                SELECT date, temperature, humidity
                FROM sensor
                WHERE week(date) = week(now())
                ''',
                self.conn,
                index_col='date'
            )

            df = pandas.DataFrame(query)
            df.index.name = None

            return df
        except Exception as e:
            print("ERROR")
