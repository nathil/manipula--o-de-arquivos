# 9. Crie uma função que receba como entrada o nome de um arquivo de entrada e outro de saída.
# O arquivo de entrada possui um cabeçalho e contem os campos cidade e população separados por vírgula.
# O programa deve ler o arquivo de entrada e gerar um arquivo de saída com o nome da cidade e a população da cidade 
# com maior população.O arquivo de saída deve conter um cabeçalho e os campos cidade e população separados por vírgula.

#primeiro modo

def funcao(caminho1: str, caminho2: str) -> None:
    with open(caminho1, "r", encoding="utf-8") as arquivo: 
        linhas = arquivo.readlines() 

        cidade = " "

        maior = int(linhas[1].split(",")[1])
        for linha in linhas[1:]:
            if int(linha.split(",")[1]) > maior: 
                maior = int(linha.split(",")[1])
                cidade = linha.split(",")[0]
    
    with open(caminho2, "w", encoding="utf-8") as arquivo: 
        arquivo.write(f"cidade,populacao\n") 
        arquivo.write(f"{cidade},{maior}\n") 

funcao("teste.csv", "novo_teste.csv")

#segundo modo 

#lista de dicionarios 

def retorna_lista(caminho1: str) -> list: 
    with open(caminho1, "r", encoding="utf-8") as arquivo: 
        dados = arquivo.readlines()
        registros = []  

        for dado in dados[1:]: 
            registro = {"cidade": dado.split(",")[0], "populacao": dado.strip().split(",")[1]}
            registros.append(registro)
    return registros

print(retorna_lista("teste.csv"))

def retorna_maior_populacao(caminho1: str, caminho2: str) -> None: 
    registros = retorna_lista(caminho1)
    maior = int(registros[0]["populacao"]) 
    cidade = ""
    with open(caminho1, "r", encoding="utf-8") as arquivo: 
        for registro in registros[1:]:  
            if int(registro["populacao"]) > maior: 
                maior = int(registro["populacao"]) 
                cidade = registro["cidade"] 

    with open("novo_caminho.csv", "w", encoding="utf-8") as arquivo: 
        arquivo.write("cidade" + "," + "populacao" + "\n") 
        arquivo.write(f"{cidade},{maior}\n")  

retorna_maior_populacao("teste.csv", "novo_caminho.csv")