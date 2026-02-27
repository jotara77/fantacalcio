import json
from calciatore import Calciatore

f = open("dataset/fantacalcio.json","r")
data = json.load(f)
f.close()

print(data)