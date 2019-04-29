import os

# Importing basic libraries for data analytics
import numpy as np
import pandas as pd





def scaled_inputs(data, fitted_scaler):
    '''
    INPUT:
    data - Pandas Dataframe of our raw inputs
    fitted_scaler - scaler object used in our clean_data function

    OUTPUT:
    features_final - Pandas dataframe of our processed input features

    Description:
    Scaling and preprocessing our inputs in a similar fashion to how our training data
    was developed. This ensures that we maintain our internal validity.
    '''

    cont_feat = ['age',
     'education_years',
     'capital_gain',
     'capital_loss',
     'hours_worked_per_week']

    for feat in cont_feat:
        data[feat] = data[feat].astype(str).astype(int)

    # creating a list of of column names
    skewed_cols = ['capital_gain','capital_loss']

    # Log transforming the skewed features
    features_log_transformed = pd.DataFrame(data = data)
    features_log_transformed[skewed_cols] = data[skewed_cols].apply(lambda x: np.log(x + 1))

    # Copying the dataframe over to a new one
    features_log_minmax_transform = features_log_transformed.copy()
    features_log_minmax_transform[cont_feat] = fitted_scaler.transform(features_log_transformed[cont_feat])

    # One-hot encode the 'features_log_minmax_transform' data using pandas.get_dummies()
    features_final = pd.get_dummies(features_log_minmax_transform)
    features_final.columns = features_final.columns.str.replace(' ', '')

    return features_final

def matching_dataframe_for_input(clean_inputs, column_headers):
    '''
    INPUT:
    clean_inputs - pandas dataframe of our cleaned inputs
    column_headers - column headers of our features dataframe we used for training our model

    OUTPUT:
    input_df - Pandas dataframe of our processed input features with the correct column headers

    Description:
    We need this function to ensure the shape of our inputs dataframe from our app
    is the same as our training dataframe. We need this since our model depends on having the same shape inputs.
    '''

    # Empty Dataframe with features headers
    input_df = pd.DataFrame(index=[0], columns = column_headers)
    # Passing values to our empty dataframe
    for col in list(clean_inputs.columns):
        input_df[col] = clean_inputs[col][0]
    # Filling the Na's with 0
    input_df.fillna(0, inplace=True)

    return input_df
