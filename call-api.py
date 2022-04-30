# call api

import requests


url = "https://mockbin.org/request"


r = requests.get(url)

print(r.text)


