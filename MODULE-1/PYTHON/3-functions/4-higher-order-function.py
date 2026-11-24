def check_cpu(cpu):
    return cpu > 80

def monitor(value, check_func):
    return check_func(value)

print(monitor(90, check_cpu))




#check_func------->check_cpu(90)-----------> cgeck
