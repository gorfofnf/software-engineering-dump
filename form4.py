import random
A = []
while len(A)<5:
    A.append(random.randint(1,100))
print(A)
rem = int(input("Digite um número para remover."))
if rem in A:
    A.remove(rem)
    print(A)
else:
    print("Esse número não está na lista.")