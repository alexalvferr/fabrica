sexo = input('Digite F para Feminino, M para Masculino ou O para Outros: ')
alt = int(input('Digite a sua Altura em cm: '))
est_fis = int(input('Digite 1 para Estado Físico Bom, 2 para Estado Físico Regular ou 3 para Estado Físico Ruim: '))
count = 0
sexo = 0

for i in range (10):

    if sexo == 'F' and alt >= 170:
        count = count + 1
    print(f'A Quantidade de Mulheres com mais de 1,70 metros de altura é {count}')

    if sexo == 'M' and est_fis == 1:
        count = count + 1
    print(f'O percentual de Homens que fizeram a entrevista foi de {count * 100 / sexo}')
