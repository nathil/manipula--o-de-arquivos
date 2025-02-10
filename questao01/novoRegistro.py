from dados import carregarDados, adicionarDado

def novoRegistro(year, gender, name, number):
    dados = carregarDados()

    adicionandoValores = {'ID': str(int(dados[-1]['ID']) + 1), 'year': year, 'gender': gender, 'name': name, 'number':
                          number} 
    adicionarDado(adicionandoValores)
    
    


