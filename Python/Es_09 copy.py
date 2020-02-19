import random as rnd
def push(stack,element):
    stack.append(element)
    return stack

def pop(stack):
    element = stack.pop()
    return stack,element

def coppare(mazzo):
    r=rnd.randint(1,52)
    r2=rnd.randint(1,r)
    l2=[]
    l3=[]
    l4=[]
    for i in range(r,52):
        mazzo,element=pop(mazzo)
        l2.append(element)
    
    for i in range(r2,r):
        mazzo,element=pop(mazzo)
        l3.append(element)
        
    l4=mazzo
    mazzo=l3+l4+l2
    return mazzo



class carta(object):

    def __init__(self,seme,numero):
        self.seme = seme
        self.numero = numero
    
    def stampa(self):
        print(f"La carta ha seme {self.seme} con numero {self.numero}.")

mazzo = []
semi = ["C","P","D","F"]

for i in range(1,14):
    for s in semi:
        push(mazzo,carta(s,i))

mazzo = coppare(mazzo)

for i in mazzo:
    i.stampa()


