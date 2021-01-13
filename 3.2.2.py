var=input("Escribe un texto \n")
palabras=0
if var!="":
	palabras=1
for i in range(0,len(var)):
	if i < len(var)-2 and var[i]==" " and var[i+1]!=" " and var[i+2]!=" ":
		palabras=palabras+1

print(palabras)