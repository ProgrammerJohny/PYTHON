i = 0
wynik = 0
for i in range(3):
	liczba = int(input("Podaj liczbę parzystą "))
	if liczba %2 ==0:
		print("Podana liczba jest parzysta")
		wynik+=liczba
		#print(wynik)
		
	else:
		print("Podana liczba nie jest parzysta")
		break
print("wynik to ",wynik)
