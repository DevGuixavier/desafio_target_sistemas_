# função para completar as sequências
def completar_sequencias():
    # dicionário para armazenar as sequências
    sequencias = {
        'a': [1, 3, 5, 7],  # Sequência de números ímpares
        'b': [2, 4, 8, 16, 32, 64],  # Sequência de potências de 2
        'c': [0, 1, 4, 9, 16, 25, 36],  # Sequência de quadrados perfeitos
        'd': [4, 16, 36, 64],  # Sequência de quadrados de números pares
        'e': [1, 1, 2, 3, 5, 8],  # Sequência de Fibonacci
        'f': [2, 10, 12, 16, 17, 18, 19],  # Sequência de números inteiros
    }

    # calcula o próximo elemento para cada sequência
    sequencias['a'].append(sequencias['a'][-1] + 2)  # próximo ímpar
    sequencias['b'].append(sequencias['b'][-1] * 2)  # próxima potência de 2
    sequencias['c'].append((len(sequencias['c'])) ** 2)  # próximo quadrado
    sequencias['d'].append((len(sequencias['d']) + 2) ** 2)  # próximo quadrado par
    sequencias['e'].append(sequencias['e'][-1] + sequencias['e'][-2])  # Próximo Fibonacci
    sequencias['f'].append(sequencias['f'][-1] + 1)  # próximo número inteiro

    return sequencias

# roda a função armazenando o resultado
resultado = completar_sequencias()

# exibe as sequências com o próximo elemento adicionado
for chave, valor in resultado.items():
    print(f"Sequência {chave}: {valor}")


    # DEIXEI ESSES COMENTÁRIOS PARA FACILITAR O ENTENDIMENTO DO CÓDIGO #
