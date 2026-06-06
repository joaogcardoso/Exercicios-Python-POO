class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

nome = str(input("Digite seu nome: "))
idade = int(input("Digite a idade: "))

pessoa = Pessoa(nome, idade)

print(pessoa.nome)
print(pessoa.idade)
