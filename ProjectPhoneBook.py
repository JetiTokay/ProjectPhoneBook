from tkinter import *
from tkinter import ttk

# color them
co0 = "#ffffff"
co1 = "#000000"
co2 = "#4456F0"

# window of app
Main_window = Tk()
Main_window.title("NEW WINDOW")
Main_window.geometry('485x450')
Main_window.configure(background=co0)
Main_window.resizable(width=FALSE, height=FALSE)

# frames
frame_up = Frame(Main_window, width=500, height=50, bg=co2)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(Main_window, width=500, height=150, bg=co0)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(width=500, height=100, bg=co2)
frame_table.grid(row=2, column=0, columnspan=2, padx=0, pady=1, sticky=NW)

# frames_up widgets
app_name = Label(frame_up, text="Phone Book Hoe", height=1, font=('Verdana 17 bold'), bg=co2, fg=co0)
app_name.place(x=5, y=5)

# frame_down widgets
l_name = Label(frame_down, text="Name *", width=20, height=1, highlightthickness=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_name.place(x=10, y=20)
e_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_name.place(x=80, y=20)

l_gender = Label(frame_down, text="Gender *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_gender.place(x=10, y=50)
c_gender = ttk.Combobox(frame_down, width=27,)
c_gender['values'] = ['', 'F', 'M']
c_gender.place(x=80, y=50)

l_telephone = Label(frame_down, text="Telephone *", height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_telephone.place(x=10, y=80)
l_telephone = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
l_telephone.place(x=80, y=80)

l_email = Label(frame_down, text="Email *", height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_email.place(x=10, y=110)
l_email = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
l_email.place(x=80, y=110)

b_search = Button(frame_down, text="search", height=1, bg=co2, fg=co0, font=('Ivy 8 bold'))
b_search.place(x=290, y=20)
e_search = Entry(frame_down, width=16, justify='left', font=('Ivy', 11), highlightthickness=1, relief="solid")
e_search.place(x=347, y=20)

b_view = Button(frame_down, text="View", width=10, height=1, bg=co2, fg=co0, font=('Ivy 8 bold'))
b_view.place(x=290, y=50)

b_add = Button(frame_down, text="Add", width=10, height=1, bg=co2, fg=co0, font=('Ivy 8 bold'), command=lambda: add_contact())
b_add.place(x=400, y=50)

b_update = Button(frame_down, text="Update", width=10, height=1, bg=co2, fg=co0, font=('Ivy 8 bold'))
b_update.place(x=400, y=80)

b_delete = Button(frame_down, text="Delete", width=10, height=1, bg=co2, fg=co0, font=('Ivy 8 bold'))
b_delete.place(x=400, y=110)

# function to show the data in the treeview
def show():
    global tree

    listheader = ['Name', 'Gender', 'Telephone', 'Email']

    tree = ttk.Treeview(frame_table, selectmode="extended", columns=listheader, show="headings")

    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    # tree head
    tree.heading(0, text='Name', anchor=NW)
    tree.heading(1, text='Gender', anchor=NW)
    tree.heading(2, text='Telephone', anchor=NW)
    tree.heading(3, text='Email', anchor=NW)

    # tree columns
    tree.column(0, width=120, anchor='nw')
    tree.column(1, width=50, anchor='nw')
    tree.column(2, width=100, anchor='nw')
    tree.column(3, width=180, anchor='nw')

# function to add a contact to the treeview
def add_contact():
    name = e_name.get()
    gender = c_gender.get()
    telephone = l_telephone.get()
    email = l_email.get()

    if name and gender and telephone and email:  # ensure all fields are filled
        tree.insert('', 'end', values=(name, gender, telephone, email))
        clear_fields()  # clear the fields after adding
    else:
        print("Please fill in all fields.")

# function to clear the input fields after adding
def clear_fields():
    e_name.delete(0, END)
    c_gender.set('')
    l_telephone.delete(0, END)
    l_email.delete(0, END)

show()

Main_window.mainloop()
