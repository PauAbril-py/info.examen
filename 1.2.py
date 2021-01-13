import random, os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

while True:
	a=int(input('escull el teu lluitador\n\t1) Son Goku\n\t2) Jakie Chun\n\t3) 	Krilin\n\t4) Tenshinhan\n'))

	if a == 1:
		aa=random.randint(80,90)
	elif a == 2:
		aa=random.randint(50,80)
	elif a == 3:
		aa=random.randint(20,50)
	elif a == 4:
		aa=random.randint(40,70)

	b=random.randint(0,80)

	print('\nLluites amb una força de',aa)

	print('\nMr Satan lluita amb una força de',b)

	if aa > b:
		print('\nGUANYES!!!!')
	elif aa < b:
		print('\nPERDS!!!!')
	elif aa == b:
		print('\nEMPATES!!!!')

	input('\nEnter per a continuar')

	cls()