import socketserver


class SecondExample(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class MainExample(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        print('Address: {}'.format(self.client_address[0]))
        print('data: {}'.format(data.decode()))
        self.request.sendall('Massage was transport to server'.encode())


if __name__ == '__main__':
    with SecondExample(('', 8088), MainExample) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            server.server_close()
