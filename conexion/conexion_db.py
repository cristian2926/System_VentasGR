from __future__ import print_function
from sqlite3 import connect

# Replace username with your own A2 Hosting account username:
class conn:
    def conexion(self):
        conn = connect('../data/tabla.db')
    
        return conn
"""
curs.execute("CREATE TABLE employees (firstname varchar(32), lastname varchar(32), title varchar(32));")
curs.execute("INSERT INTO employees VALUES('Kelly', 'Koe', 'Engineer');")
conn.commit()

curs.execute("SELECT firstname, lastname FROM employees;")
for firstname, lastname in curs.fetchall():
    print(firstname, lastname)

conn.close()"""