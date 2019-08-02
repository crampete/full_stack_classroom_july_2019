# getting the content of http://www.example.com


import requests

resp = requests.get('http://www.example.com')

print(resp.text)
