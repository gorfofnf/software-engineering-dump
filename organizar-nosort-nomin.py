L=[1,3,5,7,9,2,4,6,8,10]
org=[]
print(L)
while L:
    meno=L[0]
    for k in L:
        if k<meno:
            meno=k
    org.append(meno)
    L.remove(meno)
print(org)