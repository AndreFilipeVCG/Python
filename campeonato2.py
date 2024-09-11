from collections import OrderedDict
times = { 

}

#pegar o time e os pontos
def get_team():
    while(True):
        nome =input("digite o nome do time")
        pts = input("digite o número de pontos")
        stats = input("digite 1 para continuar ou nada para sair ir para o resultado") 
        times[nome]=int(pts)
        if stats !="1":
            break
#ordenar 

   

#mostrar
def show(lista):
    cont = 1
    for x , y in lista.items():
        print(f"{cont} - {x} - {y} ")
        cont =cont+1

#programa
get_team()
ordered = OrderedDict(sorted(times.items() ,key=lambda item : item[1] , reverse=True))
show(ordered)