# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.



boolean = input('Type 1 for true and 0 for false: ')


if boolean == '1':
    boolean = True
else:
    boolean = False


    
r = not boolean

print(f'{r} ')
    