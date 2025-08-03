# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

date = input('Type the date: dd/mm/aaaa: ')

# Usar um nome de variável mais descritivo é uma boa prática
parts = date.split('/')

# Acessa cada parte da lista pelo seu índice
day = parts[0]
month = parts[1]
year = parts[2]

# Imprime cada variável separadamente
print(f'Day: {day}')
print(f'Month: {month}')
print(f'Year: {year}')