class ClienteBancario:
    def __init__(self, titular):
        
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):

        self.saldo += valor
        print(f"Valor depositado: {valor}. Saldo: {self.saldo}")

    def sacar(self, valor):

        if valor > self.saldo:
            print("Erro! Saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"Valor sacado: {valor}. Saldo: {self.saldo}")

titular = str(input("Digite o nome do titular: "))

cliente = ClienteBancario(titular)

while True:
    try:
        print("Digite uma opção:")
        print("Opção 1: Depositar")
        print("Opção 2: Sacar")
        print("Opção 3: Sair")

        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            valor = float(input("Digite o valor a ser depositado: "))
            cliente.depositar(valor)

        elif opcao == 2:
            valor = float(input("Digite o valor a ser sacado: "))
            cliente.sacar(valor)

        elif opcao == 3:
            break

    except ValueError:
        print("Erro! Entrada inválida")