dias = float(input('Quantos dias você ficou com essa joça? '))
km = float(input('Quantos km vc rodo essa merda ai? '))
dias = dias * 60
km = km * 0.15
print('Voce devera pagar R${:.2f}'.format(dias + km))