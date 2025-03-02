# 15. Faça um programa que leia um arquivo contendo o nome e o preço de diversos produtos
# (separados por linha), e calcule o total da compra, com cabeçalho. 

def retorna_lista(caminho1: str) -> list: 
    dados = ""
    lista_produtos = []
    with open(caminho1, "r", encoding="utf-8") as arquivo: 
        dados = arquivo.readlines() 
        for dado in dados[1:]: 
            produto = {"Nome": dado.split(",")[0], "Preço": dado.strip().split(",")[1]} 
            lista_produtos.append(produto)
    return lista_produtos 

def retorna_calcula_compra(caminho1: str) -> None: 
    total = 0 

    with open(caminho1, "r", encoding="utf-8") as arquivo:
        produtos = retorna_lista("arquivo15.csv") 

        for produto in produtos: 
            total = float(produto["Preço"]) + total 
    
    with open("compra_total", "w", encoding="utf-8") as arquivo: 
        arquivo.write("Valor Total\n")
        arquivo.write(f"{total}\n") 

retorna_calcula_compra("arquivo15.csv")