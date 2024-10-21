def calcular_soma(indice):
    # começa com a soma zerada
    soma = 0
    # k começa em 1, que é o primeiro número a ser somado
    k = 1
    # continua somando enquanto k for menor que o índice
    while k < indice:
        k += 1  # aumenta k em 1
        soma += k  # adiciona k à soma total
    
    return soma  # retorna a soma final

# define até onde queremos somar
indice = 12
# calcula a soma até o índice
soma_total = calcular_soma(indice)
# exibe o resultado
print(soma_total)

# DEIXEI ESSES COMENTÁRIOS PARA FACILITAR O ENTENDIMENTO DO CÓDIGO #
