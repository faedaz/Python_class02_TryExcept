# Crie um script que solicite ao usuário uma lista de números separados por vírgula.

# O programa deve converter a string de entrada em uma lista de números inteiros. 

# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro.
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

try:
    user_input = input('Type any numbers you want using , as separator: ')
    string_list = user_input.split(',')

    integer_list = [int(item.strip()) for item in string_list]


    print("\nConversion successful!")
    print(f"Here is your list of integers: {integer_list}")
    
except ValueError:
    print("\nError: Please ensure all items are valid integers separated by commas.")
    print("Decimals (like 10.5) or text are not allowed.")
except Exception as error:
    print(f'Error! {error}')