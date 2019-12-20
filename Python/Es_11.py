import random as rnd
def push(stack,element):
    stack.append(element)
    return stack

def pop(stack):
    element = stack.pop()
    return stack,element

def coppaMazzo(stack):
    pos=rnd.randint(0,len(stack)-1)
    stack = stack[pos:len(stack)] + stack[0:pos]
    return stack

def shuffle(stack):
    stack1=[]
    while stack!=[]:
        stack=coppaMazzo(stack)
        stack1.append(stack.pop())
    return stack1


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

for i in mazzo:
    i.stampa()


mazzo=coppaMazzo(mazzo)

print("\n\nmazzo coppato:\n")

for i in mazzo:
    i.stampa()

mazzo=shuffle(mazzo)

print("\n\nmazzo mischiato:\n")

for i in mazzo:
    i.stampa()

