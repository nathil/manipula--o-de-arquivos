from dados import carregarDados

def retornaId(numero):
    dados = carregarDados()
    listaIds = []
    for item in dados: 
        if int(item['number']) == numero:
            listaIds.append(item['ID'])
    return listaIds


