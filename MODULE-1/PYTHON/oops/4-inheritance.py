class Server:
    def __init__(self , name, cpu):
        self.name = name
        self.cpu = cpu


    def check_health(self):
        return "HIGH" if self.cpu > 80 else "NORMAL"

class EC2Server(Server):
    def __init__(self ,name, cpu, instance_id):
        
        super().__init__(name, cpu)
        self.instance_id = instance_id
        print(self.name)

    def display(self):
        print(f"instance_id: {self.instance_id}")
        print(f"Name: {self.name}")
        print(f"CPU: {self.cpu}")
        print(f"Health status: {self.check_health()}")

ec2 = EC2Server("dbserver", 90, "i-1234")
ec2.display()
