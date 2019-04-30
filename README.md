# Donor Prediction App

![](assets/notebook_workflow.gif)
-*Notebook Workflow*

![](assets/Donor.gif)
-*Application GUI*


This application was designed with motivation from [Keela] (https://www.keela.co/. The appplication itself can be found [here](https://income-classifier.herokuapp.com/).

This repo contains some sample code to deploy a simple (but complete) Flask application to [Heroku](https://heroku.com). The deployed app counts with the following features:

* Running Python 3.6 🐍
* Static Files management with [WhiteNoise](http://whitenoise.evans.io/en/stable/) 🔌

## Table of Contents
1. [Installation and Instructions](#Installation)
2. [Project Motivation](#Motivation)
3. [File Descriptions](#Descriptions)
4. [Results](#Results)
5. [Acknowledgements](#Acknowledgements)

# Installation and Instructions <a name="Installation"></a>:
There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python which can be found [here](https://www.anaconda.com/). The code should run with no issues using Python versions 3. You may need to install [Flask](http://flask.pocoo.org/).

### Summary of steps to deploy your app
_(Assuming you've already created an account with Heroku)_

##### 1. Clone the repo
```bash
$ git clone https://github.com/Surohitt/Donor-Prediction-App.git
```

##### 2. Login to Heroku
```bash
$ heroku login
```

##### 3. Create your Heroku apps
```bash
$ heroku create
```

##### 4. Set the Python Path
```bash
$ heroku config:set PYTHONPATH=KeelaApp
```

##### 5. Deploy & Profit
```bash
$ git push heroku master
```

## Running the app locally


```bash
# Create the virtualenv
$ mkvirtualenv flask-heroku-env
# Install dependencies
$ pip install -r requirements.txt
# Run the app
$ python KeelaApp/main.py
# Now point your browser to localhost:5000
```

# Project Motivation <a name='Motivation'></a>

This project was offered by [Keela](https://www.keela.co/) as .

This project attempts to classify individuals income bracket (<50,000 and >50,000 USD) to a high degree of accuracy. With the hope of helping non profits and charities save time identifying donors. A project like this has the potential to seriously impact the status quo of donor identification.

Also, I want to encourage pull requests and further analysis on top of this project! I would love to see what the open source community could contribute to a project like this.

# File Descriptions <a name="Descriptions"></a>

#### Prepfiles
The PrepFiles folder consists of two main notebooks.

- **KeelaDonorProject.ipynb**: is a walkthrough of the EDA, data cleaning and model preparation/creation process. I highly recommend reviewing this portion as a data scientist/machine learning engineer.
- **Helper Functions.ipynb**: is a notebook consisting of several functions that were later implemented in the live application. This notebook was used to test function in an agile fashion.
- It is also important to note the **helper_files.txt**. This file includes a list of resources that were used during the development of this application.

#### Application
The other folders are reasonably self explanatory. The **procfile, requirements**, and **runtime** files simply indicate to heroku how to execute the application.

The **KeelaApp** folder contains the meat of this project. However, for simplicity, the only file worth real consideration is the **app.py**. This python file contains all the routing for our application.


# Results <a name='Results'></a>

With a final accuracy of 86% and F-score of ~52% its clear that the model seems to overfit. I believe this can be attributed to the fact that the majority of the data consists of individuals who receive an income of less than 50,000 and therefore the model naively assumes this to be true in practice.

Expanding the original dataset past the original ~ 45,000 rows with a more evenly distributed predictor variable will do wonders for our model development. This is further compounded with the Cross Validator which may be training some of the models on extremely sparse sets of positive predictor outcomes.


# Acknowledgements <a name='Acknowledgements'></a>

Thanks must go to [UCI](https://archive.ics.uci.edu/ml/datasets/Adult) for creating this data set using census data from 1996.
