
def cumulativo(lis): #define a funçãoi "cumulativo"
    soma = 0 #cria a variável soma e a define como 0
    lista_cumul = [] #cria a lista com os termos a serem adicionados
    for i in lis: #passa por cada termo da lista "inputada"
       soma = soma + i #soma o termo da lista "inputada" à soma já existente
       lista_cumul.append(soma) #acrescenta à lista o valor somado acima
    return(lista_cumul)  #retorna a lista com os novos termos acumulados













