n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
oper = input("Digite Soma para somar, Sub para subtrair, Mult para Div para Dividir os Números:  ")
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
rest = n1 % n2

if oper == 'Soma':
    
    if soma > 0 and soma % 2 == 0 and rest == 0:
        print(f'O resultado é {soma} e o número é positivo, par e inteiro ')
    elif soma > 0 and soma % 2 != 0 and rest == 0:
        print(f'O resultado é {soma} e o número é positivo, ímpar e inteiro ')
    elif soma > 0 and soma % 2 == 0 and rest != 0:
        print(f'O resultado é {soma} e o número é positivo, par e decimal ')
    elif soma > 0 and soma % 2 != 0 and rest != 0:
        print(f'O resultado é {soma} e o número é positivo, ímpar e decimal ')

    elif soma < 0 and soma %2 == 0 and rest == 0:
        print(f'O resultado é {soma} e o número é negativo, par e inteiro ')
    elif soma < 0 and soma % 2 != 0 and rest == 0:
        print(f'O resultado é {soma} e o número é negativo, ímpar e inteiro ')
    elif soma < 0 and soma % 2 == 0 and rest != 0:
        print(f'O resultado é {soma} e o número é negativo, par e decimal ')
    elif soma < 0 and soma % 2 != 0 and rest != 0:
        print(f'O resultado é {soma} e o número é negativo, ímpar e decimal ')
    else:
        print("O resultado da soma é Zero.")

if oper == 'Sub':
    
    if sub > 0 and sub%2 == 0 and rest == 0:
        print(f'O resultado é {sub} e o número é positivo, par e inteiro ')
    elif sub > 0 and sub%2 != 0 and rest == 0:
        print(f'O resultado é {sub} e o número é positivo, ímpar e inteiro ')
    elif sub > 0 and sub%2 == 0 and rest != 0:
        print(f'O resultado é {sub} e o número é positivo, par e decimal ')
    elif sub > 0 and sub%2 != 0 and rest != 0:
        print(f'O resultado é {sub} e o número é positivo, ímpar e decimal ')

    elif sub < 0 and sub%2 == 0 and rest == 0:
        print(f'O resultado é {sub} e o número é negativo, par e inteiro ')
    elif sub < 0 and sub%2 != 0 and rest == 0:
        print(f'O resultado é {sub} e o número é negativo, ímpar e inteiro ')
    elif sub < 0 and sub%2 == 0 and rest != 0:
        print(f'O resultado é {sub} e o número é negativo, par e decimal ')
    elif sub < 0 and sub%2 != 0 and rest != 0:
        print(f'O resultado é {sub} e o número é negativo, ímpar e decimal ')
    else:
        print("O resultado da subtração é Zero.")

if oper == 'Mult':
    
    if mult > 0 and mult%2 == 0 and rest == 0:
        print(f'O resultado é {mult} e o número é positivo, par e inteiro ')
    elif mult > 0 and mult%2 != 0 and rest == 0:
        print(f'O resultado é {mult} e o número é positivo, ímpar e inteiro ')
    elif mult > 0 and mult%2 == 0 and rest != 0:
        print(f'O resultado é {mult} e o número é positivo, par e decimal ')
    elif mult > 0 and mult%2 != 0 and rest != 0:
        print(f'O resultado é {mult} e o número é positivo, ímpar e decimal ')

    elif mult < 0 and mult%2 == 0 and rest == 0:
        print(f'O resultado é {mult} e o número é negativo, par e inteiro ')
    elif mult < 0 and mult%2 != 0 and rest == 0:
        print(f'O resultado é {mult} e o número é negativo, ímpar e inteiro ')
    elif mult < 0 and mult%2 == 0 and rest != 0:
        print(f'O resultado é {mult} e o número é negativo, par e decimal ')
    elif mult < 0 and mult%2 != 0 and rest != 0:
        print(f'O resultado é {sub} e o número é negativo, ímpar e decimal ')
    else:
        print("O resultado da multiplicação é Zero.")

if oper == 'Div':
    
    if div > 0 and div%2 == 0 and rest == 0:
        print(f'O resultado é {div} e o número é positivo, par e inteiro ')
    elif div > 0 and div%2 != 0 and rest == 0:
        print(f'O resultado é {div} e o número é positivo, ímpar e inteiro ')
    elif div > 0 and div%2 == 0 and rest != 0:
        print(f'O resultado é {div} e o número é positivo, par e decimal ')
    elif div > 0 and div%2 != 0 and rest != 0:
        print(f'O resultado é {div} e o número é positivo, ímpar e decimal ')

    elif div < 0 and div%2 == 0 and rest == 0:
        print(f'O resultado é {div} e o número é negativo, par e inteiro ')
    elif div < 0 and div%2 != 0 and rest == 0:
        print(f'O resultado é {div} e o número é negativo, ímpar e inteiro ')
    elif div < 0 and div%2 == 0 and rest != 0:
        print(f'O resultado é {div} e o número é negativo, par e decimal ')
    elif div < 0 and div%2 != 0 and rest != 0:
        print(f'O resultado é {div} e o número é negativo, ímpar e decimal ')
    else:
        print("O resultado da divisão é Zero.")
        




