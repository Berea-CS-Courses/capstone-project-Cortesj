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
                        "port": "3306",
                        "inventory_db": "database",
                        "sensor_db": "database",
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
    
    def export_conf(self):
        print(self.data_dict)
        return self.data_dict

    def save_settings(self, inter, user, pwd, host, port, inv_db, sen_db):
        x = {
                "interval": int(inter),
                "sql_login": {
                    "username": "%s" % (user),
                    "password": "%s" % (pwd),
                    "host": "%s" % (host),
                    "port": "%s" % (port),
                    "inventory_db": "%s" % (inv_db),
                    "sensor_db": "%s" % (sen_db),
                }
            }

        file = open("code/settings.json", "w+")
        file.write(json.dumps(x, indent=4))
        file.close()