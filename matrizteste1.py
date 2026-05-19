import numpy as np
matriz1=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
for i in matriz1:
    print(i)
while True:
    resposta=int(input("Deseja retirar um número? 1 para sim e 2 para não."))
    if resposta<1 or resposta>2:
        print("Resposta inválida, tente novamente.")
    else:
        break
if resposta==1:
    lin=int(input("Qual a linha do número?"))-1
    col=int(input("Qual a coluna do número?"))-1
    num=int(input("Por fim, qual número você deseja botar no lugar?"))
    matriz1[lin][col]=num
    print(matriz1)
    print(len(matriz1))
elif resposta==2:
    print("vro ToT")