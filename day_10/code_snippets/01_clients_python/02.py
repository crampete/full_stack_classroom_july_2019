# downloading an image using Python

import requests

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Cooum_River.jpg/250px-Cooum_River.jpg'

resp = requests.get(url, allow_redirects=True)

fp = open('cooum.jpg', 'wb')

fp.write(resp.content)

fp.close()
