import numpy as np
while True:
    res=int(input("Você gostaria de uma matriz composta de 0(0), 1(1) ou uma matriz identidade?(2)"))
    if 0>res or res>2:
        print("Resposta inválida, tente novamente.")
    else:
        break
if res==0:
    lin0=int(input("Quantas linhas você deseja?"))
    col0=int(input("Quantas colunas você deseja?"))
    matriz0=np.zeros((lin0,col0))
    print(matriz0)
elif res==1:
    lin1=int(input("Quantas linhas você deseja?"))
    col1=int(input("Quantas colunas você deseja?"))
    matriz1=np.ones((lin1,col1))
    print(matriz1)
else:
    ide=int(input("Qual o tamanho da matriz?"))
    matriziden=np.eye(ide)
    print(matriziden)   