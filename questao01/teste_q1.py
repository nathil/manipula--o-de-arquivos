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
print(f'\nBusca ano e sexo: {buscaYearGender(2004, "F")}\n')
print(f'\nBusca ano e sexo: {buscaYearGender(1000, "F")}\n')
print(f'\nBusca ano e sexo: {buscaYearGender(2023, "M")}\n')
print(f'\nBusca ano e sexo: {buscaYearGender(3600, "F")}\n')
print(f'\nBusca ano e sexo: {buscaYearGender(gender="F")}\n')
print(f'\nBusca ano e sexo: {buscaYearGender(1000)}\n')
print(f'\nBusca ano e sexo: {buscaYearGender()}\n')
print(retornaValores('Mu'))
print(retornaValores('th'))
print(retornaValores('an'))
print(retornaValores('dora'))
print(retornaValores('é'))
print(retornaValores())
print(retornaValores(12))
print(retornaValores(''))
print(f'\nIds:{retornaId(3465)}\n')
print(f'\nIds:{retornaId(123456)}\n')
print(f'\nIds:{retornaId(3465)}\n')
print(f'\nIds:{retornaId(50028422)}\n')
print(f'\nIds:{retornaId(23456)}\n')
print(f'\nIds:{retornaId()}\n')
print(f'\nIds:{retornaId('')}\n')
print(f'\nIds:{retornaId(0)}\n')
print(f'Novo registro: {novoRegistro(2004, "F", "Pandora", "23456")}')
print(f'Novo registro: {novoRegistro(2001, "M", "Rodrigo", "21913")}')
print(f'Novo registro: {novoRegistro(1980, "M", "Ricardo Britto", "980234")}')
print(f'Novo registro: {novoRegistro(1956, "F", "Maria", "123435")}')
print(f'Novo registro: {novoRegistro(2000, "F", "Antônia", "1135456")}')
print(f'Novo registro: {novoRegistro(2003, "M", 245684)}')
print(f'Novo registro: {novoRegistro(1990,"Bruna")}')
print(f'Novo registro: {novoRegistro("M", "Fernando", "1232131")}')

