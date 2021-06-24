import json
import random

for i in range(10):
    print(json.dumps({"Temperature": random.randint(0,40),"Soc": random.randint(20,80)}))
