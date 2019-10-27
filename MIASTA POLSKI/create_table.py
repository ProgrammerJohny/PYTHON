import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database = "miasta_polskie"
)
mycursor = mydb.cursor()

sql = "INSERT INTO miasta(id_miasta,miasto,powiat,woj,populacja,obszar) VALUES(%s, %s, %s, %s, %s, %s)"
val = [
(1,"Warszawa","powiat Warszawa","mazowieckie","1 769 529","517,2 km2"),
(2,"Kraków","powiat Kraków","małopolskie","769 498","326,9 km2"),
(3,"Łódź","powiat Łódź","łódzkie","687 702","293,3 km2"),
(4,"Wrocław","powiat Wrocław","dolnośląskie","639 258","292,8 km2"),
(5,"Poznań","powiat Poznań","wielkopolskie","537 643","261,9 km2"),
(6,"Gdańsk","powiat Gdańsk","pomorskie","464 829","262 km2"),
(7,"Szczecin","powiat Szczecin","zachodniopomorskie","403 274","300,6 km2"),
(8,"Bydgoszcz","powiat Bydgoszcz","kujawsko-pomorskie","351 254","176 km2"),
(9,"Lublin","powiat Lublin","lubelskie","339 811","147,5 km2"),
(10,"Białystok","powiat Białystok","podlaskie","297 403","102,1 km2"),
(11,"Katowice","powiat Katowice","śląskie","295 449","164,6 km2"),
(12,"Gdynia","powiat Gdynia","pomorskie","246 204","135,1 km2"),
(13,"Częstochowa","powiat Częstochowa","śląskie","223 322","159,7 km2"),
(14,"Radom","powiat Radom","mazowieckie","213 910","111,8 km2"),
(15,"Sosnowiec","powiat Sosnowiec","śląskie","203 094","91,1 km2"),
(16,"Toruń","powiat Toruń","kujawsko-pomorskie","202 482","115,7 km2"),
(17,"Kielce","powiat Kielce","świętokrzyskie","196 335","109,7 km2"),
(18,"Rzeszów","powiat Rzeszów","podkarpackie","190 849","120,4 km2"),
(19,"Gliwice","powiat Gliwice","śląskie","180 708","133,9 km2"),
(20,"Zabrze","powiat Zabrze","śląskie","173 784","80,4 km2"),
(21,"Olsztyn","powiat Olsztyn","warmińsko-mazurskie","173 125","88,3 km2"),
(22,"Bielsko-Biała","powiat Bielsko-Biała","śląskie","171 277","124,5 km2"),
(23,"Bytom","powiat Bytom","śląskie","167 762","69,4 km2"),
(24,"Zielona Góra","powiat Zielona Góra","lubuskie","140 113","278,3 km2"),
(25,"Rybnik","powiat Rybnik","śląskie","138 919","148,4 km2"),
(26,"Ruda Śląska","powiat Ruda Śląska","śląskie","138 215","77,7 km2"),
(27,"Opole","powiat Opole","opolskie","128 224","149,9 km2"),
(28,"Tychy","powiat Tychy","śląskie","128 049","81,8 km2"),
(29,"Gorzów Wielkopolski","powiat Gorzów Wielkopolski","lubuskie","124 177","85,7 km2"),
(30,"Dąbrowa Górnicza","powiat Dąbrowa Górnicza","śląskie","120 777","188,7 km2"),
(31,"Elbląg","powiat Elbląg","warmińsko-mazurskie","120 568","79,8 km2"),
(32,"Płock","powiat Płock","mazowieckie","120 403","88 km2"),
(33,"Wałbrzych","powiat Wałbrzych","dolnośląskie","113 100","84,7 km2"),
(34,"Włocławek","powiat Włocławek","kujawsko-pomorskie","111 319","84,3 km2"),
(35,"Tarnów","powiat Tarnów","małopolskie","109 358","72,4 km2"),
(36,"Chorzów","powiat Chorzów","śląskie","108 668","33,2 km2"),
(37,"Koszalin","powiat Koszalin","zachodniopomorskie","107 692","98,3 km2"),
(38,"Kalisz","powiat Kalisz","wielkopolskie","101 279","69,4 km2"),
(39,"Legnica","powiat Legnica","dolnośląskie","100 081","56,3 km2"),
(40,"Grudziądz","powiat Grudziądz","kujawsko-pomorskie","95 354","57,8 km2"),
(41,"Jaworzno","powiat Jaworzno","śląskie","91 758","152,6 km2"),
(42,"Słupsk","powiat Słupsk","pomorskie","91 225","43,2 km2"),
(43,"Jastrzębie-Zdrój","powiat Jastrzębie-Zdrój","śląskie","89 353","85,3 km2"),
(44,"Nowy Sącz","powiat Nowy Sącz","małopolskie","83 958","57,6 km2"),
(45,"Jelenia Góra","powiat Jelenia Góra","dolnośląskie","79 686","109,2 km2"),
(46,"Siedlce","powiat Siedlce","mazowieckie","77 732","31,9 km2"),
(47,"Mysłowice","powiat Mysłowice","śląskie","74 578 ","65,6 km2"),
(48,"Konin","powiat Konin","wielkopolskie","74 472","82,2 km2"),
(49,"Piotrków Trybunalski","powiat Piotrków Trybunalski","łódzkie","74 004","67,2 km2"),
(50,"Piła","powiat pilski","wielkopolskie","73 693","102,7 km2")
] 
mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount, " cities was inserted.")
mycursor.execute("SELECT * FROM miasta")
selected_miasta = mycursor.fetchall()
for x in selected_miasta:
	print(x)

mycursor.execute("CREATE TABLE woj(id_woj INT AUTO_INCREMENT PRIMARY KEY,woj VARCHAR(100))")
sql = "INSERT INTO woj(id_woj,woj) VALUES(%s,%s)"
val = [
(1,"dolnośląskie"),
(2,"kujawsko-pomorskie"),
(3,"lubelskie"),
(4,"łódzkie"),
(5,"lubuskie"),
(6,"małopolskie"),
(7,"mazowieckie"),
(8,"opolskie"),
(9,"podkarpackie"),
(10,"podlaskie"),
(11,"pomorskie"),
(12,"śląskie"),
(13,"świętokrzyskie"),
(14,"warmińsko-mazurskie"),
(15,"wielkopolskie"),
(16,"zachodniopomorskie")

]
mycursor.executemany(sql,val)
mydb.commit()

print(mycursor.rowcount," provinces was inserted")
mycursor.execute("SELECT * FROM woj")
selected_woj = mycursor.fetchall()
for x in selected_woj:
	print(x)
