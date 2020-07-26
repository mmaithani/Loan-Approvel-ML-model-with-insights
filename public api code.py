# public api code

import pickle

# url= 'http://127.0.0.1:5000/api'
url= 'https://loan5.herokuapp.com/api'

import json
import requests
# sample data
data={'Gender':1, 'Married':1, 'Dependents':2, 'Education':0, 'Self_Employed':1,'Credit_History':0,'Property_Area':1, 'Income':1}
data = json.dumps(data)

# test working
requests.post(url, data)

send_req = requests.post(url, data)
print(send_req)

print(send_req.json())