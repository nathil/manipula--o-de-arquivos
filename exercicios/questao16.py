def retorna_nome_nota(caminho: str): 
    dados = ""
    alunos = []
    with open(caminho, "r", encoding="utf-8") as arquivo: 
        dados = arquivo.readlines()
        for dado in dados[1:]: 
            aluno = {"Nome": dado.split(",")[0], "Nota": dado.strip().split(",")[1]} 
            alunos.append(aluno) 

    maior = int(alunos[0]["Nota"])
    aluno_maior_nota = ""
    for aluno in alunos: 
        if int(aluno["Nota"]) > maior: 
            maior = int(aluno["Nota"])
            aluno_maior_nota = aluno["Nome"]
    return aluno_maior_nota, maior 

nome_aluno, nota_aluno = retorna_nome_nota("arquivo_questao16.csv")

print(f"Nome:{nome_aluno}\nNota:{nota_aluno}")