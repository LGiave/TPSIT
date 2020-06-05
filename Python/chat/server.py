import socket
import time

ip = '127.0.0.1'
port = 5000
client=[]

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server.bind((ip,port))

    while(True):
        raw_data,address = server.recvfrom(4096)
        client.append(address)
        file1 = open("esempio1.txt","a")
        file1.write(str(raw_data) + str(time.strftime("%H:%M:%S")) + str(address) + "\n")
        file1.close() 

        if str(raw_data,encoding="ascii") == ".shutdown":
            break
            
        i=0
        
        while(i<len(client)):
            if address!=client[i]:
                server.sendto(raw_data,client[i])
                i+1
            else:
                i+1

        print('>> ' + str(raw_data) + str(time.strftime("%H:%M:%S")))

    server.close()

if __name__ == "__main__":
    main()