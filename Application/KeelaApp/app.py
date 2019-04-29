# Standard imports
import os
import numpy as np
import pandas as pd
# Importing backend functions
from flask import Flask, render_template, request

# Importing custom functions
from pred_fun import scaled_inputs
from pred_fun import matching_dataframe_for_input

from sklearn.externals import joblib


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')




@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')




@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':

        # Storing an empty dictionary
        data_dict = {'age':[0],'workclass':[0],'education':[0],'education_years':[0],'marital_status':[0],
             'occupation':[0],'relationship':[0],'race':[0],'sex':[0],'capital_gain':[0],'capital_loss':[0],
             'hours_worked_per_week':[0],'native_country':[0]}

        # Converting our user inputs into a dictionary format
        requests = request.form.to_dict()

        #Defining a list of continuous variables
        cont_feat = ['age',
             'education_years',
             'capital_gain',
             'capital_loss',
             'hours_worked_per_week']

        # Iterating through the user dictionary and mapping all the values over
        # This ensures consistency in the dictionary formatting
        for i in data_dict:
            if i in cont_feat:
                out = requests[i]
                out = int(out)
                data_dict[i] = [out]
            else:
                data_dict[i] = [requests[i]]

        # converting to a pandas dataframe
        input_dataframe = pd.DataFrame.from_dict(data_dict)


        #Loading in the scaler object
        scaler_object = joblib.load('KeelaApp/scaler.pkl')

        # Scaling the data
        scaled_data_input = scaled_inputs(input_dataframe, scaler_object)

        # Storing a list of the clean features headers
        clean_features = pd.read_csv('KeelaApp/clean_features.csv') # Will look for a quicker way to obtain these headers
        features_headers = list(clean_features.columns)

        # Correcting the input headers
        clean_input_df = matching_dataframe_for_input(scaled_data_input, features_headers)
        #Removing any duplicated columns
        clean_input_df = clean_input_df.loc[:,~clean_input_df.columns.duplicated()]


        #Storing the result
        loaded_model = joblib.load('KeelaApp/model.pkl')
        result = loaded_model.predict(clean_input_df)[0]

        #Returning the prediction value
        prediction = int(result)

        #rendering the template
        return render_template("result.html",prediction=prediction)
