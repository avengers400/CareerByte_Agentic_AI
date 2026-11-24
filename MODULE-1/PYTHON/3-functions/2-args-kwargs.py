#args
def monitor_servers(*servers): #tuple
#    print(servers)
#    print(type(servers))
    for server in servers:
      print(server)


monitor_servers("web", "prod", "test") # this should go to func as ["web", "prod", "test"]

#kwargs

def server_details(**servers): # {name: webserver, region: us-east-1, cpu: 80}
   for i, v in servers.items(): # [("name", "webserver"), (), ()]  #("name", "webserver")
      print(f"{i}: {v}")
          

server_details(name="webserver", region="us-east-1", cpu=80)
