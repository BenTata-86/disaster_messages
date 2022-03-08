# Disaster Response Pipeline Project
**This repository shows how to create a web-app, to classify disaster messages.
Data is originated from Appen.**

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [How to run](#results)
5. [Model](#model)
6. [Licensing, Authors, and Acknowledgements](#licensing)

### Installation <a name="installation"></a>
There is no need to run additional packages or libraries to install under the Anaconda Python distribution.


### Project Motivation<a name="motivation"></a>



### File Descriptions <a name="files"></a>

### How to run

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Click the `PREVIEW` button to open the homepage

### Model




### Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to Inside Airbnb for the data.  You can find the Licensing for the data and other descriptive information at the inside airbnb site available [here](http://insideairbnb.com/get-the-data.html).  Otherwise, feel free to use the code here as you would like! 

