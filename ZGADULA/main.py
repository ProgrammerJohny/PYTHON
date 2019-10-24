import random

"""if liczba ==x:
    print("Odgadłeś!")
else :
    print("Niestety nie tym razem... Wylosowana liczba to: ",x)
"""
def menu():
    print("1. Losowanie liczby w przedziale [0-5]")
    print("2. Losowanie liczby w przedziale [0-10]")
    print("3. Losowanie liczby w przedziale [5-10]")
    print("4. Losowanie liczby w przedziale [10-15]")
    print("5. Wyjście")


loop = True
while loop:
    menu()
    wybor = input("Wybierz opcję ")
    if wybor == '1':
        ####
        print("Losowanie przedziału od 0 do 5")
        x = random.randint(0,5)
        liczba = int(input("Podaj swoją liczbę "))
        if liczba ==  x:
            print("Brawo")
        else:
            print("Buuuu")
            print("Wylosowana liczba to ",x)
    elif wybor == '2':
        x = random.randint(0,10)
        liczba = int(input("Podaj swoją liczbę "))
        if liczba == x:
            print("Brawo")
        else:
            print("Buuuu")
            print("Wylosowana liczba to ",x)
        ###
    elif wybor == '3':
        ###
        x = random.randint(5,10)
        liczba = int(input("Podaj swoją liczbę "))
        if liczba == x:
            print("Brawo")
        else:
            print("Buuuu")
            print("Wylosowana liczba to ",x)
    elif wybor == '4':
        ###
        x = random.randint(10,15)
        liczba = int(input("Podaj swoją liczbę "))
        if liczba == x:
            print("Brawo")
        else:
            print("Buuuu")
            print("Wylosowana liczba to ",x)
    elif wybor =='5':
        loop=False
    else :
        print("Nie dokonano wyboru...")
