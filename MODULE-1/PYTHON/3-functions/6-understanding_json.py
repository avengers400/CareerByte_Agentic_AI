#json- javascript notation object

#json is used in aws/azure/gcp/oci/ api responses , k8s api responses, monitoring systems, config files and ai agentic tools

#dict to json
import json
server = {"server": "web-server", "cpu": 85, "memory": 70, "healthy": True, "is_used": None}
print(type(server))

json_data = json.dumps(server, indent=2)
print(json_data)
print(type(json_data))

#json to dict

data = '{"name": "webserver", "cpu": 85}'
print(type(data))

dict_data = json.loads(data)
print(type(dict_data))


