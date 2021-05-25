import json


class Settings:
    def __init__(self):
        """
        Initalize the class by reading the settings.json file and
        testing if file doesn't provide an IOError. Otherwise, it will
        generate a default settings.json file to be edited.
        """
        # Attempts to read Json file
        try:
            self.file = open("code/settings.json", "r")
        # IOError Detection & Default file generation
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
            # Dumps Dict ---> Json format
            self.file = open("code/settings.json", "w+")
            self.file.write(json.dumps(x, indent=4))
            self.file = open("code/settings.json", "r")
        # Load json into Dictionary & close file
        finally:
            self.data_dict = json.load(self.file)
            self.file.close()

    def export_conf(self):
        """
        Returns dictionary to be passed into other portions of
        program.

        Returns:
            [dict]: [dictionary containing all settings from json file]
        """
        print(self.data_dict)
        return self.data_dict

    def save_settings(self, inter, user, pwd, host, port, inv_db, sen_db):
        """
        Saves variables passed into function into settings.json with
        appropriate json formatting so it can be read upon next
        program restart.

        Args:
            inter ([int]): [Interval in Milliseconds]
            user ([string]): [User for DB]
            pwd ([string]): [Password for DB]
            host ([string]): [Host for DB]
            port ([string]): [Port for DB]
            inv_db ([string]): [Database for Inventory]
            sen_db ([string]): [Database for Sensor]
        """

        # Dictonary formatting of Json
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

        # Open Json settings file and dump dictionary in Json Format
        file = open("code/settings.json", "w+")
        file.write(json.dumps(x, indent=4))
        file.close()
