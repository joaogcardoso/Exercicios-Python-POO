# Defina a superclasse `Publicacao` com um método `exibir`. Crie as subclasses `Texto` e `Foto` com implementações diferentes de `exibir`. Em uma lista, adicione objetos
# de ambas e chame o método `exibir` de cada um.

class Publicacao:
    def exibir(self):
        print("Exibindo uma publicação.")

class Texto(Publicacao):
    def exibir(self):
        print("[TEXTO]: Texto do post")

class Foto(Publicacao):
    def exibir(self):
        print("[FOTO]: Imagem de uma paisagem")

feed = [Texto(), Foto()]

for post in feed:
    post.exibir()
