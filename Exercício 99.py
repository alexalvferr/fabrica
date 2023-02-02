v1 = []
v2 = []
v3 = []
numero = 0
for numero in range(5):
    v1.append(int(input("Digite um número para o Vetor 01: ")))
    
for numero in range(5):
    v2.append(int(input("Digite um número para o Vetor 02: ")))
    
for numero in range(5):
    v3.append(v1[numero])
    v3.append(v2[numero])

print(f'O Vetor 03 é: {v3}')