alunos={

}

num= int(input("digite o número de alunos"))

for x in range(num):
    
    print("------------------------------")
    matricula=input("digite a matricula : ")
    nome=input("digite o nome : ")
    curso=input("digite o curso : ")
    alunos.update({matricula : [nome , curso]})
    


for k,v in alunos.items():
    print(k ,":" ,v[0],v[1])

#tudo certo
tam = int(len(alunos)) 
cont=0
esta=False
busca = ""
while busca != "fim":
    for k,v in alunos.items():  
        esta==False
        if busca == k:
            print(k ,":" ,v[0],v[1]) 
            esta= True
        
        if cont == tam and esta == False:
            print("valor não esta na lista")
            cont= 0
        cont += 1
           
    busca = input("digite a matrícula de algum estudante, digite fim caso deseje sair do programa : ") 

