def check_cpu(cpu) -> float:
    if int(cpu):
            """
            return the severity level for cpu usage
            """
            return "HIGH" if cpu > 80 else "NORMAL"
    else:
          return "The value of cpu is nit an integer"

check_cpu(90)

