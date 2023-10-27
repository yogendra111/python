import mysql.connector as mycon

mydb = mycon.connect(
    host="localhost",
    user="myuser",
    password="mypassword"
    # database="pythondb"  # optional
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)