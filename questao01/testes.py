from dados import carregarDados, salvarDados
from buscaNome import buscaNome
from buscaYearGender import buscaYearGender

dados, quantidade = buscaNome('murilo')

print('Carregando os dados\n')
print(carregarDados())
print('\nSalvando os dados\n')
print(salvarDados(carregarDados()))
print('\nBusca por nomes\n')
print(f'{dados}, Quantidade:{quantidade}')
print(buscaYearGender(2002, 'M'))