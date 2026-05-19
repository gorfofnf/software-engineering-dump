forma={
    "GOKU":["SSJ1","SSJ2","SSJ3","SSJ DEUS", "SSJ BLUE","UI"],
    "VEGETA":["SSJ1","SSJ DEUS","SSJ BLUE","ULTRA EGO"]
}
ataque={
    "GOKU":["KAMEHAMEHA", "GENKIDAMA"],
    "VEGETA":["GALICK GUN","BIG BANG ATTACK"]
}
print("GOKU - Transformações", forma["GOKU"])
print("GOKU - Ataques",ataque["GOKU"])
print("VEGETA - Transformações", forma["VEGETA"])
print("VEGETA - Ataques",ataque["VEGETA"])
perso=str(input("Qual personagem você deseja verificar?")).upper()
esco=str(input("O que você deseja verificar?")).lower()
ver=str(input("O que você deseja verificar se está presente?")).upper()
if esco=="forma":
    if ver in forma[perso]:
        print("O item está presente na lista.")
    else:
        print("Não há item desse nome na lista.")
elif esco=="ataque":
    if ver in ataque[perso]:
        print("O item está presente na lista.")
    else:
        print("Não há item desse nome na lista.")