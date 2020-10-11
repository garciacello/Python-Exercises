dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos km Rodados?'))

# R$ 60 por dia ; # R$0.15 por km rodado.
valor = (dias * 60) + (km * 0.15)

print('O total a pagar é de R$ {:.2f}'.format(valor))
