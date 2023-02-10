sim = 0
perguntas = ['Telefonou para a vitima? [s/n]: ',
             'Esteve no local do crime? [s/n]: ',
             'Mora perto da vitima? [s/n]: ',
             'Devia para a vitima? [s/n]: ',
             'Já trabalhou com a vítima? [s/n]: '
             ]
for i in range(len(perguntas)):
    resposta = input(perguntas[i])
    if resposta == 's':
        sim += 1
if sim == 2:
    print('\nVocê é Suspeito!')
elif sim > 2 and sim <= 4:
    print('\nVocê é Cumplice!')
elif sim == 5:
    print('\nVocê é o Assassino!')
else:
    print('\nVocê é Inocente!')