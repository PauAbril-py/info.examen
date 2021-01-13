import random
while True:
	a=random.randint(1,9)

	b=random.randint(1,9)

	x=float(input(str(a)+"x+"+str(b)+"=0\tQuant val la x?\n"))
	if a*x+b >= -0.5 and a*x+b <= 0.5:
		print("Felicitats. Ets humà! Ho has encertat.")
		break
	else:
		print("Oooh ets un bot. Tornar a intentar-ho")