import socket
import turtle


#TURTLE_KING=turtle.Turtle()
#TURTLE_KING.hideturtle()
MOVE=10

server_ip="127.0.0.1"
server_port=10000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((server_ip,server_port))

function={"w":forward,"s":backward,"a":left,"d":right}

port_table=[]
turtle_dict={}

def turtle_create(address,movement):
    turtle_dict[address[1]]=turtle.Turtle()
    #turtle_dict[address[1]]=TURTLE_KING.clone()
    #turtle_dict[address[1]].showturtle()
    function[movement]

def forward():
     turtle_dict[address[1]].forward(MOVE)

def backward():
    turtle_dict[address[1]].backward(MOVE)

def left():
    turtle_dict[address[1]].left(MOVE)

def right():
    turtle_dict[address[1]].right(MOVE) 

def move(address,movement):
    if movement=="w":
           
    elif movement=="s":
            
    elif movement=="a":
            
    elif movement=="d":
             

while True:
    command,address = s.recvfrom(4096)
    movement=command.decode()
    if address[1] in port_table:
        print(address[1])
        function[movement]
    else:
        port_table.append(address[1])
        turtle_create(address,movement)
        print(address[1])





