def descobrir_lampadas():
    # inicializa o estado dos interruptores
    estado = ['desligado', 'desligado', 'desligado']
    
    # liga o interruptor 1 e aguarda um tempo
    estado[0] = 'ligado'  # Liga o interruptor 1

    # desliga o interruptor 1 e liga o interruptor 2
    estado[0] = 'desligado'
    estado[1] = 'ligado'  # Liga o interruptor 2

    # simula a verificação das lâmpadas
    # A lâmpada 1 está quente, a lâmpada 2 está acesa, e a lâmpada 3 está desligada
    lampadas = ['quente', 'acesa', 'desligada']

    # Verifica o estado das lâmpadas
    resultado = {
        'interruptor 1': 'lâmpada 1 (quente)',  # Lâmpada 1 está quente
        'interruptor 2': 'lâmpada 2 (acesa)',    # Lâmpada 2 está acesa
        'interruptor 3': 'lâmpada 3 (desligada)'  # Lâmpada 3 está desligada
    }

    return resultado

# executa a função
interruptores = descobrir_lampadas()
print(interruptores)


    # DEIXEI ESSES COMENTÁRIOS PARA FACILITAR O ENTENDIMENTO DO CÓDIGO #