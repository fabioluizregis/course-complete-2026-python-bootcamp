import math
import os

import my_module
import requests

print(math.sqrt(16))

my_module.hello()

r = requests.get('https://www.google.com')
print(r.text)
