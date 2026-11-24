try:
    number = int(input("Enter the number: "))

    result = 100 / number
except TypeError:
    print("Enter the correct datatype")
    
except ValueError:
    print("invalid number")
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("execution completed!!!!!!!!!")