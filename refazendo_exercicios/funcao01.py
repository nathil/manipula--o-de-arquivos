# A função deve eliminar da lista de carga todos os registros que possuem código de carga válido. Essa função
# deve ser programada utilizando somente comprehensions e deve retornar a lista resultante. 
import re

lista_cargas = [
                {'codigo': 'AOa123', 'tipo': '', 'tamanho': '', 'validade': '', 'quantidade': ''}
                ,{'codigo': 'AOa123', 'tipo': '', 'tamanho': '', 'validade': '', 'quantidade': ''}
                ,{'codigo': 'AOab23', 'tipo': '', 'tamanho': '', 'validade': '', 'quantidade': ''}
                ,{'codigo': 'oOa123', 'tipo': '', 'tamanho': '', 'validade': '', 'quantidade': ''}
                ] 

# def deletar_codigo_invalido(lista_cargas : list) -> list:
#     nova_lista = [] 
#     for carga in lista_cargas: 
#         if bool(re.fullmatch(r'[AEIOU]{2}.{1}[0-9]{3}', carga['codigo'])):
#             nova_lista.append(carga)
#     return nova_lista

def deletar_codigo_invalido(lista_cargas: list) -> list: 
    return [carga for carga in lista_cargas if bool(re.fullmatch(r'[AEIOU]{2}.{1}[0-9]{3}', carga['codigo']))] 

print(deletar_codigo_invalido(lista_cargas))

