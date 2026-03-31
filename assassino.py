print("Você irá responder questões para concluir sua relação com o recente assasinato. Responda com honestidade.")
while True:
    res1= int(input("Você telefonou para a vítima? 1 para sim e 0 para não."))
    if res1<0 or res1>1:
        print("Insira um valor válido.")
    else:
        break
while True:
    res2= int(input("Você esteve no local do crime? 1 para sim e 0 para não."))
    if res2<0 or res2>1:
        print("Insira um valor válido.")
    else:
        break
while True:
    res3= int(input("Você mora perto da vítima? 1 para sim e 0 para não."))
    if res3<0 or res3>1:
        print("Insira um valor válido.")
    else:
        break
while True:
    res4= int(input("Você devia para a vítima? 1 para sim e 0 para não."))
    if res4<0 or res4>1:
        print("Insira um valor válido.")
    else:
        break
while True:
    res5= int(input("Você já trabalhou com a vítima."))
    if res5<0 or res5>1:
        print("Insira um valor válido.")
    else:
        break
resultado= res1+res2+res3+res4+res5
if resultado==5:
    print("Você foi classificado como o assassino, renda-se pacificamente ou força será usada.")
elif resultado==3 or resultado==4:
    print("Você foi classificado com cúmpilce do assassino, e portanto será preso, mas sua testemunha será vital.")
elif resultado==1 or resultado==5:
    print("Você foi classificado como suspeito. Seu involvimento no caso é possível, mas você será preso somente preventivamente.")
else:
    print("Você é inocente. Não se preocupe com qualquer envolvimento seu nesse caso.")