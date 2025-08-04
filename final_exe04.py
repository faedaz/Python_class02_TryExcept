# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

try:
    n = float(input('Type a number: '))
    if n > 0:
        print('Positive')
    elif n == 0:
        print('Zero')
    else:
        print('Negative')
        
    if n % 1 == 0: 
        if n % 2 == 0:
            print('And it is Even.') 
        else:
            print('And it is Odd.')  
    else:
        print("The even/odd classification does not apply to non-integer numbers.")
except ValueError:
    print('Type a valid number')
except Exception as error:
    print(f'Error! {error}')