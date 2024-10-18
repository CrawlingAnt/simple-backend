import json

json_str = '{"name": "John", "age": 30, "city": "New York"}'
data = json.dumps(json_str)
data1 = json.loads(data)
print(data,data1)
