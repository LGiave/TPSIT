matrix=[]
n=int(input("numero di righe"))
d={}
j=1
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
k=1

for r in range(0,n):
    for e in range(0,n):
        l=[]
        if(matrix[r][e]!=False):
            if(r-1>=0):
                if(matrix[r-1][e]!=False):
                    l.append(matrix[r-1][e])
            if(e-1>=0):
                if(matrix[r][e-1]!=False):
                    l.append(matrix[r][e-1])
            if(r+1< len(matrix)):
                if(matrix[r+1][e]!=False):
                    l.append(matrix[r+1][e])
            if e+1<len(matrix):
                if(matrix[r][e+1])!=False:
                    l.append(matrix[r][e+1])
            
            d[k]=l
            k=k+1

print(d)
