# Chennai weather
import requests
url = 'https://openweathermap.org/find?q=chennai'

resp = requests.get(url)

# will not be readable as CSS and JS are not coming into picture
#  but you'll get some HTML

fp = open('result.html', 'w')
fp.write(resp.text)

fp.close()
