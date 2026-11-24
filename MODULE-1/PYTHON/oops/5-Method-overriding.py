class Server:
    def restart(self):
        print("This is current server")

class Server1(Server):
    def restart(self):
        print("This is latesst server")

server = Server()
server1 = Server1()
server.restart()
server1.restart()