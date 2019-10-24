from time import sleep
from math import *

import sys
print("Witaj w programie 'system dwójkowy'!")
def menu():
    print(30* "|","MENU",30*"|")
    print("1. Zamiana liczby z systemu dziesiętnego na dwójkowy")
    print("2. Zamiana liczby z systemu dwójkowego na dziesiętny")
    print("3.KONIEC")
    print(67*"|")

loop = True
while loop:
    menu()
    wybor = input("Którą opcję wybierasz? ")
    if wybor == '1':
    
        print("Postaram się podaną przez Ciebie liczbę zapisać w systemie dwójkowym")
        liczba = int(input("Podaj liczbę : "))
        print("Twoja liczba to ",liczba)
        print("Liczbę dzielimy przez 2...")
        sleep(1)
        print(liczba/2)
        reszta = (liczba%2)
        print("Reszta z dzielenia to ", reszta)
        resztaList = []
        while liczba >0:
            reszta = liczba%2
            liczba //= 2
            print("Twoja liczba to ",liczba, "\n Reszta z dzielenia  to ",reszta)
            resztaList.append(reszta)
        resztaList.reverse()
        print(resztaList)
        print("Pamiętaj aby liczyć od lewej do prawej")
        sleep(0.5)

    elif wybor =='2':
        liczba = input("Podaj liczbę w systemie dwójkowym, a ja zamienię ją na dziesietną ")     
        x = int(liczba,2)
        print("Liczba dziesiętna wynosi ",x)
        sleep(0.5)
    elif wybor =='3':
        print("Dziękujemy za skorzystanie z programu")
        loop=False
    else:
        print("Nie wybrałeś prawidłowej opcji")
        sys.exit(0)

