def contar_letra_a(letra):
    # Conta quantas vezes a letra 'a' aparece na string, sem diferenciar maiúsculas de minúsculas
    contador = letra.lower().count('a')  # Converte a string para minúsculas e conta 'a'
    
    # Se a letra 'a' apareceu pelo menos uma vez
    if contador > 0:
        return f"A letra 'a' aparece {contador} vez(es) na string."  # Retorna a contagem
    else:
        return "A letra 'a' não aparece na string."  # Informa que não há 'a'

def main():
    # pede para o usuário digitar uma string
    string = input("Informe uma string: ")
    # Conta as letras 'a' na string
    resultado = contar_letra_a(string)
    # exibe o resultado
    print(resultado)

# executa a função main se o script for rodado diretamente
if __name__ == "__main__":
    main()

    # DEIXEI ESSES COMENTÁRIOS PARA FACILITAR O ENTENDIMENTO DO CÓDIGO #
