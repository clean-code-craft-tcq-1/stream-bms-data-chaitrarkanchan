import json
import random

for i in range(10):
    print(json.dumps({"Temperature": random.randint(10,100),"SOC": random.randint(10,100)}))
