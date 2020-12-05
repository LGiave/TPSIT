import threading
import sqlite3
import socket
import logging

ip='127.0.0.1'
porta=8000

class Thread(threading.Thread):
    def __init__(self, connection,server):
        self.connection=connection 
        self.server=server

    def run(self):
        while(True):
            data=self.connection.recv(4096)
            step=query(data)
            send_alphabot(self.server,self.connection, step)

def con_alphabot(server):
    connect,_ = server.accept() 
    return connect 

def send_alphabot(server, connessione, data):
    data= data.encode()
    connessione.sendall(data)

def query(data):
    dati=data.decode()
    conn = sqlite3.connect('percorsi.db')
    cursor = conn.cursor()
    x,y=dati.split(',')
    print(f'SELECT percorso FROM (inizio_fine INNER JOIN percorsi ON (inizio_fine.id_percorso = percorsi.id) INNER JOIN luoghi s ON (id_start = s.id)) INNER JOIN luoghi f ON (id_end = f.id) WHERE "{x}" = s.nome AND "{y}" = f.nome')
    cursor.execute(f'SELECT percorso FROM (inizio_fine INNER JOIN percorsi ON (inizio_fine.id_percorso = percorsi.id) INNER JOIN luoghi s ON (id_start = s.id)) INNER JOIN luoghi f ON (id_end = f.id) WHERE "{x}" = s.nome AND "{y}" = f.nome')
    path=cursor.fetchone()
    conn.close()
    return path

def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, porta))  
    print("SERVER ONLINE")
    server.listen()
    return server

#MAIN

server=server()
while(1):
    con = con_alphabot(server)
    t= Thread(server,con)

server.close()



