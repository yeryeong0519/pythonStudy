import json
with open("product.json") as f:
        data = json.load(f)
print(data)