class Pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0

class Funcionario:
    def __init__(self, salario, nome):
        self.nome = nome
        self.salario = salario

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area (self):
        return self.base * self.altura
    def parimetro (self):
        return 2 * (self.base + self.altura)
    def diagonal(self):
        return (self.base**2 + self.altura**2)**0.5
