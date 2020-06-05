import threading
import logging
import time
import random

n_biglietti=100

def cassa():
    global n_biglietti
    
    
    
    l.acquire()
    rnd=random.randint(1,10)
    if  n_biglietti==0:
        print("Biglietti acquistati 0\n")
    elif n_biglietti>0 and rnd<=n_biglietti :
        print("Biglietti acquistati:"+ str(rnd))
        n_biglietti = n_biglietti - rnd
    elif n_biglietti>0 and rnd>n_biglietti :
        print("Biglietti acquistati:" + str(n_biglietti))
        n_biglietti = 0

    print("Biglietti rimanenti:"+str(n_biglietti))
    l.release()

if __name__ == "__main__":

    l=threading.Lock()
    clienti=list()
    i=3
    while i>=0:
        print("la biglietteria apre tra:"+ str(i))
        time.sleep(1)
        i=i-1
        

    for i in range(10):
        logging.info("Padre: creo ed avvio thread %d",i)
        x=threading.Thread(target=cassa)
        clienti.append(x)
        x.start()

    for i, t  in enumerate(clienti):
        logging.info("Padre: prima dell'attesa del thread %d.",i)
        t.join()
        logging.info("Padre: thread %d terminato",i)