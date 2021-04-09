import json


class Settings:
    def __init__(self):
        self.file = open("code/settings.json", "r")
        self.data_dict = json.load(self.file)

    def validity(self):
        pass


test_obj = Settings()
print(test_obj.data_dict)

x = {'interval': 600,
     'sql_login': {
         'username': 'root',
         'password': 'password',
         'host': '127.0.0.1',
         'port': '8080',
         'database': 'database'
         }
     }

y = json.dumps(x)
print(y)