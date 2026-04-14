num_alunos=0
media_turma=0
while num_alunos<50:
    nota1= float(input("Qual foi a nota da primeira prova?"))
    nota2= float(input("Qual foi a nota da segunda prova?"))
    nota3= float(input("Qual foi a nota da terceira prova?"))
    nota4= float(input("Qual foi a nota da quarta prova?"))
    media=(nota1+nota2+nota3+nota4)/4
    print("A media desse aluno foi", media)
    if media<7:
        print("Esse aluno não foi aprovado.")
    else:
        print("Esse aluno foi aprovado.")
    while media<0 or media>10:
        print("Tenha em mente que as notas vão somente de 0 até 10, tente novamente.")
        nota1 = float(input("Qual foi a nota da primeira prova?"))
        nota2 = float(input("Qual foi a nota da segunda prova?"))
        nota3 = float(input("Qual foi a nota da terceira prova?"))
        nota4 = float(input("Qual foi a nota da quarta prova?"))
        media = (nota1 + nota2 + nota3 + nota4) / 4
        print("A media desse aluno foi", media)
        if media < 7:
            print("Esse aluno não foi aprovado.")
        else:
            print("Esse aluno foi aprovado.")
    else:
        num_alunos+=1
        media_turma+=media
        if num_alunos==50:
            break
media_final=media_turma/50
print("A média da turma é",media_final)