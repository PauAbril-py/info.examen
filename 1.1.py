mides = input('Escriu la llargada, amplada i alçada de la caixa separades amb un espai\n\t').split()

llarg = int(mides[0])
amplada = int(mides[1])
alcada = int(mides[2])

b = min(amplada * llarg, llarg * alcada, amplada * alcada)

cm2=2 * llarg * amplada + 2 * amplada * alcada + 2 * alcada * llarg + b
print('necessitaras',cm2,'centimetres cuadrats de paper')