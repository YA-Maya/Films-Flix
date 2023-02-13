import MySQLconnects

# connect to mysql server

conn= MySQLconnects.connect(
    host="localhost", database="filmflix.db", user="root", _Password="pass"
)

if conn.is_connected():
    print("Connected to MySQL")
else:
        print("Connection failed!")

Cursor = conn.cursor(prepared=True) 
