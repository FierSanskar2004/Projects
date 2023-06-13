def chekk(ck):
    for op in ck:
        if op==0:
            return 99
            break
        if op==1:
            return 100
            break


n=int(input("No of data : "))
x=[]
y=[]
m=0
l=0
i=0

while 1:
    for i in range(0,n):
        m=int(input("X = "))
        l=float(input("P(X) = "))
        x.append(m)
        y.append(l)

    sume=0
    for j in y:
        sume+=j
    
    ck=[]
    for cc in y:
        if cc<0 or cc>1:
            ck.append(0)
        else:
            ck.append(1)

    chekk(ck)

    if sume==1 and chekk(ck)==100:
        break
    else:
        x.clear()
        y.clear()
        ck.clear()
        print("Error! Try Again!")
        continue

sume=0
hmm=0

for oi in x:
    for ai in y:
        hmm=oi*ai
        sume=sume+hmm

print("E(",n,") = ",hmm)
