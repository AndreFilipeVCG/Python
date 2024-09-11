class Times():
    def __init__(self,nome,pontos):
        self.nome = nome
        self.pontos= pontos
    def __str__(self):
        return f"time: {self.nome} pontos : {self.pontos}"
clubes=[]

def mostrar_times():
    print("-----------------TABELA------------------")
    clubesord = sorted(clubes, key=lambda time: time.pontos , reverse=True)
    for x in clubesord:
        print(x)


while True :
    nome = input("digite o nome do time ")
    pontos = int(input("digite o número de pontos "))
    nome = Times(nome,pontos)
    clubes.append(nome)
    print("-----------------------")
    print("time registrado")
    chat = input("digite 1 para registrar outro time e 2 para sair")
    if chat == "2":
        break

mostrar_times()