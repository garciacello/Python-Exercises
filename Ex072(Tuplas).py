cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez')

while True:
   núm= int(input('Digite um numero  entre 0 e 10: '))
   if 0 <= núm <=10:
      break
      print('Tente novamente. ', end=' ')
print(f'voce digitou o numero {cont[núm]}')