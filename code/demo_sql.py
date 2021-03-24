import mysql-connector-python


class SqlConnect:
    def __init__(self, user='root', password='password', host='127.0.0.1', database='database'):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
