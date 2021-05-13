def save_settings(inter, user, pwd, host, port, inv_db, sen_db):
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


save_settings(123, 2323, 32, 32, 424, 423, 423)