import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8088))
sock.listen(5)
sock.settimeout(60)
# sock.setblocking(False)

while True:
    try:
        client, addr = sock.accept()
    except socket.error:
        print('no clients')
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        client.setblocking(True)
        result = client.recv(1024)
        client.close()
        print('Massage {} '.format(result.decode('utf-8')))
