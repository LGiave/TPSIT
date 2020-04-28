'''
#TCP
import socket as sck 
s=sck.socket(sck.AF_INET,sck.SOCK_STREAM)
server_ip='192.168.1.253'
data=b'ciao'
s.connect(('192.168.1.253',10000))
risp=s.recv(4096)
print(risp)
s.close()
'''
#UDP
import socket as sck
s=sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
server_ip='5.102.12.239'
data=b'agbuntu mangia le banane e se le ficca nel culo cosi sono piu gustose'
s.sendto(data,(server_ip,5200))
risp=s.recv(4096)
print(risp.decode("ascii"))
s.close()