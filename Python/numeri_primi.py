N=100000
while N>1:
    div,c=2,0
    while div<=N/2 and c==0:
        if N%div==0:
            c+=1
        div+=1
    if c==0:
        print(N)
    N-=1
