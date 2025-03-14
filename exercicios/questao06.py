# 6. Faça um programa que receba do usuario um arquivo texto. Crie outro arquivo texto
# contendo o texto do arquivo de entrada, mas com as vogais substituídas por ‘*’.

import re 

caminho = input("Informe o caminho do arquivo:")

dados = " "

with open(caminho, "r", encoding="utf-8") as arquivo: 
    dados = arquivo.read() 
    #metodo read lê todo o arquivo e retorna uma string contendo o arquivo inteiro
    #metodo readline lê uma linha do arquivo e retorna a linha como string
    #metodo readlines lê todo o arquivo e retonar uma lista onde cada elemento é uma string de cada linha do arquivo

with open("novo_" + caminho, "w", encoding="utf-8") as arquivo: 
    arquivo.write(re.sub("[aeiouAEIOU]", "*", dados)) 