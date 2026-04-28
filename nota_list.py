# 4)
alunos = int(input("Informe o número de alunos:"))
alunos = alunos - 1
listanotas_media = []
listanotas_rec = []
while (len(listanotas_media)+ len (listanotas_rec))<=alunos:
    nota = int(input("Informe a nota do aluno:"))
    while nota<0 or nota>100:
        print("Valor inválido.")
        nota = int(input("Informe a nota do aluno:"))
    if nota<60:
        listanotas_rec.append(nota)
    else:
        listanotas_media.append(nota)
print("Há",len(listanotas_media), "alunos aprovados.")
listanotas_media.sort()
print(listanotas_media)
print("Há", len(listanotas_rec), "alunos em recuperação.")
listanotas_rec.sort()
print(listanotas_rec)