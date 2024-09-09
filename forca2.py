
#CRIAR LISTA

palavra=["P","I","E","R","R","E"]
hide=["-","-","-","-","-","-"]
#PEDIR PARA O JOGADOR DIGITAR UMA LETRA

def pedir_letra():
    letra = input("digite uma letra").upper()
    return letra

#CHECAR SE A LETRA ESTA NA PALAVRA , CASO ESTEJA SUBSTITUA A LETRA PELO TRAÇO
def checar(let):
    cont = 0
    for x in palavra:
        cont+=1
        if x==let:
            hide[cont-1] = let
    for x in hide:
        print(x , end="")
    print('\n')



#inicio
for x in hide:
    print(x , end="")    
print('\n')

while (True):
    checar(pedir_letra())
    if hide == palavra:
        break

#QUANDO TODA A PALAVRA FOR REVELADA MOSTRE AO JOGADOR VOCE GANHOU , A PALAVRA É : 
    
print( "Voce ganhou!!!")