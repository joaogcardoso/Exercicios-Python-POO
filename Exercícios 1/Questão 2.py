class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

nome = str(input("Digite seu nome: "))
idade = int(input("Digite a idade: "))

pessoa = Pessoa(nome, idade)

pessoa.apresentar()
