valor_da_divida = float(input("Digite o valor da dívida:R$ "))
parcelas = 1
juros = 0
print(
    "|Valor da Dívida|Valor dos Juros|Quantidade de Parcelas |Valor da Parcela|"
)
while True:
    
    juros = (5 / 3) * parcelas + 5
    
    if parcelas == 1:
        juros = 0

    valor_do_juros = valor_da_divida * (juros / 100)
    valor_total = valor_da_divida + valor_do_juros
    valor_da_parcela = valor_total / parcelas
    print(
        f"|R$ {valor_total:.2f}\t"
        f"|R$ {valor_do_juros:.2f}\t"
        f"|{parcelas}\t\t\t"
        f"|R$ {valor_da_parcela:.2f}"
    )
    if parcelas == 1:
        parcelas -= 1
    parcelas += 3
    if parcelas > 12:
        break
