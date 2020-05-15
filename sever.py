import socket

s = socket.socket()
print('Socket created')

s.bind(('localhost', 9999))

s.listen(3)
print('waiting for connections...')

while True:
    c, address = s.accept()
    name = c.recv(1024).decode()
    print(f'client connected with address: {address}, and\nname : {name}')

    c.send(bytes(f'Hey {name}, Welcome to python', 'utf-8'))

    c.close()
