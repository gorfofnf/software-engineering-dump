media= 6.0
while True:
    nota1 = float(input("Qual foi sua nota na primeira avaliação."))
    if nota1 < 0 or nota1 > 5:
        print("Por favor, informe um valor válido entre 0 e 5.")
    else:
        break
while True:
    nota2 = float(input("Qual foi sua nota na segunda avaliação?"))
    if nota2 < 0 or nota2 > 5:
        print("Por favor, informe um valor válido entre 0 e 5.")
    else:
        break
if nota1+nota2>=media:
    print("Você foi aprovado. Parabéns!! :D")
elif media>nota1+nota2>1:
    notarec= float(input("Qual foi sua nota de recuperação?"))
    if notarec>=nota1:
        media1=notarec+nota2
        if media1>=media:
            print("Você foi aprovado. :)")
        else:
            print("Você foi reprovado, infelizmente.")
    elif notarec>=nota2:
        media2=notarec+nota1
        if media2>=media:
            print("Você foi aprovado. :)")
        else:
            print("Você foi reprovado, infelizmente.")
else:
    print("Você foi reprovado, infelizmente.")