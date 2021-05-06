import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


root = tk.Tk()
root.title('Treeview demo')
root.geometry('1060x360')

# columns
columns = ('#1', '#2', '#3', '#4', '#5', '#6')

tree = ttk.Treeview(root, columns=columns, show='headings', height=15) #DEFAULT 10

# define headings
tree.heading('#1', text='ID')
tree.column('#1', minwidth=30, width=60, anchor='center')
tree.heading('#2', text='Name')
tree.column('#2', minwidth=50, width=200, anchor='center')
tree.heading('#3', text='DESC')
tree.column('#3', minwidth=100, width=600)
tree.heading('#4', text='Stock')
tree.column('#4', minwidth=30, width=60, anchor='center')
tree.heading('#5', text='Temp.')
tree.column('#5', minwidth=30, width=60, anchor='center')
tree.heading('#6', text='Humid.')
tree.column('#6', minwidth=30, width=60, anchor='center')

# generate sample data
contacts = []
for n in range(1, 200):
    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

# adding data to the treeview
for contact in contacts:
    tree.insert('', tk.END, values=contact)


# bind the select event
def item_selected(event):
    for selected_item in tree.selection():
        # dictionary
        item = tree.item(selected_item)
        # list
        record = item['values']
        #
        showinfo(title='Information',
                message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=1, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=1, sticky='ns')


btn = tk.Button(root, text='Random')
btn.grid(row=0, sticky='nsew', columnspan=2)

# run the app
root.mainloop()