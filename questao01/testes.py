from dados import carregarDados, salvarDados
from buscaNome import buscaNome
from buscaYearGender import buscaYearGender
from retornaValores import retornaValores
from retornaId import retornaId
from novoRegistro import novoRegistro

dados, quantidade = buscaNome('murilo')

print('Carregando os dados\n')
print(carregarDados())
print('\nSalvando os dados\n')
print(salvarDados(carregarDados()))
print('\nBusca por nomes\n')
print(f'\n{dados}, Quantidade:{quantidade}\n')
print(f'\nBusca ano e sexo: {buscaYearGender(2002, "M")}\n')
print(retornaValores('Mu'))
print(f'\nIds:{retornaId(3465)}\n')
print(f'Novo registro: {novoRegistro(2004, "F", "Pandora", "23456")}')

