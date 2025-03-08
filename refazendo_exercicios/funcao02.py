# faça uma função que deve informar a quantidade de cargas por tipo de um determinado de setor, considerando somente
# os tipos existentes no setor. O codigo do setor será passado como argumento e o retorno desta função deve ser um
# dicionario em que as chaves são os tipos das cargas e o valor a quantidade. 

lista_cargas = [
                {'codigo': 'AOa123', 'tipo': 'A', 'tamanho': '', 'validade': '', 'quantidade': 12}
                ,{'codigo': 'AOa123', 'tipo': 'A', 'tamanho': '', 'validade': '', 'quantidade': 14}
                ,{'codigo': 'AOab23', 'tipo': 'B', 'tamanho': '', 'validade': '', 'quantidade': 15}
                ,{'codigo': 'oOa123', 'tipo': 'A', 'tamanho': '', 'validade': '', 'quantidade': 2}
                ] 

def quantidade_de_carga_por_tipo(lista_cargas, cod_setor): 
    dicionario = {}

    for carga in lista_cargas: 
        if cod_setor == carga['codigo'][:2]:
            dicionario[carga['tipo']] = dicionario.get(carga['tipo'], 0) + carga['quantidade'] 
        #     if carga['tipo'] in dicionario: 
        #         dicionario[carga['tipo']] += carga['quantidade']
        #     else: 
        #         dicionario[carga['tipo']] = carga['quantidade']
    return dicionario 

print(quantidade_de_carga_por_tipo(lista_cargas, 'AO'))

