class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, delta):
        self.delta = delta
        self.velocidade += delta
        print(f"Velocidade aumentada em {self.delta} Km/h")
        print(f"Velocidade atual: {self.velocidade} Km/h")
    
    def frear(self, delta):

        if delta > self.velocidade:
            self.delta = delta
            self.velocidade = 0
        
        else:
            self.delta = delta
            self.velocidade -= delta

        print(f"Velocidade reduzida em {self.delta} Km/h")
        print(f"Velocidade atual: {self.velocidade} Km/h")

marca = str(input("Digite a marca do carro: "))
modelo = str(input("Digite o modelo do carro: "))

carro = Carro(marca, modelo)

while True:
    try:
        print("Escolha uma opção:")
        print("Opção 1: Acelerar")
        print("Opção 2: Frear")
        print("Opção 3: Sair")

        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            delta = int(input("Digite o valor da velocidade a ser acelerado: "))
            carro.acelerar(delta)
        
        elif opcao == 2:
            delta = int(input("Digite o valor da velocidade a ser freado: "))
            carro.frear(delta)
        
        elif opcao == 3:
            break

    except ValueError:
        print("Erro! Entrada inválida!")