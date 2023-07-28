
def soma_dos_aninhados(lista): #define a função "soma dos aninhados"
    soma = 0 #define a soma como 0, inicialmente
    for i in lista: #passa por cada termo na lista
        for a in i: #passa por cada termo dentro das listas dentro das listas
            soma = a + soma #soma os termos acima
    return soma #retorna o valor de soma













