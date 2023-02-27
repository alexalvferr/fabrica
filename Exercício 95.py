usuarios = []
uso_dados =[]
uso_dados_MB = []
percentual_MB = []

with open("C:\Users\Alexandre\Desktop\usuários.txt", "r") as arquivo: #abrindo o arquivo txt do exercicio é necessario criar o arquivo
    for i in range(6):
        nome = arquivo.readline(15)
        nome = nome.replace(' ','') #remove os espaços em branco
        dados = arquivo.readline(18)
        dados = dados.replace(' ','') #remove os espaços em branco
        dados = int(dados.replace('\n','')) #remove os '\n' e transforma em inteiro
        usuarios.append(nome)
        uso_dados.append(dados)

def conversor_bytes(uso_dados):
    for i in range(len(uso_dados)):
        kilobyte = round(uso_dados[i] / 1024, 2)
        megabyte = round(kilobyte / 1024, 2)
        uso_dados_MB.append(megabyte)
            
def calc_percent(uso_dados_MB):
    for i in range(len(uso_dados_MB)):
        percentual = round(((100 * uso_dados_MB[i]) / sum(uso_dados_MB)), 2)
        percentual_MB.append(percentual)

def impressao(percentual_MB,usuarios):
    with open("C:\Users\Alexandre\Desktop\ relatório.txt", 'w') as arquivo: #criando o arquivo relatorio txt
        arquivo.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
        arquivo.write('-' * 72)
        arquivo.write('\n')
        arquivo.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
        arquivo.write('\n')
        for i in range(len(usuarios)):
            arquivo.write(f'{i+1:<4} {usuarios[i]:<10} {uso_dados_MB[i]:>11} MB {percentual_MB[i]:>17}%\n')
        total = sum(uso_dados_MB)
        media = round(total / len(uso_dados_MB), 2)
        arquivo.write('\n')    
        arquivo.write(f'Espaço total ocupado: {total} MB\nEspaço médio ocupado: {media} MB')

conversor_bytes(uso_dados)
calc_percent(uso_dados_MB)
impressao(percentual_MB,usuarios)
