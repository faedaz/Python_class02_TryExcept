# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

boolean = input('Type 1 for true and 0 for false: ')
boolean2 = input('Again: type 1 for true and 0 for false: ')

if boolean == '1':
    boolean = True
else:
    boolean = False

if boolean2 == '1':
    boolean2 = True
else:
    boolean2 = False
    
r = boolean or boolean2

print(f'{boolean} or {boolean2} = {r}')
    