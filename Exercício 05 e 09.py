nome_aluno = str(input("Digite o nome do aluno: "))
disciplina = str(input("Digite a disciplina: "))
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media = (n1 + n2 + n3)/3
print("Aluno: \n", nome_aluno)
print("Disciplina: \n", disciplina)
print(f"Qual é a primeira nota: {n1:.2f}")
print(f"Qual é a segunda nota: {n2:.2f}")
print(f"Qual é a terceira nota: {n3:.2f}")
print(f"Qual é a média do aluno: {media:.2f}")
if media >= 6.0:
    print("O aluno foi APROVADO")
else:
    print("O aluno está REPROVADO")