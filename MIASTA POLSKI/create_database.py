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
("12","Gdynia","powiat Gdynia","pomorskie","246 204","135,1 km2"),
("13","Częstochowa","powiat Częstochowa","śląskie","223 322","159,7 km2"),
("14","Radom","powiat Radom","mazowieckie","213 910","111,8 km2"),
("15","Sosnowiec","powiat Sosnowiec","śląskie","203 094","91,1 km2"),
("16","Toruń","powiat Toruń","kujawsko-pomorskie","202 482","115,7 km2"),
("17","Kielce","powiat Kielce","świętokrzyskie","196 335","109,7 km2"),
("18","Rzeszów","powiat Rzeszów","podkarpackie","190 849","120,4 km2"),
("19","Gliwice","powiat Gliwice","śląskie","180 708","133,9 km2"),
("20","Zabrze","powiat Zabrze","śląskie","173 784","80,4 km2"),
("21","Olsztyn","powiat Olsztyn","warmińsko-mazurskie","173 125","88,3 km2"),
("22","Bielsko-Biała","powiat Bielsko-Biała","śląskie","171 277","124,5 km2"),
("23","Bytom","powiat Bytom","śląskie","167 762","69,4 km2")
("24","Zielona Góra","powiat Zielona Góra","lubuskie","140 113","278,3 km2"),
("25","Rybnik","powiat Rybnik","śląskie","138 919","148,4 km2"),

] 
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
