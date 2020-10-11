salario = float(input('Qual o seu salário atual? R$: '))
# Aumento de 15%
novo = salario + (salario * 15/100)
print('Um funcionario que ganhava R${:.2f}. e recebe 15% de aumento, passa a receber R$ {:.2f}'.format(salario,novo))