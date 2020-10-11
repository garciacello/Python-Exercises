from math import hypot
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))

# hipotenusa  a2 + b2 = c2
hi = hypot(co, ca)

print('o valor da hipotenusa é {:.2f}'.format(hi))
#hi = (co ** 2 + ca **2) ** (1/2)
#print('o valor da hipotenusa é {:.2f}'.format(hi))

