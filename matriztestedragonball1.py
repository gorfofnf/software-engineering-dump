forma={
    "GOKU":["SSJ1","SSJ2","SSJ3","SSJ Deus", "SSJ Blue"],
    "VEGETA":["SSJ1","SSJ Deus","SSJ Blue"]
}
ataque={
    "GOKU":["Kamehameha", "Genkidama"],
    "VEGETA":["Galick Gun","Big Bang Attack"]
}
print("GOKU - Transformações", forma["GOKU"])
print("GOKU - Ataques",ataque["GOKU"])
print("VEGETA - Transformações", forma["VEGETA"])
print("VEGETA - Ataques",ataque["VEGETA"])
escolha=str(input("Você deseja remover ou adicionar itens?")).upper()
if escolha=="ADICIONAR":
    perso=str(input("Qual personagem você seleciona?")).upper()
    nova=str(input("Qual forma você deseja adicionar?"))
    if nova in forma[perso]:
        print("Essa forma já está presente.")
    else:
        forma[perso] += [nova]
    nova1=str(input("Qual ataque você deseja adicionar?"))
    if nova1 in ataque[perso]:
        print("Esse ataque já está presente.")
    else:
        ataque[perso] += [nova1]
    print(perso,"- Transformações", forma[perso])
    print(perso,"- Ataques",ataque[perso])
elif escolha=="REMOVER":
    perso = str(input("Qual personagem você seleciona?")).upper()
    rem = str(input("Qual forma você deseja retirar?"))
    if rem not in forma[perso]:
        print("Essa forma já não está presente.")
    else:
        forma[perso].remove(rem)
    rem1 = str(input("Qual ataque você deseja retirar?"))
    if rem1 not in ataque[perso]:
        print("Esse ataque já não está presente.")
    else:
        ataque[perso].remove(rem1)
    print(perso, "- Transformações", forma[perso])
    print(perso, "- Ataques", ataque[perso])