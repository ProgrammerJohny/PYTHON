from time import sleep
name = input("Wprowadź swoje imię : ")
Name = name.capitalize()
print("Witaj ",format(Name))
a = int(input("Podaj liczbę a : "))
b = int(input("Podaj liczbę b : "))
mnozenie = a*b
dzielenie = a/b
dodawanie = a + b
odejmowanie = a-b
## Text menu in Python

def print_menu():       
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Mnożenie")
    print ("2. Dzielenie")
    print ("3. Dodawanie")
    print ("4. Odejmowanie")
    print ("5. Koniec")
    print (67 * "-")
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
     
    if choice== '1' :     
        print ("Wybrane działanie to mnożenie")
        print ("Wynik działania ->",mnozenie)
        #loop=False
        ## You can add your code or functions here
    elif choice== '2':
        if b == 0:
            print("cholero nie dziel przez zero !!")
        else:
            print ("Wybrane działanie to dzielenie")
            print ("Wynik działania ->",dzielenie)
        ## You can add your code or functions here
    elif choice== '3' :
        print ("Wybrane działanie to dodawanie")
        print("Wynik działania ->",dodawanie)
        ## You can add your code or functions here
    elif choice== '4' :
        print ("Wybrane działanie to odejmowanie")
        print("Wynik działania ->",odejmowanie)
        ## You can add your code or functions here
    elif choice== '5' :
        print ("Dziękujemy za korzystanie z programu")
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Wrong option selection. Enter any key to try again..")
