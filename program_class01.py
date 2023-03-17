from Ex_classes01 import *
class Program:
    if __name__ == "__main__":
        pessoa01 = Pessoa()
        pessoa02 = Pessoa()
        print('Dados da primeira Pessoa: ')
        pessoa01.nome = input('Nome da Pessoa 01: ')
        pessoa01.idade = int(input('Idade Pessoa 01: '))

        print('Dados da Segunda Pessoa: ')
        pessoa02.nome = input('Nome da Pessoa 02: ')
        pessoa02.idade = int(input('Idade Pessoa 02: '))

        if(pessoa01.idade > pessoa02.idade):
            print(f'A Pessoa Mais Velha é {pessoa01.nome}')
        elif(pessoa02.idade > pessoa01.idade):
            print(f'A Pessoa Mais Velha é {pessoa02.nome}')
        else:
            print(f'{pessoa01.nome} e {pessoa02.nome} têm a mesma idade {pessoa01.idade} anos')
