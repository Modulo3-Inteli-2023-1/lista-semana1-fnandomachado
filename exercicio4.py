#  Se achar necessario, faça import de outras bibliotecas

# Crie a função que será avaliada no exercício aqui
def tem_duplicados(t):

    d = {}

    for x in t:

        if x in d:

            return True

        d[x] = True

    return False

# Teste a sua função aqui (caso ache necessário)











