import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Temparature':30, 'Humidity':60, 'Moisture':40,'Nitrogen':20, 'Phosphorous':70,'Soil-Type':'Soil Type_Clayey','Crop-Type':'Crop Type_Pulses'})

print(r.json())