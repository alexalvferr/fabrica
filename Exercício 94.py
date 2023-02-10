import random
idades = []
alturas = []
aluno_13 = []
media_13 = []

for i in range(30):
    num_aleat = idades.append(random.randrange(1, 20))
    num_aleat2 = alturas.append(random.randrange(50, 200))

for i in range(30):
    if idades[i] > 13:
        aluno_13.append(alturas[i])

media = sum(aluno_13) / len(aluno_13)

for i in range(len(aluno_13)):
    if aluno_13[i] < media:
        media_13.append(aluno_13[i])

print(f'A idade dos alunos são: {idades},\n A altura dos alunos em cm são: {alturas}')
print(f'Foram {len(aluno_13)} alunos com idade acima de 13 anos que são: {aluno_13}')
print(f'A média de altura desses {len(aluno_13)} alunos é: {media:.2f}cm')
print(f'Foram {len(media_13)} alunos com mais de 13 anos possuem altura inferior à média de altura: {media_13}')
