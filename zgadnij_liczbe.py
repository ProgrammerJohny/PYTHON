from time import sleep
sleep(0.5)
print("Witaj w programie 'Zgadnij liczbę'\nDo wyboru 3 poziomy trundości. Zaczynajmy")
def menu():
	print("1. Zgadnij liczbę w 4 podejściach")
	print("2. Zgadnij liczbę w 3 podejściach")
	print("3. Zgadnij liczbę w 2 podejściach")
	print("4. Koniec")
loop = True
while loop:
	menu()
	wybor = input("Wybierz na klawiaturzę cyfrę od 1 do 3 aby wybrać poziom trudności. ")
	if wybor == '1':
		print("Masz  4 podejścia. Powodzenia")
		sleep(0.5)
		szukanaLiczba = 40
		zgadywanaLiczba = 0
		i = 0

		while(zgadywanaLiczba != szukanaLiczba):
			zgadywanaLiczba = int(input("Odgadnij liczbę"))
			if(zgadywanaLiczba == szukanaLiczba):
				print("Brawo!!")
			else:
				print("Spróbuj jeszcze raz")
				
	elif wybor == '2':
		print("Masz  3 podejścia. Powodzenia")
		sleep(0.5)
		szukanaLiczba = 40
		zgadywanaLiczba = 0
		i = 0
		while(zgadywanaLiczba != szukanaLiczba) in range(3):
			zgadywanaLiczba = int(input("Odgadnij liczbę"))
			if(zgadywanaLiczba == szukanaLiczba):
				print("Brawo!!")
				print("Liczba prób ",i)
				break
			else:
				print("Spróbuj jeszcze raz")
				i-=1
	elif wybor == '3':
		print("Masz  2 podejścia. Powodzenia")
		sleep(0.5)
		szukanaLiczba = 40
		zgadywanaLiczba = 0
		i = 0
		while(zgadywanaLiczba != szukanaLiczba) in range(2):
			zgadywanaLiczba = int(input("Odgadnij liczbę"))
			if(zgadywanaLiczba == szukanaLiczba):
				print("Brawo!!")
				print("Liczba prób ",i)
				break
			else:
				print("Spróbuj jeszcze raz")
				i-=1
	elif wybor == '4':
		print("Dzięki ;)")
		break
	else:
		print("Nie wybrano żadnej opcji")
"""""szukanaLiczba = 10
zgadywanaLiczba = 0
i = 1
while zgadywanaLiczba !=szukanaLiczba:
	zgadywanaLiczba = int(input("Odgadnij liczbę\n"))
	if(zgadywanaLiczba == szukanaLiczba):
		print("Brawo")
		print("Liczba prób ",i)
	else:
		print("Spróbuj jeszcze raz")
		print(" to była Próba nr ",i)
		if(zgadywanaLiczba > szukanaLiczba):
			print("Podałeś za dużą liczbę")
		else:
			print("Podałeś za małą liczbę")
		i+=1
"""
