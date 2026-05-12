import random
lin=int(input("Quantos elementos na lista?"))
L=[]
for j in range(lin):
    L.append(random.randint(1,100))
print(L)
org=[]
while L:
    meno=L[0]
    for k in L:
        if k<meno:
            meno=k
    org.append(meno)
    L.remove(meno)
print(org)