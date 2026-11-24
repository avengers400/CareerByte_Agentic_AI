# cpu = 70
cpu = int(input("please enter the cpu: "))
print(type(cpu))

if cpu > 85:
    print("WARNING: HIGH CPU USAGE")
else:
    print("CPU USAGE IS NORMAL")

