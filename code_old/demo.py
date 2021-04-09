from tkinter import *
import matplotlib
import pandas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Main Window Generation


def main_window():
    # Main Window Settings
    window = Tk()
    window.title("Greenhouse Mangement (Development)")
    window.geometry('810x540')
    window.resizable(False, False)

    # Screen Centering
    win_wid = 810
    win_hei = 540

    x_left = int(window.winfo_screenwidth()/2 - win_wid/2)
    y_top = int(window.winfo_screenheight()/2 - win_hei/2)

    window.geometry("+{}+{}".format(x_left, y_top))

    # Button Size
    btn_h = 2
    btn_w = 35

    btn_x = 450

    # Inventory Buttons
    inv_create = Button(window,
                        text='Create Inventory Entry',
                        bd='2',
                        bg='gray',
                        command=window.destroy,
                        height=btn_h,
                        width=btn_w
                        )
    inv_create.place(x=btn_x, y=70)

    inv_edit = Button(window,
                      text='Edit/Delete Inventory Entry',
                      bd='2',
                      bg='gray',
                      command=window.destroy,
                      height=btn_h,
                      width=btn_w
                      )
    inv_edit.place(x=btn_x, y=140)

    inv_view = Button(window,
                      text='View Inventory',
                      bd='2',
                      bg='gray',
                      command=window.destroy,
                      height=btn_h,
                      width=btn_w
                      )
    inv_view.place(x=btn_x, y=210)

    # Report Buttons
    report_current = Button(window,
                            text='Current Report',
                            bd='2',
                            bg='gray',
                            command=window.destroy,
                            height=btn_h,
                            width=btn_w
                            )
    report_current.place(x=btn_x, y=280)

    report_history = Button(window,
                            text='Report History',
                            bd='2',
                            bg='gray',
                            command=window.destroy,
                            height=btn_h,
                            width=btn_w
                            )
    report_history.place(x=btn_x, y=350)

    report_critical = Button(window,
                             text='Critical Issues',
                             bd='2',
                             bg='gray',
                             command=window.destroy,
                             height=btn_h,
                             width=btn_w,
                             fg='red'
                             )
    report_critical.place(x=btn_x, y=420)

    # Settings Button
    settings = Button(window,
                      text='Settings',
                      bd='2',
                      bg='gray',
                      command=window.destroy,
                      height=1,
                      width=10
                      )
    settings.place(x=650, y=490)

    # Load CSV/Graphs | Needs to be Own Function
    curr_data = pandas.read_csv("~/Documents/GitHub/capstone-project-Cortesj/code/data/demo_data.csv",
                                delimiter=',',
                                index_col=0,
                                names=['Time', 'Temperature', 'Humidity']
                                )

    # Graphic 1 | Temp
    figure1 = plt.Figure(figsize=(4, 5), dpi=100)
    ax1 = figure1.add_subplot(211)

    graphic_1 = FigureCanvasTkAgg(figure1, window)
    graphic_1.get_tk_widget().place(x=30, y=15)
    curr_data.plot(legend=True, y='Temperature', ax=ax1)
    ax1.set_title('Current Temperature')

    # Graphic 2 | Humidity
    ax2 = figure1.add_subplot(212)
    curr_data.plot(legend=True, y='Humidity', ax=ax2)
    ax2.set_title('Current Humidity')

    # Main Window Loop
    window.mainloop()


def main():
    main_window()


if __name__ == "__main__":
    main()
