personagens = []
#PERSONAGENS
class Character:
    def __init__(self,nome,nivel,elemento):
        self.nome=nome
        self.nivel=nivel
        self.elemento=elemento
    def __str__(self):
         return f" {self.nome} - {self.nivel} - {self.elemento}"
         

#REGISTRAR OS PERSONAGENS
def registrar():
    while(True):    
        stats =input("1- registrar   2- excluir   3- listar 4- sair")
        if stats == "1":
            name =input("Digite o nome do personagem")
            level = input("digite o nivel do personagem")
            element=input("digite o elemento")
            personagem = Character(name,level,element)
            personagens.append(personagem)

        if stats == "2":
            name = input("digite o nome do personagem que voce deseja excluir:")
            for x in personagens:
                if x.nome == name:
                    personagens.remove(x)
            print(f"personagem {name} foi excluido")
        if stats == "3":
            for x in personagens:
                 print(x)
        if stats == "4":
            break


registrar()
