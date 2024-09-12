from random import randint

print("tente adivinhar o número aleatório entre 1 a 100, você tem apenas 5 chances")
num = 0
aleatorio = randint(1,100)
perde = False

for x in range(5):
    num = int(input("digite : "))
    if num > aleatorio:
        print("digite um número menor")
        perde=True
    elif num < aleatorio:
        print("digite um número maior")
        perde=True
    if num == aleatorio :
       print("voce venceu")
       perde=False
       break
    
if perde == True:
    print("você perdeu!")
    print("O número era:",aleatorio)

     

