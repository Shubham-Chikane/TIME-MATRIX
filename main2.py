import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os, sys
sys.path.insert(0, 'windows/')
# import timetable_stud
# import timetable_fac
import sqlite3

conn = sqlite3.connect(r'files/timetable.db')
sql_query = """SELECT name FROM sqlite_master
    WHERE type='table';"""

cursor = conn.cursor()
cursor.execute(sql_query)
print("List of tables\n")
print(cursor.fetchall())
'''q1="de from schedule;"
cursor.execute(q1)
names = list(map(lambda x: x[0], cursor.description))
print(names)
print(cursor.fetchall())

q1="update SCHEDULE set SECTION='TE-I' where SECTION='H';"
cursor.execute(q1)
conn.commit()
print(cursor.fetchall())'''


q2="select * from SCHEDULE;"
cursor.execute(q2)
conn.commit()
print(cursor.fetchall())

