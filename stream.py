from flask import Flask, request, jsonify
import os
import xgboost as xgb
import joblib
import numpy as np
import json

app = Flask(__name__)

def check(sepal_length, sepal_width, pedal_length, pedal_width):
    checking_list = [sepal_length, sepal_width, pedal_length, pedal_width]
    for checking in checking_list:
        if checking is None:
            return False
        if not (type(checking) == int or type(checking) == float) : 
            return False
        if checking < 0 or checking > 10:
            return False
    return True


def predicting(sepal_length, sepal_width, pedal_length, pedal_width):
    bst = joblib.load("/home/neuwirth/work/xgboost_iris")
    prediction_input_array = np.array([[sepal_length, sepal_width, pedal_length, pedal_width]])
    prediction_input_dmatrix = xgb.DMatrix(prediction_input_array)
    prediction = bst.predict(prediction_input_dmatrix)
    return prediction 

ROOT_PATH = os.environ.get('ROOT_PATH')
@app.route('/prediction', methods=['GET', 'POST','DELETE', 'PATCH'])
   
def prediction():
    if  request.method == 'POST':
        data_bytes=request.data
        data_dict = json.loads(data_bytes.decode('utf-8'))        
        sepal_width = data_dict.get("sepal_width")
        sepal_length = data_dict.get("sepal_length")
        pedal_length = data_dict.get("pedal_length")
        pedal_width = data_dict.get("pedal_width")

        if not check(sepal_length, sepal_width, pedal_length, pedal_width):
            return jsonify(isError= False,
                    message= "Values of sepal or pedal are wrong",
                    statusCode= 406), 406

        prediction = predicting(sepal_length, sepal_width, pedal_length, pedal_width)
        prediction_list = prediction.tolist()

        return jsonify(isError= False, data = prediction_list, statusCode= 200), 200
        


    else: return jsonify(isError= True,
                    message= "Request operation must be a POST",
                    statusCode= 405), 405


if __name__ == '__main__':
    app.run(debug= True)