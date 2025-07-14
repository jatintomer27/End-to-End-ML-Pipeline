# It is my web application 

from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from ML_pipeline.pipeline.state_06_predection import PredectionPipeline 

# We have directly imported from the ML_pipeline 
# because we have aleady installed ML_pipeline as my local package in the setup.py file. (SRC_REPO)

# Initializing a flask app

app = Flask(__name__) 


# Render the home page

@app.route('/',methods=['GET'])
def homePage():
    return render_template("index.html") # By default search in templates folder

@app.route('/train',methods=['GET'])
def train():
    os.system("python main.py")
    return "Training Successfull!"

@app.route('/predict',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,
                    free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1,11)
            print(data)
            obj = PredectionPipeline()
            predict = obj.predict(data)

            return render_template('results.html',prediction=str(predict))
        except Exception as e:
            print(f"The exception message is: {e}")
            return 'Something went wrong'
    else:
        return render_template('index.html')

# Run the app

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
