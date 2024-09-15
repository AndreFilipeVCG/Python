import requests

url ="https://euro-20242.p.rapidapi.com/"
endpoint="players"


headers = {
	"x-rapidapi-key": "e50414ebd3msh8b85c3aea7555b3p1b6b1djsn40a8b09647c1",
	"x-rapidapi-host": "euro-20242.p.rapidapi.com"
}

players = requests.get(url+endpoint, headers=headers)


r = players.json()

#teams
germany_team=[]
portugal_team=[]
england_team=[]

tamanho = len(r)
for x in range(tamanho):
    if r[x]['team']['name'] == "germany":
        germany_team.append(x)
    if r[x]['team']['name'] == "portugal":
        portugal_team.append(x)
    if r[x]['team']['name'] == "england":
        england_team.append(x)

 # print(f"{r[x]['name']} - {r[x]['team']['name']}")

for x in germany_team:
    with open("C:\\Users\\franc\\OneDrive\\Área de Trabalho\\prog\\python\\workspace\\programador_junior\\seleção\\germany.txt","a") as arq:
        arq.write(f"{r[x]['name']} - {r[x]['team']['name']} - {r[x]['position']}\n")
        arq.write("\n")
for x in england_team:
    with open("C:\\Users\\franc\\OneDrive\\Área de Trabalho\\prog\\python\\workspace\\programador_junior\\seleção\\england.txt","a") as arq:
        arq.write(f"{r[x]['name']} - {r[x]['team']['name']} - {r[x]['position']}\n")
        arq.write("\n")
for x in portugal_team:
    with open("C:\\Users\\franc\\OneDrive\\Área de Trabalho\\prog\\python\\workspace\\programador_junior\\seleção\\portugal.txt","a") as arq:
        arq.write(f"{r[x]['name']} - {r[x]['team']['name']} - {r[x]['position']}\n")
        arq.write("\n")




   
