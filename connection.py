import sqlite3

conn =  sqlite3.connect('tutorial.db')
c =  conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuff (unix REAL, datastamp TEXT, keyword TEXT, value REAL)')
def data_entry():
    c.execute("INSERT INTO stuff VALUES (14523, '2016-01-01', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()



create_table()
data_entry()