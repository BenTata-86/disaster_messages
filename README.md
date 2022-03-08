# Disaster Response Pipeline Project
**This repository shows how to create a web-app, to classify disaster messages.
Data is originated from Appen.**

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [How to run](#run)
5. [Model](#model)
6. [Licensing, Authors, and Acknowledgements](#licensing)

### Installation <a name="installation"></a>
- Python 3.8+
- ML Libraries: NumPy, Pandas, Sciki-Learn
- NLP Libraries: NLTK
- SQLlite Database Libraqries: SQLalchemy
- Model Loading and Saving Library: Pickle
- Web App and Data Visualization: Flask, Plotly
- Additional: Bootstrap for styling, HTML for templates


### Project Motivation<a name="motivation"></a>
This projects aims to demonstrate almost(except monitoring) all steps in Data Science project.

1. ETL

    - Extract data : Input data from Appen
    - Transform data : clean  and transfor data
    - Load data : Load data to a SQL database
2. Modelling
    - Initializing the data
    - Vectorization and transfromation of the texts
    - Build model
    - Train model
    - Display the results and metrics
    - Save model
3. Deployment 
    -Create a web-app with Flask and Plotly

It is also demonstrating NLP modeling with NLTK and scikit-learn.


### File Descriptions <a name="files"></a>

There are 3 folders each one is related with the above steps;
    -app:
        this folder contains run.py file which is running the web-app
        -templates: there are two templates
    -data:
        this folder contains the ETL part files.
        - Input files: messages.csv and categories.csv
        - Clean and transform: process_data.py
        -Load data : Load data into a database disaster_response.db
     -model:
        this folder contains modelling part of the files
        -modelling files: 

### How to run <a name="run"></a>

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Click the `PREVIEW` button to open the homepage

### Model <a name="model"></a>




### Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to Inside Airbnb for the data.  You can find the Licensing for the data and other descriptive information at the inside airbnb site available [here](http://insideairbnb.com/get-the-data.html).  Otherwise, feel free to use the code here as you would like! 

