#Por todas as definições eu fiz algo de errado, mas ficou muito bacana o resultado.
degs=int(input("Quantos degraus tem a forma?"))
for i in range(degs):
    q=i+1
    dems=degs-i
    print("")
    for l in range(q):
        print(" "*dems,"XX",end="")