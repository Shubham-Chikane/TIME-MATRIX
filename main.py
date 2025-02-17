import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os, sys
sys.path.insert(0, 'windows/')
import timetable_stud
import timetable_fac
import sqlite3

def challenge():
    conn = sqlite3.connect(r'files/timetable.db')
    #elif user == "Admin":
    if id_entry.get() == 'admin' and passw_entry.get() == 'admin':
        m.destroy()
        os.system('py windows\\admin_screen.py')
            # sys.exit()
    else:
            messagebox.showerror('Bad Input', 'Incorret Username/Password!')
            


m = tk.Tk()

m.geometry('400x430')
m.title('Welcome')

tk.Label(
    m,
    text='TIMETABLE MANAGEMENT SYSTEM',
    font=('Consolas', 20, 'bold'),
    wrap=400
).pack(pady=20)

tk.Label(
    m,
    text='Welcome!\nLogin to continue',
    font=('Consolas', 12, 'italic')
).pack(pady=10)

tk.Label(
    m,
    text='Username',
    font=('Consolas', 15)
).pack()

id_entry = tk.Entry(
    m,
    font=('Consolas', 12),
    width=21
)
id_entry.pack()

# Label5
tk.Label(
    m,
    text='Password:',
    font=('Consolas', 15)
).pack()

# toggles between show/hide password
def show_passw():
    if passw_entry['show'] == "●":
        passw_entry['show'] = ""
        B1_show['text'] = '●'
        B1_show.update()
    elif passw_entry['show'] == "":
        passw_entry['show'] = "●"
        B1_show['text'] = '○'
        B1_show.update()
    passw_entry.update()

pass_entry_f = tk.Frame()
pass_entry_f.pack()
# Entry2
passw_entry = tk.Entry(
    pass_entry_f,
    font=('Consolas', 12),
    width=15,
    show="●"
)
passw_entry.pack(side=tk.LEFT)

B1_show = tk.Button(
    pass_entry_f,
    text='○',
    font=('Consolas', 12, 'bold'),
    command=show_passw,
    padx=5
)
B1_show.pack(side=tk.LEFT, padx=15)

'''combo1 = ttk.Combobox(
    m,
    values=['Student', 'Faculty', 'Admin']
)
combo1.pack(pady=15)
combo1.current(0)'''

tk.Button(
    m,
    text='Login',
    font=('Consolas', 12, 'bold'),
    padx=30,
    command=challenge
).pack(pady=10)

m.mainloop()