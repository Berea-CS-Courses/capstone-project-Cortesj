import json


class Settings:
    def __init__(self):
        # Attempt to open settings.json
        try:
            self.file = open("code/settings.json", "r")
        # If IOError detected then create default file
        except IOError:
            x = {   
                    "interval": 600,
                    "sql_login": {
                        "username": "root",
                        "password": "password",
                        "host": "localhost",
                        "port": "8080",
                        "database": "database"
                    }
                }
            # Dump dictonary into empty json file then set to read
            self.file = open("code/settings.json", "w+")
            self.file.write(json.dumps(x, indent=4))
            self.file = open("code/settings.json", "r")
        # Load json into Dictionary & close file
        finally:
            self.data_dict = json.load(self.file)
            self.file.close()
