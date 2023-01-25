# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 17:16:50 2022

@author: Alexandre
"""

file = 35.8
alcatra = 46.8
picanha = 67.8

tipo = input('Digite o tipo de carne que deseja: F para Filé Duplo, A para Alcatra e P para Picanha: ')
qtd = float(input('Digite a quantidade desejada: '))
pag = input('Digite a Forma de pagamento: C para Cartão Tabajara, P para PIX e D para Dinheiro: ')

if tipo == 'F' and qtd >= 5 and pag == 'C':
    print('==' * 20)
    print('*' * 4, 'CUPOM FISCAL', '*' * 4)
    print(f'{tipo} ------------- {qtd} ------------- Total R$ {file * qtd:.2f}')
    print(f'O desconto nessa compra é de R$ {file * qtd * 0.07514:.2f}')
    print(f'O valor total pago em {pag} é de R$ {file * qtd * 0.92486:.2f}')
elif tipo == 'F' and qtd >= 5 and pag != 'C':
    print('==' * 20)
    print('*' * 4, 'CUPOM FISCAL', '*' * 4)
    print(f'{tipo} ------------- {qtd} ------------- Total R$ {file * qtd:.2f}')
    print(f'O desconto nessa compra é de R$ {file * qtd * 0.02514:.2f}')
    print(f'O valor total pago em {pag} é de R$ {file * qtd * 0.97486:.2f}')
    
if tipo == 'A' and qtd >= 5 and pag == 'C':
    print('==' * 20)
    print('*' * 4, 'CUPOM FISCAL', '*' * 4)
    print(f'{tipo} ------------- {qtd} ------------- Total R$ {alcatra * qtd:.2f}')
    print(f'O desconto nessa compra é de R$ {alcatra * qtd * 0.09059:.2f}')
    print(f'O valor total pago em {pag} é de R$ {alcatra * qtd * 0.9094:.2f}')
elif tipo == 'A' and qtd >= 5 and pag != 'C':
    print('==' * 20)
    print('*' * 4, 'CUPOM FISCAL', '*' * 4)
    print(f'{tipo} ------------- {qtd} ------------- Total R$ {alcatra * qtd:.2f}')
    print(f'O desconto nessa compra é de R$ {alcatra * qtd * 0.04059:.2f}')
    print(f'O valor total pago em {pag} é de R$ {alcatra * qtd * 0.9594:.2f}')
    
if tipo == 'P' and qtd >= 5 and pag == 'C':
    print('==' * 20)
    print('*' * 4, 'CUPOM FISCAL', '*' * 4)
    print(f'{tipo} ------------- {qtd} ------------- Total R$ {picanha * qtd:.2f}')
    print(f'O desconto nessa compra é de R$ {picanha * qtd * 0.06327:.2f}')
    print(f'O valor total pago em {pag} é de R$ {picanha* qtd * 0.93672:.2f}')
elif tipo == 'P' and qtd >= 5 and pag != 'C':
    print('==' * 20)
    print('*' * 4, 'CUPOM FISCAL', '*' * 4)
    print(f'{tipo} ------------- {qtd} ------------- Total R$ {picanha * qtd:.2f}')
    print(f'O desconto nessa compra é de R$ {picanha * qtd * 0.01327:.2f}')
    print(f'O valor total pago em {pag} é de R$ {picanha * qtd * 0.98672:.2f}')
    
else:
    print('Digite um opção válida')
