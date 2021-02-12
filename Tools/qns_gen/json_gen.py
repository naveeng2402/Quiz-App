import json, _jsonnet

with open('Tools/qns_gen/test.jsonnet') as f:
    data  = f.read()
    
data = _jsonnet.evaluate_snippet("snippet",data)
# print(data)

with open('Tools/qns_gen/_qns.json', 'w') as f : f.write(data)