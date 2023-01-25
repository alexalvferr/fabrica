print("Digite seu Usuário e Senha: ")

login = str(input("Usuário: "))
senha = (input("Senha: "))
while login == senha:

	print("ERRO:O USUÁRIO NÃO PODE SER IGUAL A SENHA, TENTE NOVAMENTE")
	login = str(input("usuário: "))
	senha = str(input("senha: "))

else:
	print("Cadastro Efetuado Com Sucesso")
  
