from math import trunc

num=float(input("Qual o valor?"))
mun2=int(trunc(num))
res=int(num%2)
if num==0:
    print("O valor é zero.")
else:
    if num>mun2 and num>0:
        print("O valor é decimal.")
    elif num<0 and mun2>num:
        print("O valor é decimal.")
    else:
        print("O valor é inteiro.")
    if res == 0:
        print("O valor informado é par.")
    else:
        print("O valor informado é ímpar.")
    if num > 0:
        print("O valor é positivo.")
    else:
        print("O valor é negativo")
