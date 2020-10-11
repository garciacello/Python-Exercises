preco= float(input('Qual o preco do produto? R$'))
novo=preco - (preco * 5 / 100)
print('O preco do produto é R${:.2f}, e com o desconto será: {:.2f}'.format(preco,novo))