atletas = []
while True:
    nome = str(input("Digite o nome do atleta (ou enter para encerrar o programa): "))
    if nome == "":
        break
    atleta = {
        "nome": nome,
        "apresentações": [],
        "media": 0,
        "melhor_apresentação": 0,
        "pior_apresentação": 0,
    }
    for i in range(7):
        atleta.get("apresentações").append(float(input(f"Nota da {i+1}º apresentação: ")))
    atleta.get("apresentações").sort()
    atleta["pior_apresentação"] = atleta.get("apresentações").pop(0)
    atleta["melhor_apresentação"] = atleta.get("apresentações").pop()
    atleta["media"] = sum(atleta.get("apresentações")) / 5
    print(f"\nMelhor apresentação: {atleta.get('melhor_apresentação'):.2f} "
        f"\nPior apresentação: {atleta.get('pior_apresentação'):.2f} "
        f"\nMédia dos demais apresentações: {atleta.get('media'):.2f} \n")
    atletas.append(atleta)

print("\n\nResultado final")
for atleta in atletas:
    print(f"{atleta.get('nome')}: {atleta.get('media'):.2f} ")