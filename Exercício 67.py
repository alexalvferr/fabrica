print("Digite seu Usuário e Senha: ")

usuario=str(input("Usuário: "))
senha=(input("Senha: "))
while usuario==senha:

	print("ERRO:O USUÁRIO NÃO PODE SER IGUAL A SENHA, TENTE NOVAMENTE")
	usuario=str(input("usuário--> "))
	senha=str(input("senha-->"))

else:
	print("Cadastro Efetuado Com Sucesso")
  