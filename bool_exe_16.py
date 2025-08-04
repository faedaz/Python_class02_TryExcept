# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.


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
    
r = boolean and boolean2

print(f'{boolean} and {boolean2} = {r}')
    
