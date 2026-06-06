class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    
    def detalhes(self, nome, especie):
        print(f"Nome: {nome} \n Espécie: {especie}")

nome = str(input("Digite o nome do animal: "))
especie = str(input("Digite a especie do animal: "))

animal = Animal(nome, especie)

animal.detalhes(nome, especie)