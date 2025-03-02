# 6. Faça um programa que receba do usuario um arquivo texto. Crie outro arquivo texto
# contendo o texto do arquivo de entrada, mas com as vogais substituídas por ‘*’.

import re 

caminho = input("Informe o caminho do arquivo:")

dados = " "

with open(caminho, "r", encoding="utf-8") as arquivo: 
    dados = arquivo.read() 

with open("novo_" + caminho, "w", encoding="utf-8") as arquivo: 
    arquivo.write(re.sub("[aeiouAEIOU]", "*", dados)) 