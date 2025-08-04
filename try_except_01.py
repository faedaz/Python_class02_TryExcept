

try:
    n1 = int(input('Type a number: '))
    n2 = int(input('Type another number: '))
    sum = n1 + n2
    print(f'{n1} + {n2} = {sum}')
except ValueError:
    print("Type a number!")
except KeyboardInterrupt:
    print("You choose to abort the programm")
else:
    print("The programm is fine!")
finally:
    print("End")