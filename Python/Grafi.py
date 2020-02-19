Matrix=[]
Nodi=int(input("inserire n° nodi"))

for i in range(0,Nodi):
    col=input("inserire collegamenti")
    collegamenti=int(col.split(","))
    colonna=[0 for i in range(0,Nodi)]
    for n in collegamenti:
        colonna[n]=1

    Matrix.append(colonna)