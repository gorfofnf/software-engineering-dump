forma={
    "GOKU":["SSJ1","SSJ2","SSJ3","SSJ DEUS", "SSJ BLUE","UI"],
    "VEGETA":["SSJ1","SSJ DEUS","SSJ BLUE","ULTRA EGO"]
}
gokucopia=forma["GOKU"]
vegetacopia=forma["VEGETA"]
ataque={
    "GOKU":["KAMEHAMEHA", "GENKIDAMA"],
    "VEGETA":["GALICK GUN","BIG BANG ATTACK"]
}
print("GOKU - Transformações", forma["GOKU"])
print("GOKU - Ataques",ataque["GOKU"])
print("VEGETA - Transformações", forma["VEGETA"])
print("VEGETA - Ataques",ataque["VEGETA"])
unicaforma=[]
unicoataque=[]
for f in forma["GOKU"]:
    if f in forma["VEGETA"]:
        pass
    else:
        unicaforma.append(f)
for j in forma["VEGETA"]:
    if j in forma["GOKU"]:
        pass
    else:
        unicaforma.append(j)
for k in ataque["GOKU"]:
    if k in ataque["VEGETA"]:
        pass
    else:
        unicoataque.append(k)
for l in ataque["VEGETA"]:
    if l in ataque["GOKU"]:
        pass
    else:
        unicoataque.append(l)
print("As formas que apenas um dos personagens possuem são:",unicaforma)
print("Os ataques que apenas um dos personagens possuem são:",unicoataque)