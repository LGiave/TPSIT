import subprocess
#p =  subprocess.Popen(['ping', '-c 2', '192.168.10.255'], stdout=subprocess.PIPE)
#ping = p.communicate()
#print(ping[0].decode())

ipAddress = input("inserire indirizzo")
mask=input("inserire maschera")

ipAddress_splitted = [int(i) for i in ipAddress.split(".")]

ipAddress_bin = 0 
for e, group in enumerate(ipAddress_splitted):
    ipAddress_bin = ipAddress_bin + group*(2**(((3-e)*8)))

ipAddress_host = ipAddress_bin
for c in range(1,2**(32-int(mask))-1):
    ipAddress_host = ipAddress_host + 1
    l = '.'.join([str(int(bin(ipAddress_host)[i:i+8],2)) for i in range(2,34,8)])
    print(l)
    p =  subprocess.Popen(['ping', '-c 2', l], stdout=subprocess.PIPE)
    ping = p.communicate()
    print(ping[0].decode())
    #print(f' numero di occorrenze {ping[0].decode().count("Tempo approssimativo")}')
    if(ping[0].decode().count("time")>0):
        print(f"L'host {l} è attivo")
    else:
        print(f"L'host {l} è inattivo")