# Ler Largura
larg = float(input('Largura da Parede?'))
# ler Altura
alt= float(input('Altura da Parede?'))
area = (larg * alt)
Tinta = (area /2)
# 1 litro de tinta pinta 2 metros quad
print('Sua parede tem a dimensao de {}x{}, e sua area é de m2'.format(larg,alt))
print('Para pintar a parede voce ira precisar de {}l de tinta'.format(Tinta))