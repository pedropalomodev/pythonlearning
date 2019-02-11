#Quanto de tinta é necessario para pintar uma parede, sendo que cada litro de tinta pinta 2m²
l1 = float(input('Qual é a largura da parede: '))
l2 = float(input('Qual é a altura da parede: '))
tinta = l1*l2/2
print('Sera necessário {} litros de tinta'.format(tinta))
