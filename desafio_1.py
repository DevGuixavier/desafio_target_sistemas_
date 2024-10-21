# Verifica se um número pertence à sequência de Fibonacci
def fibonacci_check(n):
    a, b = 0, 1  # inicia essa sequência com 0 e 1

    fib_sequence = [a]  # lista para armazenar a sequência
    
    while b <= n:  # gera a sequência até b ser maior que n
        fib_sequence.append(b)  # Adiciona b à lista
        a, b = b, a + b  # atualiza a e b
    
    # retorna se n pertence à sequência
    return f"O número {n} pertence à sequência de Fibonacci." if n in fib_sequence else f"O número {n} não pertence à sequência de Fibonacci."

# pede um número ao usuário
while True:
    try:
        numero = int(input("Informe um número inteiro: "))  # tenta converter a entrada para inteiro
        break  # se a conversão for bem-sucedida, sai desse loop
    except ValueError:
        print("Erro: Você deve informar um número inteiro. Por favor, tente novamente.")

resultado = fibonacci_check(numero)  # Chama a função
print(resultado)  # exibe o resultado


  # DEIXEI ESSES COMENTÁRIOS PARA FACILITAR O ENTENDIMENTO DO CÓDIGO #
