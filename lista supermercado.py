mercado=[]

item = input("digite o item da sua lista")

while True:
    
    if item == "fim":
        break
    mercado.append(item)
    item = input("digite o item da sua lista")


cont=1

for x in range(len(mercado)):
    
    print(cont ,":", mercado[x])
    cont=cont+1