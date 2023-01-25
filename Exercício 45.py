ano_atual = 2022
ano_nasc = int(input('Digite o seu ano de nascimento com 04 Dígitos: '))
id_anos = ano_atual - ano_nasc
id_mes = id_anos * 12
id_sem = id_anos * 52
id_dias = id_anos * 365

print(f'Você tem {id_anos} anos,\n ou {id_mes} meses,\n ou {id_sem} semanas,\n ou {id_dias} dias')
