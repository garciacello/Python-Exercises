print('Tabela do Brasileirão 2020 - CLASSIFICACAO: ')
times = ('Atletico Mineiro', 'Internacional', 'São Paulo', 'Palmeiras', 'Vasco',
         'Flamengo', 'Fluminense', 'Sport', 'Santos', 'Fortaleza', 'Athletico-PR',
         'Ceará', 'Atlético-GO','Grêmio', 'Corinthians', 'Coritiba', 'Bragantino',
         'Botafogo', 'Goiás', 'Bahia')
# Times:
#print(times)
# os 5 primeiros
print('Os 5 primeiros Times são: ',times[:5])

# 4 ultimos
print('Os 4 ultimos são: ', times[-4:])

# ordem alfabetica
print(sorted(times))

# Coritiba esta:
print('O Coritiba está na:', times.index('Coritiba'),'ªposicão')
