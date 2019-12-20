def push(stack,element):
    stack.append(element)
    return stack

def pop(stack):
    element = stack.pop()
    return stack,element

pila= [1,2,3,"ciao"]
pila=push(pila,5)
print(pila)
pila,_ = pop(pila)
print(pila)