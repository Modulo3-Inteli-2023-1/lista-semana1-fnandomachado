
def tem_duplicados(lista): #define a função "tem duplicados"

    dict = {} #cria o dicionário dict

    for i in lista: #passa por cada termo na lista
        if i in dict: #vê se o termo está presente no dicionário
            return True
        dict[i] = True #adiciona o termo no dicionário, caso este não esteja ainda

    return False













