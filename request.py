import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'N':60, 'P':50, 'K':40,'temperature':20, 'humidity':80,'ph':7,'rainfall':200})

print(r.json())