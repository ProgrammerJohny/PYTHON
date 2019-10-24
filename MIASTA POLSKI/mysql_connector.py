import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="Webmaster2017"
)

print(mydb)
