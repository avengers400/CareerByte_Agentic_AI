#Build a simple program that accepts server info from user and reports whether cpu usage is above threshold

server_name = input("Enter server name: ")
cpu = float(input("Enter cpu: "))
memory = float(input("Enter memory usage: "))

cpu_limit = 80
memory_limit = 85

print("\n------Server Report---------")
print(f"Server: {server_name}")
print(f"CPU Usage: {cpu}%")
print(f"Memory usage: {memory}%")

print(f"CPU threshold exceeded: {cpu > cpu_limit}")
print(f"Memory threshold exceeded: {memory > memory_limit}")


