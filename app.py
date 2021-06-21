import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    temp_array = list ()
    if request.method == "POST":
        soil_type = request.form['Soil-Type']
        if soil_type == 'Soil Type_Black':
            temp_array = temp_array + [1, 0, 0, 0, 0]
        elif soil_type == 'Soil Type_Clayey':
            temp_array = temp_array + [0, 1, 0, 0, 0]
        elif soil_type == 'Soil Type_Loamy':
            temp_array = temp_array + [0, 0, 1, 0, 0]
        elif soil_type == 'Soil Type_Red':
            temp_array = temp_array + [0, 0, 0, 1, 0]
        elif soil_type == 'Soil Type_Sandy':
            temp_array = temp_array + [0, 0, 0, 0, 1]

        crop_type = request.form['Crop-Type']
        if crop_type == 'Crop Type_Barley':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif crop_type == 'Crop Type_Cotton':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif crop_type == 'Crop Type_Ground Nuts':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        elif crop_type == 'Crop Type_Maize':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        elif crop_type == 'Crop Type_Millets':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        elif crop_type == 'Crop Type_Oil seeds':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        elif crop_type == 'Crop Type_Paddy':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        elif crop_type == 'Crop Type_Pulses':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        elif crop_type == 'Crop Type_Sugarcane':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        elif crop_type == 'Crop Type_Tobacco':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        elif crop_type == 'Crop Type_Wheat':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

        temp = int(request.form['Temparature'])
        humid = int(request.form['Humidity'])
        mois = int(request.form['Moisture'])
        nit = int(request.form['Nitrogen'])

        pho = int(request.form['Phosphorous'])

        temp_array = temp_array + [temp , humid , mois , nit , pho]




      #  int_features = [int ( x ) for x in request.form.values ()]
        final_features = np.array([temp_array])
        prediction = model.predict( final_features )
        output = prediction

        return render_template ( 'result.html', prediction_text=' Recommended Fertilizer is {}'.format ( output ) )

    else:
        return render_template('index.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)