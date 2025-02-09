from dados import carregarDados 

def buscaYearGender(year = None, gender = None): 
    contarYearGender = 0
    dados = carregarDados()

    if year == None or gender == None: 
        return None
    
    for item in dados: 
        if int(item['year']) >= year and item['gender'] == gender:
            contarYearGender += 1

    return contarYearGender

