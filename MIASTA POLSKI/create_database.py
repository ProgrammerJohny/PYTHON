import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database = "miasta_polskie"
)
mycursor = mydb.cursor()



mycursor = mydb.cursor()
sql = "INSERT INTO miasta(id_miasta,miasto,powiat,woj,populacja,obszar) VALUES(%s,%s,%s,%s,%s,%s)"
val = [
("1","Warszawa","powiat Warszawa","mazowieckie","1 769 529","517,2 km2"),
("2","Kraków","powiat Kraków","małopolskie","769 498","326,9 km2"),
("3","Łódź","powiat Łódź","łódzkie","687 702","293,3 km2"),
("4","Wrocław","powiat Wrocław","dolnośląskie","639 258","292,8 km2"),
("5","Poznań","powiat Poznań","wielkopolskie","537 643","261,9 km2"),
("6","Gdańsk","powiat Gdańsk","pomorskie","464 829","262 km2"),
("7","Szczecin","powiat Szczecin","zachodniopomorskie","403 274","300,6 km2"),
("8","Bydgoszcz","powiat Bydgoszcz","kujawsko-pomorskie","351 254","176 km2"),
("9","Lublin","powiat Lublin","lubelskie","339 811","147,5 km2"),
("10","Białystok","powiat Białystok","podlaskie","297 403","102,1 km2"),
("11","Katowice","powiat Katowice","śląskie","295 449","164,6 km2"),
("12","Gdynia","powiat Gdynia",,,),
("13",,,,,),
("14",,,,,),
("15",,,,,),
("16",,,,,),
("17",,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,),
(,,,,,)
] 
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")