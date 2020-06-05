import threading
import logging
import time
import random
MAX=2

c_presenti = 0
n_clienti = 100
serviti=0

def cassa():

    global n_clienti
    global c_presenti
    global serviti

    n_clienti= n_clienti - 1
    l.acquire()
    if(c_presenti<MAX):
        serviti=serviti+1
        c_presenti=c_presenti + 1
        conto = random.randint(5,100)
        print(F"\nTotale spesa:{conto}")
    else:
        print("Impossibile entrare clienti nel supermercato al limite")
   
    l.release()
    t=random.randint(0,1)
    time.sleep(t)
    c_presenti=c_presenti-1

if __name__ == "__main__":

    l=threading.Lock()
    clienti=list()

    for i in range(100):
        logging.info("Padre: creo ed avvio thread %d",i)
        x=threading.Thread(target=cassa)
        clienti.append(x)
        x.start()

    for i, t  in enumerate(clienti):
        logging.info("Padre: prima dell'attesa del thread %d.",i)
        t.join()
        logging.info("Padre: thread %d terminato",i)

    print(F"Clienti serviti: {serviti}")
    