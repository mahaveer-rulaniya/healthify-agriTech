import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == "POST":
        int_features = [int ( x ) for x in request.form.values ()]
        final_features = [np.array ( int_features )]
        prediction = model.predict ( final_features )
        output = prediction

        return render_template ( 'result.html', prediction_text=' The Recommended Crop to grow is {}'.format ( output ) )

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
