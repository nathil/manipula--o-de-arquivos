from dados import carregarDados

def retornaValores(arg): 
    dados = carregarDados()
    novaLista = []
    
    for item in dados: 
        for i in item.values(): 
            if arg in i: 
                novaLista.append(item)
                break

    return novaLista
