import requests

request = requests.get('https://api.github.com')
print(request.json())