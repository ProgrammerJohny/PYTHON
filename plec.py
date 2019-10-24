name = input("Podaj swoje imię : ")
name = name.capitalize()
if name[:] == 'Kuba':
    print("Twoje imię to :", name)
    print("Jesteś mężczyzną")
elif name[-1] =='a':
    
    print("Twoje imię to ",name)
    print("Jesteś kobietą")
else:
    print("Twoje imię to: ",name)
    print("Jesteś mężczyzną")
