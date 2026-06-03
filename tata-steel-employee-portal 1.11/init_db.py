import sqlite3
c=sqlite3.connect('employees.db')
c.executescript(open('schema.sql').read())
c.commit(); c.close()
print('Database Created Successfully')
