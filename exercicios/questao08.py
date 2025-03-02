# 8. Faça um programa que receba dois arquivos do usuario, e crie um terceiro arquivo com
# o conteudo dos dois primeiros juntos (o conteúdo do primeiro seguido do conteúdo do segundo).

def inserir_caminho(caminho1: str, caminho2: str) -> None: 
    """A função recebe dois arquivos do usuário e cria um novo com o conteúdo dos dois
    
    Args: 
        caminho1 (str): É o caminho do primeiro arquivo
        caminho2 (str): É o caminho do segundo arquivo 
    """
    dados1 = " "
    dados2 = " "

    with open(caminho1, "r", encoding="utf-8") as arquivo: 
        dados1 = arquivo.read()
    
    with open(caminho2, "r", encoding="utf-8") as arquivo: 
        dados2 = arquivo.read() 
    
    with open("novo_arquivo", "w", encoding="utf-8") as arquivo: 
        arquivo.write(dados1 + ", ") 
        arquivo.write(dados2) 

inserir_caminho("arquivo1.txt", "arquivo2.txt")

