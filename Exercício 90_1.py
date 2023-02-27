def main():
    vendas = []
    num_vendas = int(input('Digite a quantidade de vendas realizadas: '))
    for i in range(num_vendas):
        vendas.append(float(input('Digite o Valor da Venda:$  ')))
    salario_faixa = [200, 300, 400, 500, 600, 700, 800, 900, 1000]
    salario_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(num_vendas):
        salario = 200 + (0.09 * vendas[i])
        print(f'$ {salario:.2f}')
        for j in range(len(salario_faixa)):
            if salario < salario_faixa[j]:
                salario_count[j - 1] += 1
                break
    print('Faixa de Salário\t\tQuantidade de Vendas')
    for i in range(len(salario_faixa)):
        if i == len(salario_faixa) - 1:
            print(f'$ {salario_faixa[i]} e mais\t\t {salario_count[i]}')
        else:
            print(f'$ {salario_faixa[i]} - $ {salario_faixa[i + 1] - 1} \t\t {salario_count[i]}')

if __name__ == "__main__":
    main()
