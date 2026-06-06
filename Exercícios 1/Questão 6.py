class ClienteBancario:
    def __init__(self, titular):
        
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):

        self.valor = valor
        self.saldo += valor

    def sacar(self, valor):

        if valor > self.saldo:
            print("Erro! Saldo insuficiente!")
        else:
            self.valor = valor
            self.saldo -= valor
    
    def __str__(self, titular):
        print(f"Titular: {titular} \n Saldo: {self.saldo}")

titular = str(input("Digite o nome do titular: "))

cliente = ClienteBancario(titular)

while True:
    try:
        print("Digite uma opção:")
        print("Opção 1: Depositar")
        print("Opção 2: Sacar")
        print("Opção 3: Saldo")
        print("Opção 4: Sair")

        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            valor = float(input("Digite o valor a ser depositado: "))
            cliente.depositar(valor)

        elif opcao == 2:
            valor = float(input("Digite o valor a ser sacado: "))
            cliente.sacar(valor)

        elif opcao == 3:
            cliente.__str__(titular)

        elif opcao == 4:
            break

    except ValueError:
        print("Erro! Entrada inválida")