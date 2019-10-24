Jabłka = {
  "Kraj pochodzenia" : "Polska",
  "Cena" : 4
}
Gruszki = {
  "Kraj pochodzenia" : "Polska",
  "Cena" : 4.6
}
Ziemniaki = {
  "Kraj pochodzenia" : "Niemcy",
  "Cena" : 3
}

Produkty = {
  "Jabłka" : Jabłka,
  "Gruszki" : Gruszki,
  "Ziemniaki" : Ziemniaki
}

print(Produkty)
for x in Produkty.items():
    print(x)

def zakupy():
        print(30*"+","CENNIK",30*"+")
        print("1.Jabłka")
        print("2.Gruszki")
        print("3.Ziemniaki")
loop=True
while loop:
    zakupy()
    wybor = input("Który z tych produktów wybierasz?")

    if wybor == '1':
            print("Jabłka")
            print(Jabłka)
    elif wybor =='2':
            print("Gruszki")
            print(Gruszki)
    elif wybor == '3':
            print("Ziemniaki")
            print(Ziemniaki)
    else:
            print("Nie dokonano wyboru")
            loop=False
