# Faça uma função que deve contar quantos codigos de cargas repetidos existem em uma lista de codigo de cargas.
# Para esta função você não pode utilizar o comando for e deve utilizar a função reduce para fazer a contagem que
# será retornada. 
from functools import reduce

lista_cargas = [
                {'codigo': 'AOa123', 'tipo': 'A', 'tamanho': '', 'validade': '', 'quantidade': 12}
                ,{'codigo': 'AOa123', 'tipo': 'A', 'tamanho': '', 'validade': '', 'quantidade': 14}
                ,{'codigo': 'AOab23', 'tipo': 'B', 'tamanho': '', 'validade': '', 'quantidade': 15}
                ,{'codigo': 'oOa123', 'tipo': 'A', 'tamanho': '', 'validade': '', 'quantidade': 2}
                ] 


def contar_codigo_repetido(lista_cargas):
    
    def checar_repetidos(repetidos, zip):
        carga1, carga2 = zip
        if carga1['codigo'] == carga2['codigo']:
            return repetidos + 1 
        return repetidos

    repetidos = reduce(checar_repetidos, zip(lista_cargas, lista_cargas[1:]), 0)
    
    return repetidos

    # for carga1, carga2 in zip(lista_cargas, lista_cargas[1:]): 
    #     if carga1['codigo'] == carga2['codigo']: 
    #         repetidos += 1
         

    # lista_codigos = [carga['codigo'] for carga in lista_cargas]
    # lista_codigos_sem_duplicatas = list(set(lista_codigos))
    
    # for codigo in lista_codigos_sem_duplicatas: 
    #     if lista_codigos.count(codigo) > 1:
    #         repetidos += 1
    # return repetidos  


print(contar_codigo_repetido(lista_cargas))