import random
quan=int(input("Quantos elementos na lista?"))
papa=[]
for i in range(quan):
    papa.append(random.randint(1,100))
dura=len(papa)
print(papa)
nova=[]
while dura>len(nova):
    ja=min(papa)
    nova.append(ja)
    papa.remove(ja)
print(nova)