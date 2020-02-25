def user2adj():
    Matrix=[]
    Nodi=int(input("inserire n° nodi"))

    for i in range(0,Nodi):
        collegamenti=[int(k) for k in input(f"Inserire collegamenti di {i}: ").split(",")]
        colonna=[0 for i in range(0,Nodi)]
        for n in collegamenti:
            if(n!= -1):
                colonna[n]=1

        Matrix.append(colonna)
    return Matrix
    

def adj2dict(Matrix):
    d={}
    for l in range(0,len(Matrix)):
        d[l]=Matrix[l]
    return d

def dict2adj(d):
    m=[]
    for _,v in d.items():
        m.append(v)
    print(m)
    return m

if __name__ == "__main__":
    dict2adj(adj2dict(user2adj()))

