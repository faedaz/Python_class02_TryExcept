# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

try: 
    word = input('Type a word or phrase: ')

    # A validação com isinstance é redundante aqui, pois input() sempre retorna str.
    # Mas vamos mantê-la como parte do exercício didático.
    if not isinstance(word, str):
        raise TypeError("Invalid input: a string is required.")

    # >> CORREÇÃO PRINCIPAL: Inicializando a variável antes de usá-la.
    clear_word = "" 
    for caractere in word:
        if caractere.isalnum():
            clear_word += caractere.lower()
    
    # Verificação de string vazia após a limpeza
    if not clear_word:
        raise ValueError("The input does not contain any valid characters (letters or numbers).")

    # Lógica do palíndromo
    word_reverse = clear_word[::-1]
    print("-" * 30)

    if clear_word == word_reverse:
        print(f"Yes, '{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")

except TypeError as e:
    print(f"\n[TYPE ERROR]: {e}")
except ValueError as e:
    print(f"\n[VALUE ERROR]: {e}")
except Exception as e:
    print(f"\n[UNEXPECTED ERROR]: {e}")
