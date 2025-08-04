# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

try:
    num1 = float(input('Type a number: '))
    num2 = float(input('Type another number: '))
    operator = str(input('Choose your operator + - * /: '))

    if operator == '+' :
        r = num1 + num2
        print(f'Result: {r}')
    elif operator == '-':
        r = num1 - num2
        print(f'Result: {r}')
    elif  operator == '/':
        r = num1 / num2
        print(f'Result: {r}')
    elif operator == '*':
        r = num1 * num2
        print(f'Result: {r}')
    else:
        print("Invalid operator. Please use one of the following: +, -, *, /") 
except ValueError:
    print('Error')
except ZeroDivisionError:
    print('Error! Division by zero')
except Exception as error:
    print(f'Error! {error}')