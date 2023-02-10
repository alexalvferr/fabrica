salario_base = 200
comissao = 0.09

def calculo_salario(qtd_vendas):
    return salario_base + (comissao * qtd_vendas)

def get_faixa_salario_index(salario):
    faixa_salario = [200, 300, 400, 500, 600, 700, 800, 900, 1000]
    for i, faixa_limite in enumerate(faixa_salario):
        if salario < faixa_limite:
            return i
    return len(faixa_salario)

def main():
    valor_vendas = []
    num_vendas = int(input("Digite a Quantidade de Vendas Feitas: "))
    for i in range(num_vendas):
        valor_vendas.append(float(input("Digite o Valor da Venda: ")))

    salario_count = [0] * 9
    for qtd_vendas in valor_vendas:
        salario = calculo_salario(qtd_vendas)
        faixa_salario_index = get_faixa_salario_index(salario)
        salario_count[faixa_salario_index] += 1

    print("Faixa de Salário\t\tQuantidade de Vendedores")
    faixa_salario = [200, 300, 400, 500, 600, 700, 800, 900, 1000]
    for i, faixa_limite in enumerate(faixa_salario):
        if i == len(faixa_salario) - 1:
            print(f"$ {faixa_limite} ou maior\t\t {salario_count[i]}")
        else:
            print(f"$ {faixa_limite} - $ {faixa_salario[i + 1] - 1} \t\t\t {salario_count[i]}")

if __name__ == "__main__":
  main()