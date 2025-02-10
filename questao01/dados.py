def carregarDados():
    try:
        registros = []

        with open('dados_usuarios.txt', 'r', encoding='utf-8') as f:
            for linha in f:
                if linha.endswith('\n'):
                    linha = linha[:-1]
                    
                id, year, gender, name, number = linha.split(',')
                usuario = {'ID': id, 'year': year, 'gender': gender, 'name': name, 'number': number} 
                registros.append(usuario)
            return registros
            
    except FileNotFoundError: 
        print('Arquivo não encontrado.')
        return []

def salvarDados(registros):
    try:
        lista = []
        with open('dados_usuarios.txt', 'w', encoding='utf-8') as f:
            for registro in registros:
                f.write(','.join(registro.values()) + '\n')
        
    except FileNotFoundError:
        print('Não encontrado.')
        return []

def adicionarDado(registro): 
    try: 
        with open('dados_usuarios.txt', 'a', encoding='utf-8') as f: 
            f.write(f'{registro["ID"]},{registro["year"]},{registro["gender"]},{registro["name"]},{registro["number"]}\n')   

    except FileNotFoundError: 
        print(f'Arquivo não encontrado.')
    
    