def dict2adj(d):
    m = []
    for _, e in d.items():
        m.append(e)
    return m

data = open('data.txt', 'r') 
lines = data.readlines() 
d = {}
k=0
pazienti0=[]
for line in lines: 
    contagi=line.split(' ')
    contagi.pop(0)
    contagi=[int(c) for c in contagi]
    d[k]=contagi
    k=k+1
for k,v in d.items():
    paz0=True
    key=0
    if(len(v)!=0):
        key=k
        for s,t in d.items():
            if key in t:
                paz0=False
                break
    if(paz0==True):
        pazienti0.append(key)



data.close()
print(f"""{d}

{pazienti0}

{dict2adj(d)}

""")

