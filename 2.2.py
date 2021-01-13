while True:
	temp=int(input("Quina temperatura fa?:\n"))
	if temp<=30 and temp>=-10:
		break

if temp<0:
	print("Has de portar roba polar")
if temp>=0 and temp<=9:
	print("Has de portar guants i bufanda")
if temp>=10 and temp<=19:
	print("Has de portar maniga curta")
if temp>=20:
	print("Has de portar banyador")