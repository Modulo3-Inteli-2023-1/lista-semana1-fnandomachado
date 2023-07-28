
def multiplas_operacoes(a, b): #define a função
    soma = a + b #soma a e b
    subtrai = a - b #subtrai b de a
    multiplica = a * b #multiplica os termos a e b
    
    if b == 0: #define que, se b = 0, o resultado da divisão será 0
        dividir = 0
    else: #se b diferente de 0, continua abaixo
        dividir = a / b #divide a por b

    # print (soma, subtrai, multiplica, dividir) #retorna no console os resultados matemáticos
    return soma, subtrai, multiplica, dividir











