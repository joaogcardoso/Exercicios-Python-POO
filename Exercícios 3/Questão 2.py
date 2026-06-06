# Crie a superclasse `Ave` com um método `voar`. Crie a subclasse `Pinguim` que sobrescreve o método `voar` para informar que esta ave em particular não voa.

class Ave:
    def voar(self):
        print("Voando")
    
class Pinguim(Ave):
    def voar(self):
        print("Pinguins não podem voar.")

ave_comum = Ave()
pinguim = Pinguim()

ave_comum.voar()
pinguim.voar()