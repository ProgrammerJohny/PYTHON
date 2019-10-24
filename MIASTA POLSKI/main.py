#main.py main file of program
import mysql_connector
import ctypes
import sys
ctypes.windll.kernel32.SetConsoleTitleW("Miasta w Polsce")

def menu():
	print(30*"+","MENU",30*"+")
	print("1.Wyświetl wszystkie miasta")
	print("2.Wyświetl informacje o danym mieście")
	print("3.Dodaj nowe miasto")
	print("4.Edytuj dane miasta")
	print("5.Usuń miasto")
	print("6.KONIEC")
	print(67*"+")
loop=True
while loop:
	menu()
	choice = input("Którą opcję wybierasz [1-6] ")
	if choice == '1':
		print("Wybrałeś opcję numer 1 -> Wyświetl wszystkie miasta")
	elif choice == '2':
		print("Wybrałeś opcję numer 2 -> Wyświetl informacje o danym mieście")
	elif choice == '3':
		print("Wybrałeś opcję numer 3 -> Dodaj nowe miasto")
	elif choice == '4':
		print("Wybrałeś opcję numer 4 -> Edytuj dane miasto")
	elif choice == '5':
		print("Wybrałeś opcję numer 5 -> Usuń miasto ")
	elif choice == '6':
		print("Dziękujemy za skorzystanie  programu")
		sys.exit(0)
	else:
		print("Nie została wybrana żadna opcja. Spróbuj jeszcze raz")
		
