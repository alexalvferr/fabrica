'''salario = 200 + (0.09 * vendas[i])
j = int((salario - 200) / 100)
if j >= len(salario_count):
    j = len(salario_count) - 1
salario_count[j] += 1'''

'''def main():
    vendas = []
    num_vendas = int(input("Digite a quantidade de vendas realizadas: "))
    for i in range(num_vendas):
      vendas.append(float(input("Digite o Valor da Venda:$  ")))
    salario_faixa = [200, 300, 400, 500, 600, 700, 800, 900, 1000]
    salario_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(num_vendas):
      salario = 200 + (0.09 * vendas[i])
    j = int((salario - 200) / 100)
    if j >= len(salario_count):
      j = len(salario_count) - 1
    salario_count[j] += 1
    print("Faixa de Salário\t\tQuantidade de Vendas")
    for i in range(len(salario_faixa)):
      if i == len(salario_faixa) - 1:
        print("$", salario_faixa[i], " e mais\t\t\t", salario_count[i])
      else:
        print("$", salario_faixa[i], " - $", salario_faixa[i + 1] - 1, "\t\t\t", salario_count[i])

if __name__ == "__main__":
    main()'''

'''vendas = []
num_vendas = int(input("Digite a quantidade de vendas realizadas: "))
for i in range(num_vendas):
  vendas.append(float(input("Digite o Valor da Venda:$  ")))
salario_faixa = [200, 300, 400, 500, 600, 700, 800, 900, 1000]
salario_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(num_vendas):
  salario = 200 + (0.09 * vendas[i])
  print(f"$ {salario:.2f}")
  for j in range(len(salario_faixa)):
    if salario < salario_faixa[j]:
      salario_count[j - 1] += 1
      break
print("Faixa de Salário\tQuantidade de Vendas")
for i in range(len(salario_faixa)):
  if i == len(salario_faixa) - 1:
    print(f"$ {salario_faixa[i]} e mais\t\t\t {salario_count[i]}")
  else:
    print(f"$ {salario_faixa[i]} - $ {salario_faixa[i + 1] - 1} \t\t\t {salario_count[i]}")'''

BASE_SALARY = 200
COMMISSION_RATE = 0.09

def calculate_salary(sales_amount):
    return BASE_SALARY + COMMISSION_RATE * sales_amount

def get_salary_range_index(salary):
    salary_range = [200, 300, 400, 500, 600, 700, 800, 900, 1000]
    for i, range_limit in enumerate(salary_range):
        if salary < range_limit:
            return i
    return len(salary_range)

def main():
    sales_amounts = []
    num_of_sales = int(input("Enter number of sales: "))
    for i in range(num_of_sales):
        sales_amounts.append(float(input("Enter the sales amount: ")))

    salary_count = [0] * 9
    for sales_amount in sales_amounts:
        salary = calculate_salary(sales_amount)
        salary_range_index = get_salary_range_index(salary)
        salary_count[salary_range_index] += 1

    print("Salary Range\t\tNumber of Salespeople")
    salary_range = [200, 300, 400, 500, 600, 700, 800, 900, 1000]
    for i, range_limit in enumerate(salary_range):
        if i == len(salary_range) - 1:
            print("$", range_limit, " and over\t\t", salary_count[i])
        else:
            print("$", range_limit, " - $", salary_range[i + 1] - 1, "\t\t\t", salary_count[i])

if __name__ == "__main__":
  main()

