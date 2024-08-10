import main
from tkinter import *
from tkinter import ttk


app = Tk()
app.title("Static Change")
app.geometry("500x350")

content = ttk.Frame(app)

interfaces = ["Item 1A", "Item 1B", "Item 1C"]
configs = ["Item 2A", "Item 2B", "Item 2C"]

# setting lists as tk.StringVar for use in tk.Listbox
ifaces_as_stringvar = StringVar()
configs_as_stringvar = StringVar()
ifaces_as_stringvar.set(interfaces)
configs_as_stringvar.set(configs)

def run ():
    interface_selection = interfaces_listbox.curselection()[0]
    config_selection = configs_listbox.curselection()[0]
    interface = interfaces[interface_selection]
    config = configs[config_selection]
    print(interface, config)


interfaces_listbox = Listbox(content,exportselection=False,listvariable=ifaces_as_stringvar, selectmode=SINGLE)
configs_listbox = Listbox(content, exportselection=False, listvariable=configs_as_stringvar, selectmode=SINGLE)
execute_button = Button(content, text="Change IP", command=run)


content.grid(column=0, row=0)
Label(content, text="Static Change").grid(column=0, row=0)
interfaces_listbox.grid(column=0, row=1)
configs_listbox.grid(column=1, row=1)

execute_button.grid(column=0, row=2)


# interfaces_listbox.pack(side="left")
# configs_listbox.pack(side="right")
# execute_button.pack(side="bottom")

app.mainloop()
