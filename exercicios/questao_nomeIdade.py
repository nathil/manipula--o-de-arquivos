
def retorna_lista(caminho: str) -> list: 
    dados = ""
    lista_dados = [] 

    with open(caminho, "r", encoding="utf-8") as arquivo: 
        dados = arquivo.readlines()
    
    for dado in dados[1:]: 
        valores = dado.strip().split(",") 

        registro = {"Nome": valores[0], "Idade": valores[1]}
        lista_dados.append(registro) 

    return lista_dados 

print(retorna_lista("nome_idade.csv"))

def retorna_nome_idade(): 
    lista_dados = retorna_lista("nome_idade.csv")

    for dado in lista_dados:  
        print(f"Nome:{dado['Nome']}, Idade:{dado['Idade']}")
        
        
retorna_nome_idade()

def retorna_dict(caminho: str) -> dict:
    lista_nome = []
    lista_idade = []

    with open(caminho, "r", encoding="utf-8") as arquivo: 
        dados = arquivo.readlines()
    
    for dado in dados[1:]: 
        valores = dado.strip().split(",") 
        lista_nome.append(valores[0])
        lista_idade.append(valores[1])

    registro = {"Nome": lista_nome, "Idade": lista_idade}

    return registro

print(retorna_dict("nome_idade.csv"))