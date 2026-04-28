# 1, 2 e 3)
A = []
while len(A)<=9:
    num = int(input ('Informe o número:'))
    A.append(num)
A.sort()
print(A)
print("O menor valor é", A[0])
print("O maior valor é", A[9])