vol_cons = float(input('Digite o consumo de água em m³: '))

consumo = vol_cons
total = 0

if consumo > 30:
    dif = consumo - 30
    total = dif * 11.08
    consumo -= dif 
    
if  20 < consumo <= 30:
    consumo -= 10
    total += 65.50

if  15 < consumo <= 20:
    consumo -= 5
    total += 32.45

if 10 < consumo <= 15:
    consumo -= 5
    total += 32.30

if 5 < consumo <= 10:
    consumo -= 5
    total += 5.80

if consumo <= 5:
    total += 37.47 

totalConta = total + (total * 0.8)

print(26 * '*')
print(f'Total de Água   R$ {total:.2f}')
print(f'Total de Esgoto R$ {total * 0.8:.2f}')
print(f'Total da Conta  R$ {totalConta:.2f}')
print(26 * '*')
