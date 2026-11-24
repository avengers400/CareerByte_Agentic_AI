try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        data = file.read()
except FileNotFoundError: 
    print("Error: sample.txt file is not present in the current folder")
except Exception as e:
    print(e)
