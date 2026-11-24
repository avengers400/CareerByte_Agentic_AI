class Server:
    def __init__(self , name, cpu):
        self.name = name
        self.cpu = cpu
        print("init called")
        



    def display(self):
        print(f"Sever: {self.name}")
        print(f"CPU: {self.cpu}")


server1 = Server("web-server", 45)
# server1.display()
