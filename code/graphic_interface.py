# ##################################Imports################################## #
from tkinter import *
import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter import ttk

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

# import pandas | Remove?
from sys import exit

# Custom class imports
from database import *
from config import *
# ########################################################################### #


class User_Interface:
    def __init__(self):
        """
        User_Interface's purpose is to generate the Main/Slave UI elements
        and be on of the major classes that tie in a multitude of other classes
        to perform the necessary actions of the software.
        """
        # Declare Settings Obj & obtain Dataframe
        self.rd_conf = Settings()
        self.conf = self.rd_conf.export_conf()

        # Open Inventory DB Connection
        self.inv_conn = Database(
            user=self.conf['sql_login']['username'],
            password=self.conf['sql_login']['password'],
            host=self.conf['sql_login']['host'],
            port=self.conf['sql_login']['port'],
            database=self.conf['sql_login']['inventory_db']
            )
        self.inv_conn.connect()

        # Open Sensor DB Connection
        self.sen_conn = Database(
            user=self.conf['sql_login']['username'],
            password=self.conf['sql_login']['password'],
            host=self.conf['sql_login']['host'],
            port=self.conf['sql_login']['port'],
            database=self.conf['sql_login']['sensor_db']
            )
        self.sen_conn.connect()

    def main_window(self):
        """
        Generate Tkinter window object and populates the frame
        with necessary widgets, labels, etc...
        """

        # Window Obj & Settings
        self.window = Tk()
        self.window.title("Greenhouse Management (Beta)")
        self.window.geometry('850x510')
        self.window.resizable(True, False)
        self.window.minsize(850, 510)
        self.window.columnconfigure(0, weight=1)

        # Window Icon & Screen Centering
        self.icon = PhotoImage(file='code/Leaf-256.png')
        self.window.iconphoto(False, self.icon)
        self.window.eval('tk::PlaceWindow . center')

        # Button Height & Width
        btn_h = 2
        btn_w = 25

        """User Interface Buttons & Settings"""
        # Create Inventory Entry Button
        inv_create = Button(
            self.window,
            text='Create Inventory Entry',
            bd='2',
            bg='gray',
            command=self.create_entry,
            height=btn_h,
            width=btn_w
        )
        inv_create.grid(row=0, column=1, sticky='EW', padx=10)

        # Modify/Edit Inventory Button
        inv_edit = Button(
            self.window,
            text='Edit/Delete Inventory Entry',
            bd='2',
            bg='gray',
            command=self.edit_entry,
            height=btn_h,
            width=btn_w
        )
        inv_edit.grid(row=1, column=1, sticky='EW', padx=10)

        # View Inventory Button
        inv_view = Button(
            self.window,
            text='View Inventory',
            bd='2',
            bg='gray',
            command=self.view_inventory,
            height=btn_h,
            width=btn_w
        )
        inv_view.grid(row=2, column=1, sticky='EW', padx=10)

        # Current Report & Issues Button
        report_current = Button(
            self.window,
            text='Current Report',
            bd='2',
            bg='gray',
            command=self.current_report,
            height=btn_h,
            width=btn_w
        )
        report_current.grid(row=3, column=1, sticky='EW', padx=10)

        # Past Report & Issues Button
        report_history = Button(
            self.window,
            text='Report History',
            bd='2',
            bg='gray',
            command=self.report_history,
            height=btn_h,
            width=btn_w
            )
        report_history.grid(row=4, column=1, sticky='EW', padx=10)

        # Current Problems Button
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
        report_critical.grid(row=5, column=1, sticky='EW', padx=10)

        # Settings/Configuration Button
        settings = Button(
            self.window,
            text='Settings',
            bd='2',
            bg='gray',
            command=self.settings,
            height=1,
            width=10
            )
        settings.grid(row=6, column=1, sticky='EW', padx=10)

        def graph_refresh(ignore=None):
            """
            Function that gets called to grab most recent Sensor Data from
            Sensor DB and re-plot/re-render defined graphs

            Args:
                ignore ([N/A], optional): [description]. Defaults to None.
            """
            del self.curr_data
            self.curr_data = self.sen_conn.grab_sensor()

            self.curr_data.plot(legend=None, y='temperature', ax=self.ax1)
            self.curr_data.plot(legend=None, y='humidity', ax=self.ax2)

        # Init Sensor Data
        self.curr_data = self.sen_conn.grab_sensor()

        # Create Figure with 1x2 plot
        self.figure = plt.Figure(figsize=(10, 5), dpi=100)
        self.figure.subplots_adjust(
            left=0.1,
            bottom=0.1,
            right=0.9,
            top=0.9,
            wspace=0.8,
            hspace=0.8
        )

        # Graph Widget integration into Tkinter
        graphs = FigureCanvasTkAgg(self.figure, self.window)
        graphs.get_tk_widget().grid(
            row=0,
            column=0,
            rowspan=7,
            sticky='NESW',
            padx=10
            )

        # Plot both graphs and their appropriate settings
        self.ax1 = self.figure.add_subplot(211)
        self.curr_data.plot(legend=None, y='temperature', ax=self.ax1)
        self.ax1.set_title('Current Temperature')
        self.ax2 = self.figure.add_subplot(212)
        self.curr_data.plot(legend=None, y='humidity', ax=self.ax2)
        self.ax2.set_title('Current Humidity')

        # Calls Animation Function to refresh/re-render graphs/plots
        ani = animation.FuncAnimation(
            self.figure,
            func=graph_refresh,
            interval=self.conf['interval']
            )

        # Main Window Loop
        self.window.mainloop()

    def create_entry(self):
        """
        Creates slave UI from main Window Object that allows for the
        creation of new inventory entries into the DB via the software.
        """
        # Screen Settings/Geometry
        self.win_create_entry = Toplevel(self.window)
        self.win_create_entry.title("Add Inventory Item")
        self.win_create_entry.geometry('400x350')
        self.win_create_entry.iconphoto(False, self.icon)
        self.win_create_entry.minsize(400, 350)
        self.win_create_entry.maxsize(600, 350)
        self.win_create_entry.columnconfigure(0, weight=1)
        self.win_create_entry.columnconfigure(1, weight=4)

        # Labels & Entries
        self.name_label = Label(self.win_create_entry, text='Name')
        self.name_label.grid(column=0, row=0, sticky="NESW")
        self.name_entry = Entry(
            self.win_create_entry,
            bg='White',
            fg='Black'
            )
        self.name_entry.grid(column=1, row=0, sticky="EW")

        self.desc_label = Label(self.win_create_entry, text='Description')
        self.desc_label.grid(column=0, row=1)
        self.desc_entry = Text(
            self.win_create_entry,
            height=10,
            width=10,
            bg='White',
            fg='Black'
            )
        self.desc_entry.grid(column=1, row=1, sticky='NESW')

        self.stock_label = Label(self.win_create_entry, text='Stock')
        self.stock_label.grid(column=0, row=2)
        self.stock_entry = Entry(
            self.win_create_entry,
            bg='White',
            fg='Black',
            justify='center',
            width=5
            )
        self.stock_entry.grid(column=1, row=2, sticky='W')

        self.temp_label = Label(self.win_create_entry, text='Temperature')
        self.temp_label.grid(column=0, row=3)
        self.temp_entry = Entry(
            self.win_create_entry,
            bg='White',
            fg='Black',
            justify='center',
            width=5
            )
        self.temp_entry.grid(column=1, row=3, sticky='W')

        self.hum_label = Label(self.win_create_entry, text='Humidity')
        self.hum_label.grid(column=0, row=4)
        self.hum_entry = Entry(
            self.win_create_entry,
            bg='White',
            fg='Black',
            justify='center',
            width=5
            )
        self.hum_entry.grid(column=1, row=4, sticky='W')

        # Save Button & it's tie-in Function
        self.save_btn = Button(
            self.win_create_entry,
            text='Save',
            bd='2',
            bg='gray',
            command=self.create_inv_btn,
            )
        self.save_btn.grid(row=5, columnspan=2, sticky="NESW")

    def create_inv_btn(self):
        """
        Function to grab input entries and pass them on SQL query
        to create a new inventory entry.
        """
        self.inv_conn.new_plant(
            name=self.name_entry.get(),
            desc=self.desc_entry.get('1.0', 'end-1c'),
            stock=int(self.stock_entry.get()),
            temp=float(self.temp_entry.get()),
            hum=float(self.hum_entry.get())
        )
        self.win_create_entry.destroy()

    def edit_entry(self, list_data=None):
        """
        Creates slave UI instance upon clicking a tree-bind which
        auto-populates entries with current data and can be
        modified to one's whim and subsequently saved or deleted
        from the inventory DB.
        Args:
            list_data ([list]): Contains ID, name, etc. of "x" plant
        """
        # Store ID of Selected Plant
        self.id_store = list_data[0]

        # Screen Settings/Geometry
        self.win_edit = Toplevel(self.window)
        self.win_edit.title("Edit Inventory Item")
        self.win_edit.geometry('400x360')
        self.win_edit.iconphoto(False, self.icon)
        self.win_edit.minsize(400, 360)
        self.win_edit.maxsize(600, 350)

        self.win_edit.columnconfigure(0, weight=1)
        self.win_edit.columnconfigure(1, weight=4)

        self.id_label = Label(self.win_edit, text='ID')
        self.id_label.grid(column=0, row=0, sticky="NESW")
        self.id_entry = Label(
            self.win_edit,
            bg='White', fg='Black',
            text=str(list_data[0])
            )
        self.id_entry.grid(column=1, row=0, sticky="EW")

        self.name_label = Label(self.win_edit, text='Name')
        self.name_label.grid(column=0, row=1, sticky="NESW")
        self.name_entry = Entry(
            self.win_edit,
            bg='White',
            fg='Black'
            )
        self.name_entry.insert('0', list_data[1])
        self.name_entry.grid(column=1, row=1, sticky="EW")

        self.desc_label = Label(self.win_edit, text='Description')
        self.desc_label.grid(column=0, row=2)
        self.desc_entry = Text(
            self.win_edit,
            height=10,
            width=10,
            bg='White',
            fg='Black'
            )
        self.desc_entry.insert('1.0', list_data[2])
        self.desc_entry.grid(column=1, row=2, sticky='NESW')

        self.stock_label = Label(self.win_edit, text='Stock')
        self.stock_label.grid(column=0, row=3)
        self.stock_entry = Entry(
            self.win_edit,
            bg='White',
            fg='Black',
            justify='center',
            width=5
            )
        self.stock_entry.insert('0', list_data[3])
        self.stock_entry.grid(column=1, row=3, sticky='W')

        self.temp_label = Label(self.win_edit, text='Temperature')
        self.temp_label.grid(column=0, row=4)
        self.temp_entry = Entry(
            self.win_edit,
            bg='White',
            fg='Black',
            justify='center',
            width=5
            )
        self.temp_entry.insert('0', list_data[4])
        self.temp_entry.grid(column=1, row=4, sticky='W')

        self.hum_label = Label(self.win_edit, text='Humidity')
        self.hum_label.grid(column=0, row=5)
        self.hum_entry = Entry(
            self.win_edit,
            bg='White',
            fg='Black',
            justify='center',
            width=5
            )
        self.hum_entry.insert('0', list_data[5])
        self.hum_entry.grid(column=1, row=5, sticky='W')

        # Delete & Save Buttons
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
        """
        Function that grabs current input entries and ID then submits
        query to inventory DB to update entry via unique ID.
        """
        self.inv_conn.update_plant(
            id=int(self.id_store),
            name=self.name_entry.get(),
            desc=self.desc_entry.get('1.0', "end-1c"),
            stock=int(self.stock_entry.get()),
            temp=float(self.temp_entry.get()),
            hum=float(self.hum_entry.get())
        )

        # Destory Window instant and Update Tabular view
        self.win_edit.destroy()
        self.view_inv_refresh()

    def delete_btn(self):
        """
        Ask for confirmation to delete entry & delete entry within inventory DB
        via Query function and refresh Tabular view.
        """
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
        """
        Generate's window that displays current inventory found at Inventory DB
        and binds each entry to a function to modify said entry.
        """
        # Screen Settings/Geometry
        self.win_view = Toplevel(self.window)
        self.win_view.title("View Inventory")
        self.win_view.geometry('1060x360')
        self.win_view.iconphoto(False, self.icon)
        self.win_view.resizable(False, False)

        self.columns = ('#1', '#2', '#3', '#4', '#5', '#6')

        # Decalre Tree Object/Widget
        self.tree = ttk.Treeview(
            self.win_view,
            columns=self.columns,
            show='headings',
            height=15
            )

        # Declare Columns with appropriate names
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

        # Obtain current Inventory
        self.df = self.inv_conn.view_plants()
        self.df_index = self.df.index.tolist()

        # Add Data to empty List
        self.data = []
        for n in self.df_index:
            self.data.append([n] + self.df.loc[n].tolist())

        # Iterate & Add data to Tree
        for j in self.data:
            self.tree.insert('', tk.END, values=j)

        # Bind Entries to Function
        def item_selected(event):
            select_data = self.tree.selection()
            select_data = self.tree.item(select_data)['values']
            self.edit_entry(select_data)

        self.tree.bind('<<TreeviewSelect>>', item_selected)
        self.tree.grid(row=1, column=0, sticky='nsew')

        # Initialize Scrollbar Widget
        self.scrollbar = ttk.Scrollbar(
            self.win_view,
            orient=tk.VERTICAL,
            command=self.tree.yview
            )
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=1, sticky='ns')

        # Current Placeholder Button
        self.search_ent = tk.Entry(
            self.win_view,
            bg='White',
            fg='black'
            )
        self.search_ent.grid(row=0, sticky='nsew', columnspan=2)

        def check(event):
            if self.search_ent.get() == '':
                print('Nothing Here')
            else:
                print(self.search_ent.get())

        self.search_ent.bind("<KeyRelease>", check)

    def view_inv_refresh(self):
        """
        Cleans out Local copy of DB and grabs most recent version from
        Inventory DB to be displayed.
        """
        # Remove all previous Inventory Data
        clean = self.tree.get_children()
        if clean != '()':
            for row in clean:
                self.tree.delete(row)

        # Grab Inventory from Inventory DB
        self.df = self.inv_conn.view_plants()
        self.df_index = self.df.index.tolist()

        self.data = []
        for n in self.df_index:
            self.data.append([n] + self.df.loc[n].tolist())

        # Add Data to Tree
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
        """
        Generates slave UI for settings configuration without having to
        directly modify the json file.
        """
        # Screen Settings/Geometry
        self.win_config = Toplevel(self.window)
        self.win_config.title("Configuration")
        self.win_config.geometry('300x300')
        self.win_config.iconphoto(False, self.icon)
        self.win_config.resizable(False, False)

        self.win_config.columnconfigure(0, weight=1)
        self.win_config.columnconfigure(1, weight=4)

        # Labels, Entries & Buttons
        self.int_label = Label(self.win_config, text="Refresh Interval")
        self.int_label.grid(column=0, row=0, sticky="NESW")
        self.int_entry = Entry(
            self.win_config,
            bg='White',
            fg='Black',
            justify='center'
            )
        self.int_entry.insert('0', self.conf['interval'])
        self.int_entry.grid(column=1, row=0, sticky="EW")

        self.user_label = Label(self.win_config, text="Username")
        self.user_label.grid(column=0, row=2, sticky="NESW")
        self.user_entry = Entry(
            self.win_config,
            bg='White',
            fg='Black',
            justify='center'
            )
        self.user_entry.insert('0', self.conf['sql_login']['username'])
        self.user_entry.grid(column=1, row=2, sticky="EW")

        self.pass_label = Label(self.win_config, text="Password")
        self.pass_label.grid(column=0, row=3, sticky="NESW")
        self.pass_entry = Entry(
            self.win_config,
            bg='White',
            fg='Black',
            show='*',
            justify='center'
            )
        self.pass_entry.insert('0', self.conf['sql_login']['password'])
        self.pass_entry.grid(column=1, row=3, sticky="EW")

        self.host_label = Label(self.win_config, text="Host")
        self.host_label.grid(column=0, row=4, sticky="NESW")
        self.host_entry = Entry(
            self.win_config,
            bg='White',
            fg='Black',
            justify='center'
            )
        self.host_entry.insert('0', self.conf['sql_login']['host'])
        self.host_entry.grid(column=1, row=4, sticky="EW")

        self.port_label = Label(self.win_config, text="Port")
        self.port_label.grid(column=0, row=5, sticky="NESW")
        self.port_entry = Entry(
            self.win_config,
            bg='White',
            fg='Black',
            justify='center'
            )
        self.port_entry.insert('0', self.conf['sql_login']['port'])
        self.port_entry.grid(column=1, row=5, sticky="EW")

        self.inv_db_label = Label(self.win_config, text="Inventory DB")
        self.inv_db_label.grid(column=0, row=6, sticky="NESW")
        self.inv_db_entry = Entry(
            self.win_config,
            bg='White',
            fg='Black',
            justify='center'
            )
        self.inv_db_entry.insert('0', self.conf['sql_login']['inventory_db'])
        self.inv_db_entry.grid(column=1, row=6, sticky="EW")

        self.sensor_db_label = Label(self.win_config, text="Sensor DB")
        self.sensor_db_label.grid(column=0, row=7, sticky="NESW")
        self.sensor_db_entry = Entry(
            self.win_config,
            bg='White',
            fg='Black',
            justify='center'
            )
        self.sensor_db_entry.insert('0', self.conf['sql_login']['sensor_db'])
        self.sensor_db_entry.grid(column=1, row=7, sticky="EW")

        self.adv_btn = Button(
            self.win_config,
            text='Advanced Options',
            bd='2',
            bg='gray',
            command=self.win_config.destroy,
        )
        self.adv_btn.grid(row=8, column=0, sticky="NESW", columnspan=2)

        self.save_conf_btn = Button(
            self.win_config,
            text='Save',
            bd='2',
            bg='gray',
            command=self.settings_save_btn,
        )
        self.save_conf_btn.grid(row=9, column=0, sticky="NESW", columnspan=2)

    def settings_save_btn(self):
        """
        Grab current entry inputs and pass to saving function
        to get formated into json and close out the program to force
        changes.
        """
        iter = self.int_entry.get()
        user = self.user_entry.get()
        pwd = self.pass_entry.get()
        host = self.host_entry.get()
        port = self.port_entry.get()
        inv_db = self.inv_db_entry.get()
        sen_db = self.sensor_db_entry.get()

        self.rd_conf.save_settings(
            iter,
            user,
            pwd,
            host,
            port,
            inv_db,
            sen_db
        )

        self.win_config.destroy()
        sys.exit()


test = User_Interface()
test.main_window()
