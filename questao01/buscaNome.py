from dados import carregarDados

def buscaNome(nome = ''): 
    dados = carregarDados() 
    contarNome = 0
    listaNomes = []

    for item in dados: 
        if item['name'].split()[0].lower() == nome.lower(): 
            contarNome += 1 
            listaNomes.append(item)        

    return listaNomes, contarNome
