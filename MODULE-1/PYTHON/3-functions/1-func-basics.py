print("Checking web server")
print("Checking app server")
print("Checking db server")

def greet():
    print("Hello")

greet()

greet()

def check_server(server_name):
    print(f"Checking health of {server_name}")

check_server("web-server")
check_server("db-server")



def server_details(name: str, cpu: float, memory: float):
    print("=======Server data summary=========")
    print(f"Server: {name}")
    print(f"Server: {cpu}%")
    print(f"Server: {memory}%")

server_details("db-server", 80, 80)

#return 
def add(a, b):
    return (a + b)

result = add(100,50)
print(result)

def check_cpu(cpu):
    if cpu >= 90:
        return "CRITICAL"
    elif cpu >= 75:
        return "WARNING"
    else:
        return "HEALTHY"
    
status = check_cpu(95)
print(status)
