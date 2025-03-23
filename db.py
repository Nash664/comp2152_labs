import sqlite3

db_connection = sqlite3.connect("sqlite.db")
print(db_connection)

db_cursor = db_connection.cursor()

query1= "SELECT * FROM demo"
db_cursor.execute(query1)

row= db_cursor.fetchone()
print(row)

rows= db_cursor.fetchall()
for r in rows:
    print(r)

query2= "INSERT INTO demo (Name, Hint) VALUES ('John', 'Murphy')"
db_cursor.execute(query2)