matrix=[]
n=int(input("numero di righe"))
d={}
k=0
j=0
for i in range(0,n):
    riga=[]
    for k in range (0,n):
        b =input("Inserire situazione")
        if(b=='f'):
            riga.append(False)
        if(b=='t'):
            riga.append(j)
            j=j+1

    matrix.append(riga)
k=0
l=[]
for r in range(0,n):
    for e in range(0,n):
        if(matrix[r][e]==true):
            d[k]=k
            if(r!=0 and r!=n-1 and e!=0 and e!=n-1):
                if(matrix[r-1][e]==True):
                    d[k]=matrix[r-1][e]
                if(matrix[r][e-1]==True):
                    

print(d)
