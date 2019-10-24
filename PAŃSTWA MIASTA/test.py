import random
from slowniki import *
from time import sleep
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Państwa Masta")
letter_choise = random.choice(letter)
#panstwo_random = random.choice(panstwo)
#miasto_random =  random.choice(miasto)
#rzecz_random = random.choice(rzecz)

print("Wylosowana litera to ",letter_choise)
panstwo_choice = input("Podaj panstwo na podaną literę ").capitalize()

if panstwo_choice[0] == letter_choise:
	print("Twoje państwo to ", panstwo_choice)
else:
	print("Nie ta litera")
miasto_choice = input("Podaj miasto na podaną literę ").capitalize()
if miasto_choice[0] == letter_choise:
	print("Twoje miasto to ", miasto_choice)
else:
	print("Nie ta litera")
rzecz_choice = input("Podaj rzecz na podaną literę ").capitalize()
if rzecz_choice[0] == letter_choise:
	print("Twoja rzecz to ",rzecz_choice)
else:
	print("Nie ta litera");
sleep(0.5)
print("Tura komputera")
if letter_choise == 'A':
	print("Państwo wybrane przez komputer",random.choice(panstwo_A))
	print("Miasto wybrane przez komputer",random.choice(miasto_A))
	print(random.choice(rzecz_A))
elif letter_choise =='B':
	print("Państwo wybrane przez komputer",random.choice(panstwo_B))
	print("Miasto wybrane przez komputer",random.choice(miasto_B))
	print(random.choice(rzecz_B))
elif letter_choise =='C':
	print("Państwo wybrane przez komputer",random.choice(panstwo_C))
	print("Miasto wybrane przez komputer",random.choice(miasto_C))
	print(random.choice(rzecz_C))
elif letter_choise == 'D':
	print("Państwo wybrane przez komputer",random.choice(panstwo_D))
	print("Miasto wybrane przez komputer",random.choice(miasto_D))
	print(random.choice(rzecz_D))
elif letter_choise =='E':
	print("Państwo wybrane przez komputer",random.choice(panstwo_E))
	print("Miasto wybrane przez komputer",random.choice(miasto_E))
	print(random.choice(rzecz_E))
elif letter_choise == 'F':
	print("Państwo wybrane przez komputer",random.choice(panstwo_F))
	print("Miasto wybrane przez komputer",random.choice(miasto_F))
	print(random.choice(rzecz_F))
elif letter_choise == 'G':
	print("Państwo wybrane przez komputer",random.choice(panstwo_G))
	print("Miasto wybrane przez komputer",random.choice(miasto_G))
	print(random.choice(rzecz_G))
elif letter_choise == 'H':
	print("Miasto wybrane przez komputer",random.choice(panstwo_H))
	print(random.choice(miasto_H))
	print(random.choice(rzecz_H))
elif letter_choise == 'I':
	print("Miasto wybrane przez komputer",random.choice(panstwo_I))
	print(random.choice(miasto_I))
	print(random.choice(rzecz_I))
elif letter_choise == 'J':
	print("Miasto wybrane przez komputer",random.choice(panstwo_J))
	print(random.choice(miasto_J))
	print(random.choice(rzecz_J))
elif letter_choise == 'K':
	print("Miasto wybrane przez komputer",random.choice(panstwo_K))
	print(random.choice(miasto_K))
	print(random.choice(rzecz_K))
elif letter_choise == 'L':
	print("Miasto wybrane przez komputer",random.choice(panstwo_L))
	print(random.choice(miasto_L))
	print(random.choice(rzecz_L))
elif letter_choise =='M':
	print("Miasto wybrane przez komputer",random.choice(panstwo_M))
	print(random.choice(miasto_M))
	print(random.choice(rzecz_M))
elif letter_choise == 'N':
	print("Miasto wybrane przez komputer",random.choice(panstwo_N))
	print(random.choice(miasto_N))
	print(random.choice(rzecz_N))
elif letter_choise == 'O':
	print("Miasto wybrane przez komputer",random.choice(panstwo_O))
	print(random.choice(miasto_O))
	print(random.choice(rzecz_O))
elif letter_choise =='P':
	print("Miasto wybrane przez komputer",random.choice(panstwo_P))
	print(random.choice(miasto_P))
	print(random.choice(rzecz_P))
elif letter_choise =='R':
	print("Miasto wybrane przez komputer",random.choice(panstwo_R))
	print(random.choice(miasto_R))
	print(random.choice(rzecz_R))
elif letter_choise =='S':
	print("Miasto wybrane przez komputer",random.choice(panstwo_S))
	print(random.choice(miasto_S))
	print(random.choice(rzecz_S))
elif letter_choise =='T':
	print("Miasto wybrane przez komputer",random.choice(panstwo_T))
	print(random.choice(miasto_T))
	print(random.choice(rzecz_T))
elif letter_choise =='U':
	print("Miasto wybrane przez komputer",random.choice(panstwo_U))
	print(random.choice(miasto_U))
	print(random.choice(rzecz_U))
elif letter_choise =='V':
	print("Miasto wybrane przez komputer",random.choice(panstwo_V))
	print(random.choice(miasto_V))
	print(random.choice(rzecz_V))	
elif letter_choise =='W':
	print("Miasto wybrane przez komputer",random.choice(panstwo_W))
	print(random.choice(miasto_W))
	print(random.choice(rzecz_W))
elif letter_choise =='Y':
	print('Brak państwa na Y')
	print(random.choice(miasto_Y))
	print(random.choice(rzecz_Y))
elif letter_choise =='Z':
	print("Miasto wybrane przez komputer",random.choice(panstwo_Z))
	print(random.choice(miasto_Z))
	print(random.choice(rzecz_Z))

sleep(3)
