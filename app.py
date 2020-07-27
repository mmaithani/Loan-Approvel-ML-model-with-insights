import pandas as pd
from flask import Flask, jsonify, request
import pickle
#new addition
from flask import render_template
import numpy as np

model = pickle.load(open('modell.pkl','rb'))
app = Flask(__name__)

# routes
@app.route('/api', methods=['POST'])
def predict():
    # get data
    data = request.get_json(force=True)
    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)
    # predictions
    result = model.predict(data_df)
    # send back to browser
    output = {'results': int(result[0])}
    # return data
    return jsonify(results=output)

@app.route('/')
def home():
    return render_template('loan_application_form.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction(): 
    if request.form:
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(int, to_predict_list)) 
        print(to_predict_list)
        result = ValuePredictor(to_predict_list)    
        print(result)     
        if int(result) == 0: 
            prediction = 'No, You are not elligible for loan :( '
        else: 
            prediction = 'Hurray ! You Are elligible for loan :)'            
        return render_template("loan_application_form.html", prediction = prediction)

# prediction function 
def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 8) 
    loaded_model = pickle.load(open("modell.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    return result[0] 

if __name__ == '__main__':
    print("-"*85)
    app.run(port = 5000, debug=True)