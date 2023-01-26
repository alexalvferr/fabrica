nun_conta = int(input("Digite o Número da conta: "))
saldo = 5467.75
credito = float(input("Digite o valor depositado na conta: "))
debito = float(input("Digite o valor sacado da conta: "))
saldo_atual = saldo + (credito - debito)

print(f"O número da sua conta é: {nun_conta}")
print(f"O seu saldo é de R$ {saldo}")
print(f"O valor depositado na conta foi de R$ {credito}")
print(f"O valor sacado da conta foi de R$ {debito}")
print(f"O seu saldo atual é de R$ {saldo_atual:.2f}")
if saldo_atual > 0:
  print(f"O saldo é POSITIVO no valor de R$ {saldo_atual:.2f}")
else:
  print(f"O saldo é NEGATIVO no valor de -R$ {saldo_atual:.2f}")
