from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import matplotlib.pyplot as plt
import pandas


class User_Interface:
    def __init__(self):
        pass

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
        inv_create = Button(self.window,
                            text='Create Inventory Entry',
                            bd='2',
                            bg='gray',
                            command=self.create_entry,
                            height=btn_h,
                            width=btn_w
                            )
        inv_create.place(x=btn_x, y=70)

        inv_edit = Button(self.window,
                          text='Edit/Delete Inventory Entry',
                          bd='2',
                          bg='gray',
                          command=self.edit_entry,
                          height=btn_h,
                          width=btn_w
                          )
        inv_edit.place(x=btn_x, y=140)

        inv_view = Button(self.window,
                          text='View Inventory',
                          bd='2',
                          bg='gray',
                          command=self.view_inventory,
                          height=btn_h,
                          width=btn_w
                          )
        inv_view.place(x=btn_x, y=210)

        # Report Buttons
        report_current = Button(self.window,
                                text='Current Report',
                                bd='2',
                                bg='gray',
                                command=self.current_report,
                                height=btn_h,
                                width=btn_w
                                )
        report_current.place(x=btn_x, y=280)

        report_history = Button(self.window,
                                text='Report History',
                                bd='2',
                                bg='gray',
                                command=self.report_history,
                                height=btn_h,
                                width=btn_w
                                )
        report_history.place(x=btn_x, y=350)

        report_critical = Button(self.window,
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
        settings = Button(self.window,
                          text='Settings',
                          bd='2',
                          bg='gray',
                          command=self.settings,
                          height=1,
                          width=10
                          )
        settings.place(x=650, y=490)

        # Load CSV/Graphs | Needs to be Own Function
        curr_data = pandas.read_csv("code/data/demo_data.csv",
                                    delimiter=',',
                                    index_col=0,
                                    names=['Time', 'Temperature', 'Humidity']
                                    )

        # Graphic 1 | Temp
        figure1 = plt.Figure(figsize=(4, 5), dpi=100)
        ax1 = figure1.add_subplot(211)

        graphic_1 = FigureCanvasTkAgg(figure1, self.window)
        graphic_1.get_tk_widget().place(x=30, y=15)
        curr_data.plot(legend=True, y='Temperature', ax=ax1)
        ax1.set_title('Current Temperature')

        # Graphic 2 | Humidity
        ax2 = figure1.add_subplot(212)
        curr_data.plot(legend=True, y='Humidity', ax=ax2)
        ax2.set_title('Current Humidity')

        # Main Window Loop
        self.window.mainloop()

    def create_entry(self):
        # Screen Settings/Geometry
        win_create_entry = Toplevel(self.window)
        win_create_entry.title("Add Inventory Item")
        win_create_entry.geometry('300x300')
        win_create_entry.resizable(False, False)

    def edit_entry(self):
        # Screen Settings/Geometry
        win_edit = Toplevel(self.window)
        win_edit.title("Edit Inventory")
        win_edit.geometry('300x300')
        win_edit.resizable(False, False)

    def view_inventory(self):
        # Screen Settings/Geometry
        win_view = Toplevel(self.window)
        win_view.title("View Inventory")
        win_view.geometry('300x300')
        win_view.resizable(False, False)

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
