from flask import Flask, render_template, url_for , request, redirect, jsonify
import pickle
import numpy as np

app = Flask ( __name__ )
model = pickle.load(open('model.pkl', 'rb'))

@app.route ( '/' )
def home():
    return render_template('index.html')

@app.route( '/predict',methods=['POST'])
def predict():

    temp_array =list()
    if request.method== 'POST':
        age =int(request.form['age'])
        hype = int(request.form['hypertension'])
        heart = int(request.form['heart_disease'])
        glevel = int(request.form['avg_glucose_level'])
        bmi = int(request.form['bmi'])

        gender = request.form['Gender']
        if gender =='Female':
            temp_array= temp_array+[1,0]
        else:
            temp_array = temp_array + [0 , 1]

        marr = request.form['Martial Status']
        if marr=='Not Married':
            temp_array = temp_array + [1, 0]
        else:
            temp_array = temp_array + [0 , 1]

        govt = request.form['Work Type']
        if govt == 'Govt Job':
            temp_array = temp_array + [1,0,0,0,0]
        elif govt == 'Never Worked':
            temp_array = temp_array + [0, 1, 0, 0, 0]
        elif govt == 'Private Job':
            temp_array = temp_array + [0, 0, 1, 0, 0]
        elif govt == 'Self Employed':
            temp_array = temp_array + [0, 0, 0, 1, 0]
        elif govt == 'Student/Children':
            temp_array = temp_array + [0, 0, 0, 0, 1]


        rt = request.form['Residence Type']
        if rt=='Rural':
            temp_array = temp_array + [1, 0]
        else:
            temp_array = temp_array + [0 , 1]

        smk = request.form['Smoking Status']
        if smk == 'Dont want to Disclose':
            temp_array = temp_array + [1,0,0,0]
        elif smk == 'Formerly Smoked':
            temp_array = temp_array + [0, 1, 0, 0]
        elif smk == 'Never Smoked':
            temp_array = temp_array + [0, 0, 1, 0 ]
        elif smk == 'Smokes':
            temp_array = temp_array + [0, 0, 0, 1]


        temp_array = temp_array + [age , hype , heart , glevel , bmi]

        final_features = np.array([temp_array])
        prediction = model.predict( final_features )
        output = prediction[0]

        if output == 0:
            output = 'You are less likely to get stroke'
        else:
            output = 'You are likely to get stroke'

        return render_template ( 'result.html', prediction_text='  {}'.format( output ) )

    else:
        return render_template('index.html')



@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)




if __name__ == '__main__':
    app.run (debug = True)
