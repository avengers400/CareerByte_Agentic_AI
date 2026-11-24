class Server:

    def __init__(self, name, cpu):
        self.name = name
        self.cpu = cpu
        print(self.cpu)

    def update_cpu(self, new_cpu):
        self.cpu = new_cpu
        print(self.cpu)

server = Server("webserver", 90)
server.update_cpu(90)