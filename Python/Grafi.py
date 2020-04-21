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
    
    def heavyOrientedMatrix():
    nodes = int(input("Inserire numero di nodi: "))

    matrix = []

    for i in range(0,nodes):
        heavy_neighbor = [n for n in input(f"Inserisci i nodi adiacenti a {i} con il peso (2|32,): ").split(",")]
        column = [0 for n in range(0,nodes)]

        neighboor=[]
        heavy=[]
            
        for k in heavy_neighbor:
            n,h = k.split("|")
            neighboor.append(int(n))
            heavy.append(int(h))
        print(neighboor,heavy,column)
        for p,n in enumerate(neighboor):
            column[n] = heavy[p]

        matrix.append(column)

    return matrix


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

