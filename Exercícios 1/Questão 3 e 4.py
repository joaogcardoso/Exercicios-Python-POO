class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        area = self.largura * self.altura
        return area
    
largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

retangulo = Retangulo(largura, altura)

print(retangulo.calcular_area())