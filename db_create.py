# project/db_create.py

import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()
    # create the table
    c.execute('CREATE TABLE tasks( task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,'
              ' due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)')

    c.execute('insert into tasks(name, due_date, priority, status) values("finish the tutorial","03/25/2018",10,1)')
    c.execute('insert into tasks(name, due_date, priority, status) values("finish REAL Python2","04/28/2018",09,2)')
