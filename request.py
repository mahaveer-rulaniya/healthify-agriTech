import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Temparature':60, 'Humidity':50, 'Moisture':40,'Nitrogen':20, 'Potassium':80,'Phosphorous':70,'Soil-Type':'Soil Type_Loamy','Crop-Type':'Crop Type_Sugarcane'})

print(r.json())