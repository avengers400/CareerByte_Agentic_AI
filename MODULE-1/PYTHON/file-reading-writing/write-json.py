import json
server = {
    "LogicalID": {
      "Type": "AWS::AccountAccess::Application",
      "Properties": {
        "IdentitySource": {
          "IdentityCenter": {
            "ApplicationArn": "String",
            "InstanceArn": "String"
          }
        },
        "Tags": [
          {
            "Key": "String",
            "Value": "String"
          }
        ]
      }
    }
}


with open("C:/Users/HP/Downloads/Agentic-Ai/MODULE-1/PYTHON/file-reading-writing/server1.json", "w", encoding="utf-8") as f:
    json.dump(server,f, indent=4)