import json

import requests
import yaml

r = requests.get('http://127.0.0.1:8000/api/category/', headers={"Accept": "application/json"})

content = r.content.decode("utf-8")

# data = yaml.safe_load(content)

data = json.loads(content)
print(data)
