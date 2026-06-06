class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.nota = nota
        self.notas.append(nota)

    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)
        print(f"Notas: {self.notas}")
        print(f"Média: {media}")

    
nome = str(input("Digite a nome do estudante: "))
matricula = str(input("Digite a matrícula do estudante: "))

estudante = Estudante(nome, matricula)

while True:
    try:
        print("Escolha uma opção: ")
        print("Opção 1: Adicionar nota")
        print("Opção 2: Calcular média")
        print("Opção 3: Sair")

        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            nota = float(input("Digite a nota do aluno a ser inserida: "))
            estudante.adicionar_nota(nota)

        if opcao == 2:
            estudante.calcular_media()

        if opcao == 3:
            break

    except ValueError:
        print("Erro! Entrada inválida!")