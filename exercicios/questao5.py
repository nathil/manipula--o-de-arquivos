# Faça um programa que receba do usuario um arquivo texto e mostre na tela quantas
# vezes cada letra do alfabeto aparece dentro do arquivo.

def retorna_contagem(caminho): 
    dados = ""
    contador = {}
    with open(caminho, "r", encoding="utf-8") as arquivo: 
        dados = arquivo.read()

        for letra in "abcdefghijklmnopqrstuvwxyz": 
            l = dados.count(letra.lower()) + dados.count(letra.upper()) 
        # a = dados.count("a") + dados.count("A")
        # e = dados.count("e") + dados.count("E")
        # i = dados.count("i") + dados.count("I")
        # o = dados.count("o") + dados.count("O")
        # u = dados.count("u") + dados.count("U") 
            print(f"{letra}={l}")

retorna_contagem("arquivo_questao5.csv")