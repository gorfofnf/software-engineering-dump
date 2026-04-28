# 5)
listapar = []
listaimpar = []
listafull =[]
while len(listafull)<=4:
    num = int(input("Informe um número."))
    listafull.append(num)
    if num%2 ==0:
        listapar.append(num)
    else:
        listaimpar.append(num)
listafull.sort()
soma = sum(listafull)
media= soma/len(listafull)
print("A partir dos números informados, foi feita a lista:", listafull)
if len(listapar)!=0:
    print("O maior valor par é", max(listapar))
if len(listaimpar)!=0:
    print("O menor valor ímpar é", min(listaimpar))
print("A soma de todos os elementos é",soma,"e a média é",format(round(media,2)),".")