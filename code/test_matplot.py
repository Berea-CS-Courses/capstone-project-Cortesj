from tkinter import *
import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import matplotlib.pyplot as plt
import pandas
import numpy as np

import matplotlib.animation as animation

from database import *
from config import *


class User_Interface:
    def __init__(self):
        self.inv_conn = Database(
            user='root',
            password='root',
            host='localhost',
            port='3306',
            database='inventory'
            )
        self.inv_conn.connect()

        self.sen_conn = Database(
            user='root',
            password='root',
            host='localhost',
            port='3306',
            database='test_db'
            )
        self.sen_conn.connect()

    def main_window(self):
        # Screen Settings/Geometry
        self.window = Tk()
        self.window.title("Greenhouse Mangement (Development)")
        self.window.geometry('810x540')
        self.window.resizable(False, False)

        # Screen Centering
        win_wid = 810
        win_hei = 540

        x_left = int(self.window.winfo_screenwidth()/2 - win_wid/2)
        y_top = int(self.window.winfo_screenheight()/2 - win_hei/2)

        self.window.geometry("+{}+{}".format(x_left, y_top))

        # Button Size
        btn_h = 2
        btn_w = 35

        btn_x = 450

        # Inventory Buttons
        inv_create = Button(
            self.window,
            text='Create Inventory Entry',
            bd='2',
            bg='gray',
            command=self.create_entry,
            height=btn_h,
            width=btn_w
            )
        inv_create.place(x=btn_x, y=70)

        inv_edit = Button(
            self.window,
            text='Edit/Delete Inventory Entry',
            bd='2',
            bg='gray',
            command=self.edit_entry,
            height=btn_h,
            width=btn_w
            )
        inv_edit.place(x=btn_x, y=140)

        inv_view = Button(
            self.window,
            text='View Inventory',
            bd='2',
            bg='gray',
            command=self.view_inventory,
            height=btn_h,
            width=btn_w
            )
        inv_view.place(x=btn_x, y=210)

        # Report Buttons
        report_current = Button(
            self.window,
            text='Current Report',
            bd='2',
            bg='gray',
            command=self.current_report,
            height=btn_h,
            width=btn_w
            )
        report_current.place(x=btn_x, y=280)

        report_history = Button(
            self.window,
            text='Report History',
            bd='2',
            bg='gray',
            command=self.report_history,
            height=btn_h,
            width=btn_w
            )
        report_history.place(x=btn_x, y=350)

        report_critical = Button(
            self.window,
            text='Critical Issues',
            bd='2',
            bg='gray',
            command=self.critial_issues,
            height=btn_h,
            width=btn_w,
            fg='red'
            )
        report_critical.place(x=btn_x, y=420)

        # Settings Button
        settings = Button(
            self.window,
            text='Settings',
            bd='2',
            bg='gray',
            command=self.settings,
            height=1,
            width=10
            )
        settings.place(x=650, y=490)

        def ani(dump):
            #new_rando = {'Temperature': np.random.randint(100), 'Humidity': np.random.randint(100)}
            #print(self.curr_data)
            #self.curr_data = self.curr_data.append(new_rando, ignore_index=True)
            del self.curr_data
            self.curr_data = self.sen_conn.grab_sensor()

            self.curr_data.plot(legend=None, y='temperature', ax=self.ax1)            

        # Load CSV/Graphs | Needs to be Own Function
        #data = {'Temperature': [100, 200],
        #        'Humidity': [34, 64]}
        #self.curr_data = pandas.DataFrame(data)
        self.curr_data = self.sen_conn.grab_sensor()

        # Graphic 1 | Temp
        self.figure1 = plt.Figure(figsize=(4, 5), dpi=100)
        self.ax1 = self.figure1.add_subplot(211)

        graphic_1 = FigureCanvasTkAgg(self.figure1, self.window)
        graphic_1.get_tk_widget().place(x=30, y=15)
        self.curr_data.plot(legend=None, y='temperature', ax=self.ax1)
        self.ax1.set_title('Current Temperature')

        ani = animation.FuncAnimation(self.figure1, func=ani, interval=5000)

        # Main Window Loop
        self.window.mainloop()

    def create_entry(self):
        # Screen Settings/Geometry
        self.win_create_entry = Toplevel(self.window)
        self.win_create_entry.title("Add Inventory Item")
        self.win_create_entry.geometry('400x350')
        self.win_create_entry.minsize(400, 350)
        self.win_create_entry.maxsize(600, 350)

        self.win_create_entry.columnconfigure(0, weight=1)
        self.win_create_entry.columnconfigure(1, weight=4)

        self.name_label = Label(self.win_create_entry, text='Name')
        self.name_label.grid(column=0, row=0, sticky="NESW")
        self.name_entry = Entry(self.win_create_entry, bg='White', fg='Black')
        self.name_entry.grid(column=1, row=0, sticky="EW")

        self.desc_label = Label(self.win_create_entry, text='Description')
        self.desc_label.grid(column=0, row=1)
        self.desc_entry = Text(self.win_create_entry, height=10, width=10, bg='White', fg='Black')
        self.desc_entry.grid(column=1, row=1, sticky='NESW')
        
        self.stock_label = Label(self.win_create_entry, text='Stock')
        self.stock_label.grid(column=0, row=2)
        self.stock_entry = Entry(self.win_create_entry, bg='White', fg='Black', justify='center', width=5)
        self.stock_entry.grid(column=1, row=2, sticky='W')

        self.temp_label = Label(self.win_create_entry, text='Temperature')
        self.temp_label.grid(column=0, row=3)
        self.temp_entry = Entry(self.win_create_entry, bg='White', fg='Black', justify='center', width=5)
        self.temp_entry.grid(column=1, row=3, sticky='W')

        self.hum_label = Label(self.win_create_entry, text='Humidity')
        self.hum_label.grid(column=0, row=4)
        self.hum_entry = Entry(self.win_create_entry, bg='White', fg='Black', justify='center', width=5)
        self.hum_entry.grid(column=1, row=4, sticky='W')

        self.save_btn = Button(
            self.win_create_entry,
            text='Save',
            bd='2',
            bg='gray',
            command=self.create_btn,
            )
        self.save_btn.grid(row=5, columnspan=2, sticky="NESW")
    
    def create_btn(self):
        self.inv_conn.new_plant(
            name=self.name_entry.get(),
            desc=self.desc_entry.get('1.0', 'end-1c'),
            stock=int(self.stock_entry.get()),
            temp=float(self.temp_entry.get()),
            hum=float(self.hum_entry.get())
        )
        self.win_create_entry.destroy()

    def edit_entry(self, list_data):
        self.id_store = list_data[0]
        # Screen Settings/Geometry
        self.win_edit = Toplevel(self.window)
        self.win_edit.title("Edit Inventory Item")
        self.win_edit.geometry('400x360')
        self.win_edit.minsize(400, 360)
        self.win_edit.maxsize(600, 350)

        self.win_edit.columnconfigure(0, weight=1)
        self.win_edit.columnconfigure(1, weight=4)

        self.id_label = Label(self.win_edit, text='ID')
        self.id_label.grid(column=0, row=0, sticky="NESW")
        self.id_entry = Label(self.win_edit, bg='White', fg='Black', text=str(list_data[0]))
        self.id_entry.grid(column=1, row=0, sticky="EW")

        self.name_label = Label(self.win_edit, text='Name')
        self.name_label.grid(column=0, row=1, sticky="NESW")
        self.name_entry = Entry(self.win_edit, bg='White', fg='Black')
        self.name_entry.insert('0', list_data[1])
        self.name_entry.grid(column=1, row=1, sticky="EW")

        self.desc_label = Label(self.win_edit, text='Description')
        self.desc_label.grid(column=0, row=2)
        self.desc_entry = Text(self.win_edit, height=10, width=10, bg='White', fg='Black')
        self.desc_entry.insert('1.0', list_data[2])
        self.desc_entry.grid(column=1, row=2, sticky='NESW')
        
        self.stock_label = Label(self.win_edit, text='Stock')
        self.stock_label.grid(column=0, row=3)
        self.stock_entry = Entry(self.win_edit, bg='White', fg='Black', justify='center', width=5)
        self.stock_entry.insert('0', list_data[3])
        self.stock_entry.grid(column=1, row=3, sticky='W')

        self.temp_label = Label(self.win_edit, text='Temperature')
        self.temp_label.grid(column=0, row=4)
        self.temp_entry = Entry(self.win_edit, bg='White', fg='Black', justify='center', width=5)
        self.temp_entry.insert('0', list_data[4])
        self.temp_entry.grid(column=1, row=4, sticky='W')

        self.hum_label = Label(self.win_edit, text='Humidity')
        self.hum_label.grid(column=0, row=5)
        self.hum_entry = Entry(self.win_edit, bg='White', fg='Black', justify='center', width=5)
        self.hum_entry.insert('0', list_data[5])
        self.hum_entry.grid(column=1, row=5, sticky='W')

        self.del_btn = Button(
            self.win_edit,
            text='Delete',
            bd='2',
            bg='red',
            command=self.delete_btn,
            )
        self.del_btn.grid(row=6, column=0, sticky="NESW")

        self.save_btn = Button(
            self.win_edit,
            text='Save',
            bd='2',
            bg='gray',
            command=self.edit_btn,
            )
        self.save_btn.grid(row=6, column=1, sticky="NESW")

    def edit_btn(self):
        self.inv_conn.update_plant(
            id=int(self.id_store),
            name=self.name_entry.get(),
            desc=self.desc_entry.get('1.0', "end-1c"),
            stock=int(self.stock_entry.get()),
            temp=float(self.temp_entry.get()),
            hum=float(self.hum_entry.get())
        )

        self.win_edit.destroy()
        self.view_inv_refresh()

    def delete_btn(self):
        ans = tk.messagebox.askyesno(
            title='Warning!',
            message='Are you sure you wish to delete?',
            icon='warning'
            )

        if ans == 'yes':
            self.inv_conn.del_plant(
                id=self.id_store
            )
            self.win_edit.destroy()
            self.view_inv_refresh()
        else:
            self.win_edit.destroy()
            self.view_inv_refresh()

    def view_inventory(self):
        # Screen Settings/Geometry
        self.win_view = Toplevel(self.window)
        self.win_view.title("View Inventory")
        self.win_view.geometry('1060x360')
        self.win_view.resizable(False, False)
        
        self.columns = ('#1', '#2', '#3', '#4', '#5', '#6')

        self.tree = ttk.Treeview(self.win_view, columns=self.columns, show='headings', height=15)

        self.tree.heading('#1', text='ID')
        self.tree.column('#1', minwidth=30, width=60, anchor='center')
        self.tree.heading('#2', text='Name')
        self.tree.column('#2', minwidth=50, width=200, anchor='center')
        self.tree.heading('#3', text='DESC')
        self.tree.column('#3', minwidth=100, width=600)
        self.tree.heading('#4', text='Stock')
        self.tree.column('#4', minwidth=30, width=60, anchor='center')
        self.tree.heading('#5', text='Temp.')
        self.tree.column('#5', minwidth=30, width=60, anchor='center')
        self.tree.heading('#6', text='Humid.')
        self.tree.column('#6', minwidth=30, width=60, anchor='center')

        self.df = self.inv_conn.view_plants() # Grab current inventory
        self.df_index = self.df.index.tolist()

        self.data = []
        for n in self.df_index:
            self.data.append([n] + self.df.loc[n].tolist())

        # adding data to the treeview
        for j in self.data:
            self.tree.insert('', tk.END, values=j)

        # bind the select event
        def item_selected(event):
            select_data = self.tree.selection()
            select_data = self.tree.item(select_data)['values']
            self.edit_entry(select_data)

        self.tree.bind('<<TreeviewSelect>>', item_selected)

        self.tree.grid(row=1, column=0, sticky='nsew')

        # add a scrollbar
        self.scrollbar = ttk.Scrollbar(self.win_view, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=1, sticky='ns')

        self.btn = tk.Button(self.win_view, text='Random')
        self.btn.grid(row=0, sticky='nsew', columnspan=2)

    def view_inv_refresh(self):
        clean = self.tree.get_children()
        if clean != '()':
            for row in clean:
                self.tree.delete(row)

        self.df = self.inv_conn.view_plants() # Grab current inventory
        self.df_index = self.df.index.tolist()

        self.data = []
        for n in self.df_index:
            self.data.append([n] + self.df.loc[n].tolist())

        # adding data to the treeview
        for j in self.data:
            self.tree.insert('', tk.END, values=j)

    def current_report(self):
        # Screen Settings/Geometry
        win_report = Toplevel(self.window)
        win_report.title("Reports")
        win_report.geometry('300x300')
        win_report.resizable(False, False)

    def report_history(self):
        # Screen Settings/Geometry
        win_history = Toplevel(self.window)
        win_history.title("History")
        win_history.geometry('300x300')
        win_history.resizable(False, False)

    def critial_issues(self):
        # Screen Settings/Geometry
        win_crit = Toplevel(self.window)
        win_crit.title("Critial Issues")
        win_crit.geometry('300x300')
        win_crit.resizable(False, False)

    def settings(self):
        # Screen Settings/Geometry
        win_config = Toplevel(self.window)
        win_config.title("Configuration")
        win_config.geometry('300x300')
        win_config.resizable(False, False)


test = User_Interface()
test.main_window()