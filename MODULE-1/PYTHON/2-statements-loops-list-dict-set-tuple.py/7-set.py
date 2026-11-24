#set-unordered, mutable, collection of unique events-no duplicates

servers = {"web", "db", "prod"}
from datetime import datetime
import requests
import os


print(datetime.now())
for s in servers:
    print(s)

print(servers)
servers.add("dev")
print(servers)
servers.update(["ec2", "aix"])
print(servers)
servers.remove("ec2")
print(servers)
servers.discard("db")
print(servers)

a = [1, 2 , 2, 4, 5, 6, 2]
b = set(a)
desc_order = sorted(b, reverse=True)
print(desc_order)