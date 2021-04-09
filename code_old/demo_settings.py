import configparser
from tkinter import *


class Settings:
    def __init__(self):
        self.settings = configparser.ConfigParser()
        self.settings.read('~/Documents/GitHub/capstone-project-Cortesj/code/settings.ini')

        #self.interval = self.settings.get('INTERVAL', 'time')
        #self.sql_params = self.settings.get('SQL', 'user')

    def interval_validity(self):
        pass

    def sql_validity(self):
        pass

    def settings_gui(self):
        self.settings_gui = Tk()
        self.settings_gui.title("Settings (Development)")
        self.settings_gui.geometry('400x400')
        self.settings_gui.resizable(False, False)

        self.settings_gui.mainloop()


lol = Settings()
#lol.settings_gui()
