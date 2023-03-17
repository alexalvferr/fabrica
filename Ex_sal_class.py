from Ex_classes01 import *

class program:
    if __name__ == "__main__":
        funcionario01 = Funcionario(float(input('Salário do Funcionário 01 R$: ')), input('Nome do Funcionário 01: '))
        funcionario02 = Funcionario(float(input('Salário do Funcionário 02 R$: ')), input('Nome do Funcionário 02: '))
        med_sal = (funcionario01.salario + funcionario02.salario)/2

        print(f'A média dos salários é R$ {med_sal:.2f}')
    
    '''print('Digite o nome do Funcionário 01: ')
    funcionario01.nome: input('Nome do Funcionário 01: ')
    funcionario01.salario: float(input('Salário do Funcionário 01 R$: '))

    print('Digite o nome do Funcionário 02: ')
    funcionario02.nome: input('Nome do Funcionário 02: ')
    funcionario02.salario: float(input('Salário do Funcionário 02 R$: '))

    print(f'A Média dos salários é R$ ({funcionario01.salario} + {funcionario02.salario})/2 :.2f')'''
