myList = []
mySecondList = []
cond = True

while cond:
    x =  input("inserire un valore:")
    myList.append(x)
    
    r = input("vuoi inserire un altro valore? y/n\n")

    if r == "y" or r == "Y":
        continue
    else:
        cond = False


n = int(input("len: "))
print(n)

for word in myList:
    print(word+" :"+str(len(word)))
    if len(word) >= n:
        mySecondList.append(word)
    else:
        print("troppo piccolo")


print(mySecondList)