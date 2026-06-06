# Crie a superclasse `Funcionario` com `nome` e `salario`. Em seguida, crie a subclasse `Gerente`, que herda de `Funcionario` e adiciona um atributo extra chamado `setor`.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def apresentar(self):
        return f"Nome: {self.nome}, Salário: R${self.salario:.2f}"
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor
    
gerente = Gerente("João", 5000.00, "Vendas")
print(gerente.apresentar())
print(f"Setor: {gerente.setor}")
