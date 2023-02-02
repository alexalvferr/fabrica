print(''''Qual o melhor Sistema Operacional para uso em servidores, dentre os informados abaixo:'

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
''')

urna = []
sistemas = ['Windows Server','Unix','Linux','Netware','Mac OS','Outro']
ind_vit = []
ind_porc_vit = []
eleitor = True
num_voto = 1

while eleitor != 0:
    print(f'\nEleitor nº {num_voto}\n')
    voto = int(input('Digite o seu voto [1 a 6] ou Digite [0] para sair: '))
    if voto == 0:
        break
    else:
        while voto < 0 or voto > 6:
            print('###Número Inválido, Digite Um Número Válido###')
            voto = int(input('Digite o seu voto [1 a 6] ou Digite [0] para sair: '))
        print('[Voto Confirmado]\n')
        urna.append(voto)
    num_voto += 1

print('\n' * 2)
print('{:<19}{:>10}{:>4}'.format('Sistema Operacional','Votos','%'))
print('{:<19}{:>10}{:>6}'.format('-'*19,'-'*5,'-'*3))

contador = 0
for i in range(len(sistemas)):
    porc_voto = round((urna.count(contador+1) / len(urna)) * 100)
    print('{:<19}{:>10}{:>5}%'.format(sistemas[contador],urna.count(contador+1),porc_voto))
    contador +=1
    ind_vit.append(urna.count(contador+1))
    ind_porc_vit.append(porc_voto)

print('{:<19}{:>10}'.format('-'*19,'-'*5,))
print('{:<19}{:>10}'.format('Total',len(urna)))

vitoria = max(ind_vit)
for i in range(len(sistemas)):
    if ind_vit[i] == vitoria:
        print('\nO sistema mais votado foi o ', sistemas[i], end=' ')

print('com ', max(ind_vit), ' votos, correspondendo a ', max(ind_porc_vit), '% dos votos.')