num1=0
num2=1
num3=num1+num2
num4=num2+num3
limite=int(input("Insira um valor limitrófe."))
atual=4
if limite==1:
    print(num1)
elif limite==2:
    print(num1,num2)
elif limite==3:
    print(num1,num2,num3)
elif limite==4:
    print(num1,num2,num3,num4)
else:
    print(num1)
    print(num2)
    while atual <= limite:
        num1 = num3
        num2 = num4
        num3 = num1 + num2
        num4 = num2 + num3
        print(num1)
        print(num2)
        atual = atual + 1
        if atual > limite-1:
            break


