import threading
import logging
import time

def fn_thread(val):
    logging.info("Thread %s: inizio",val)
    time.sleep(2)
    logging.info("Thread %s: fine",val)


if __name__ == "__main__":
    format = "%(asctime)s : %(message)s" # inizializzazione log
    logging.basicConfig(format=format, level=logging.INFO, datefmt= "%H,%M,%S")

    logging.info("Padre: creazione di un thread")

    x=threading.Thread(target=fn_thread, args=(1,))

    logging.info("Padre: avvio thread")
    x.start()

    logging.info("Padre: aspetto la terminazione del thread")
    x.join()

    logging.info("Padre: fine")