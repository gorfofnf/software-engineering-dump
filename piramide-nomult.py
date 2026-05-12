degs=int(input("Quantos degraus tem a forma?"))
for i in range(degs):
    q=i+1
    dems=degs-i
    print("")
    for j in range(dems):
        print(" ",end="")
    for l in range(q):
        print("XX",end="")