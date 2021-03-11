# In this Work:
# Install PyODBC library
# Connect to SQL Server
# Basic database operations: Create, Read, Update and Delete.

import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};" 
    "Server=DESKTOP-DBM1R4E;"
    "Database=Demo_DB_for_PYTHON;"
    "Trusted_Connection=yes;")

def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from SUBJECTS")
    for row in cursor:
        print(f'row = {row}')
    print()
        
def create(conn):
    print("Create")
    cursor = conn.cursor()
    cursor.execute('insert into SUBJECTS (ID, NAME, HOURS, SEMESTER) values (?,?,?,?);', (8,"Python",150,2))
    conn.commit()
    read(conn)

def update(conn):
    print("Update")
    cursor = conn.cursor()
    cursor.execute ('update SUBJECTS set NAME = ? where ID = ?;',('SQL',8))
    conn.commit()
    read(conn)

def delete(conn):
    print("Delete")
    cursor = conn.cursor()
    cursor.execute('delete from SUBJECTS where ID = 8')
    conn.commit()
    read(conn)

read(conn)
create(conn)
update(conn)
delete(conn)

conn.close()

##########################################################
## Shortcode to check opening process
# cursor = conn.cursor ()
# mySQLQuery = ("select * from SUBJECTS ;")
# cursor.execute (mySQLQuery)
# results = cursor.fetchall()
# print (results)
