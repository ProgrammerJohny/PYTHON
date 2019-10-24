from time import sleep
liczba = int(input("Podaj liczbę w zakresie 0 - 10 "))
if liczba >=0 and liczba <= 10:
    print("Liczba mieści się w żądanym zakresie, jest to ",liczba)
    sleep(1)
elif liczba >0 or  liczba < 10:
    print("Liczba jest poza zakresem, jest to ",liczba)
    sleep(1)
