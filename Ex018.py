# ler o angulo e mostra o valor
import math
Angulo = float(input('Digite o valor do Angulo: '))

# seno
seno = math.sin(Angulo)
# cosseno
cosseno = math.cos(Angulo)
# tangente
tangente = math.tan(Angulo)

print('O valor do Seno é: {}'.format(seno, math.ceil(seno)))
print('O valor do Cosseno é: {}'.format(cosseno, math.ceil(cosseno)))
print('O valor da Tangente é: {}'.format(tangente, math.ceil(tangente)))
