try:
    from Tkinter import *
except ImportError:
    from tkinter import *
    from tkinter import messagebox
    import sql


def get_selected_row(event):
    global selected_tuple
    index = INCI_list.curselection()[0]
    selected_tuple = INCI_list.get(index)
    E1.delete(0, END)
    E1.insert(END, selected_tuple[0])
    E2.delete(0, END)
    E2.insert(END, selected_tuple[1])


def search_command():
    INCI_list.delete(0, END)
    for row in sql.search(INCI_text.get(), CAS_text.get()):
        INCI_list.insert(row, END)


master = Tk()

L1 = Label(master, text='INCI Name')
L1.grid(row=1, column=0)

L2 = Label(master, text='CAS No')
L2.grid(row=2, column=0)

INCI_text = StringVar()
E1 = Entry(master, textvariable=INCI_text)
E1.grid(row=1, column=1)

CAS_text = StringVar()
E2 = Entry(master, textvariable=CAS_text)
E2.grid(row=2, column=1)

CAS_list = Listbox(master, height=10, width=50)
CAS_list.grid(row=1, column=3, rowspan=3, columnspan=2)

INCI_list = Listbox(master, height=10, width=50)
INCI_list.grid(row=4, column=3, rowspan=3, columnspan=2)

scrl = Scrollbar(master)
scrl.grid(row=1, column=2, sticky='ns', rowspan=6)

INCI_list.bind('<<ListboxSelect>>', get_selected_row)

INCI_list.configure(yscrollcommand=scrl.set)
scrl.configure(command=INCI_list.yview)

B1 = Button(master, text='Search', width=12, command=search_command)
B1.grid(row=3, column=0, columnspan=2)

master.mainloop()
