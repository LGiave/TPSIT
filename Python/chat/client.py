import socket

ip = '127.0.0.1'
port = 5000


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while(True):
        msg = input(">>")

        client.sendto(msg.encode(),(ip,port))
        data=client.recv(4096)
        print(str(data))

        if str(msg) == ".shutdown":
            break

    client.close()

if __name__ == "__main__":
    main()