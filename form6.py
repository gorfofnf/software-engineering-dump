import random
A = []
while len(A)<10:
    A.append(random.randint(1,100))
print(A)
A.sort()
num = 0
B = []
while len(B)<5:
    B.append(A[num])
    num+=1
print(B)