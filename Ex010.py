# quanto em dinheiro
real=float(input('Quanto dinheiro voce tem na carteira? '))
# converter em dolar 1 / 3.27
dolar = real / 3.27
print('Com R$ {:.2f}, voce pode comprar US$ {:.2f} Dólares'. format(real,dolar))