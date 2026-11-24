a = [2, 3, 4, 5]

b = []
for no in a:
    square_no = no**2
    b.append(square_no)
print(b)

# def square(x):
#     print(x**2)
# square(2)

square = lambda x: x**2
print(square(2))

#sort servers by cpu

servers = [{"name": "web", "cpu": 60},
           {"name": "test", "cpu": 70},
           {"name": "prod", "cpu": 80}]
#all server names whose cpu > 60

for s in servers:  #{"name": "web", "cpu": 60},{"name": "test", "cpu": 70},{"name": "prod", "cpu": 80}
    if s['cpu'] > 60:
        print(f"server-name: {s['name']}")
#sort servers by cpu in descending order

result = sorted(servers, key=lambda b: b["cpu"], reverse=True) #gives result as list
print(result)

