import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('127.0.0.1', 8088))
sock.send(str(input()).encode())
print('Server response: {}'.format(sock.recv(1024).decode()))
sock.close()
