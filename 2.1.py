echo=int(input("Quants cops repeteix l'eco?\n"))

while True:
	word=input("\nQuè vols dir?:\n")
	if word == "adeu" or word == "Adeu" or word == "ADEU":
		print("\nAdéu! TInguis un bon dia!")
		break
	else:
		word=word+" "
		print(str(word)*echo)
