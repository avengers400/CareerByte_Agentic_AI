cpu_usage = 80
cpu_limit = 75

# print(cpu_usage > cpu_limit) #True
# print(cpu_usage == cpu_limit) #False
# print(cpu_usage != cpu_limit) #True

#whatever the new cpu usage is there i have to add 10 to it

new_cpu_usage = "60"
result = int(new_cpu_usage)  + 10
# print(result) #

server = "web-server-01"
status = "Running"
cpu = 65

#add the cpu by 10 and write sentence-"Server <server name> is runnung with cpu ()%""

new_result = f"Server {server} is running with {cpu+10}%"
print(new_result)

name = "RISHAV"

print(name.lower())

message = "ERROR: Database connection failed"
print(message.upper())

print("ERROR" in message)