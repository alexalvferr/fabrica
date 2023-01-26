nome = input('Digite o seu nome: ')
sex = input('Digite o seu sexo: M para Masculino, F para Feminino ou O para Outros: ')
est_civ = input('Digite o seu estado civil: C para Casado(a), S para Solteiro(a), D para Divorciado(a), V para Viúvo ou O para Outros(as): ')
if sex == 'F' and est_civ == 'C':
    anos = int(input('Digite quantos anos é Casada: '))
    print(f'Seu nome é {nome}, é do sexo feminino, e tem {anos} anos de Casada')
else:
    print('Obrigado pelas Informações')
