#FUNCOES DA BIBLIOTECA MATH
# ceil = > arredonda pra cima
# floor => arredonda pra baixo
# trunc => tira as casas decimais em excesso
# pow => potencia
# sqrt = >raiz quadrada
# factorial => fatorial
#import math => Importa toda a biblioteca
# from math import sqrt => importo apenas uma funcao

from math import sqrt,floor
num= int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))