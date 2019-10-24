name = input("Podaj swoe imię : ")
name = name.capitalize()
print("Witaj  w naszym sklepie",format(name))
age = int(input("Ile masz lat? "))

if age < 18:
        print("Nie możesz kupować u nas alkoholu. Przykro mi")            
else:
    print("Możesz kupić u nas alkohol")
    def menu_alkohol():
            print(30 * "+", "MENU",30*"+")
            print("1. Piwo Rodzaj 1")
            print("2. Piwo Rodzaj 2")
            print("3. Wódka Rodzaj 1 ")
            print("4. Wódka Rodzaj 2 ")
            print("5.Whiskey Rodzaj 1")
            print("6.Whiskey Rodzaj 2")
            print("7.Wino Rodzaj 1")
            print("8.Wino Rodzaj 2")
            print("9. Koniec zakupów")
            print(67* "+")

    loop=True
    while loop:
        menu_alkohol()
        wybor = input("Co chcesz kupić?[opcja 1-9]")

        if wybor == '1':
                loop=False

                print("Wybrane piwo to Żywiec. Smacznego! ")
              
        
        elif wybor == '2':
            print("Wybrane piwo to EB. Smacznego!")
            loop=False
        elif wybor == '3':
            print("Wybrana wódka to Żubrówka. Smacznego!")
            loop=False
        elif wybor == '4':
            print("Wybrana wódka to Żołądkowa. Smacznego!")
        elif wybor == '5':
            print("Wybrane whiskey to Bourbon. Smacznego!")
            loop=False
        elif wybor == '6':
            print("Wybrane whiskey to Jack Daniels. Smacznego!")
            loop=False
        elif wybor == '7':
            print("Wybrane wino to Karafka. Smacznego!")
            loop=False
        elif wybor == '8':
            print("Wybrane wino to Pinot Noir. Smacznego!")
            loop=False
        elif wybor =='9':
            print("Dziękujemy za zakupy")
            loop=False
        else:
            print("Nieprawidłowy wybór. Wybierz jeszcze raz")
