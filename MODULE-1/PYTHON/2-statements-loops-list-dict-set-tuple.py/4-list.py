#A list stores multiple values in single variable.lists are ordered, mutable and allow duplicate values.

fruits = ["mango", "guava", 2, "apple", True]

print(fruits[-1])
print(len(fruits))

fruits.append("banana")
#print(fruits)
fruits.remove("banana")
print(fruits)
fruits.pop(1)
print(fruits)

#List slicing

servers = ["web", "app", "db", "cache"]
print(servers[0:3]) # 0,1,2


#LOOP

for server in servers:
 if server == "app":
    print(server)

#print all numbers from 1 to 10

# for number in range(1, 11):
#     print(number)


nos = [1, 2, 3, 4, 5, 6, 7,  9, 10, 11, 12, 8,  13, 14, 15, 16]
for num in nos:
   if num == 8:
      continue
   print(num)

#dictionary

student = {"name": "", 
           "class": "10th", 
           "city": "kolkata", 
           "hobby": "watching tv series"}
print(student["name"])
print(student.get('name', 'Ajay'))

servers = [{"name": "web" , "cpu": 80},
           {"name": "prod", "cpu": 90}, 
           {"name": "db-server", "cpu": 50}]


people = {"name": "Ram", "place": "ayodhya", "skills": "archery"}
print(people.items())
print(type(people.keys()))
print(people.values())