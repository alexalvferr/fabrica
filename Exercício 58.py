print( 30 * '-', 'CARDÁPIO', 30 * '-')

print(
'''BIFE ACEBOLADO = R$ 17,00 [1]
LASANHA           = R$ 23,00 [2]
CACHORRO QUENTE   = R$ 10,00 [3]
FRANGO ASSADO     = R$ 12,00 [4]
CARRETEIRO        = R$ 20,00 [5]
BIFE A CAVALO     = R$ 25,00 [6]
OVO FRITO         = R$ 5,00  [7]
REFIRGERANTE      = R$ 6,00  [8]
SUCO              = R$ 8,00  [9]
CAFÉ              = R$ 4,00  [10]''')
print(68 * '-')

prato = int(input('Digite o código do prato deseja:\n'))

match prato:
  case 1:
    prato = 17

  case 2:
    prato = 23

  case 3:
    prato = 10

  case 4:
     prato = 12

  case 5:
    prato = 20
    
  case 6:
    prato = 25

  case 7:
    prato = 5

  case 8:
    prato = 6

  case 9:
    prato = 8
  
  case 10:
    prato = 4
    

tx = str(input('Você aceita pagar a Taxa de serviço de 10%? \n'))
tx = tx.upper()
tx = tx.strip()[0]

if tx == 'S':
    por = prato * 0.1
    valortotal = prato + por
    print(f'O valor total é de R$ {valortotal:.2f}')

elif tx == 'N':
    print (f'O valor total é de R$ {prato:.2f}')