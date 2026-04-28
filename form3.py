A = ['João','Irineu','Zygmunt','George','Hyan']
print(A)
escolha = int(input("Qual nome você deseja remover? Insira o número correspondente à posição dele."))
while escolha<0 or escolha>5:
    print("Opção inválida, tente novamente.")
    escolha = int(input("Qual nome você deseja remover? Insira o número correspondente à posição dele."))
escolha = escolha - 1
A.pop(escolha)
print(A)