class Server:

    @staticmethod
    def validate_cpu(cpu):
        
        return 0 <= cpu <= 100

print(Server.validate_cpu(80))