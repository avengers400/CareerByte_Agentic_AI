import json
#load--------->converting json to python dictionary
with open("C:/Users/HP/Downloads/Agentic-Ai/MODULE-1/PYTHON/file-reading-writing/server.json", "r", encoding="utf-8") as file:
    data = json.load(file)
print(data['LogicalID'])

with open("C:/Users/HP/Downloads/Agentic-Ai/MODULE-1/PYTHON/file-reading-writing/sample.txt", "r", encoding="utf-8") as f:
    data_txt = f.read()
print("")
print(data_txt)
