import socket

serversocket = socket.socket()
host = 'localhost'
port = 3423

serversocket.connect((host, port))

def send_command(s, string):
   s.send(string.encode())
   data = s.recv(1024).decode()
   print (data)

while True:
   command = input('Command For Hal: ')
   send_command(serversocket, command)

serversocket.close()

