import sys
import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger', 'stopwords'])

import re
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.externals import joblib

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer


def load_data(database_filepath):
    """ Load data from database
    Loads data from database_filepath.
    Create arrays for messages, labels. List for target names of labels.
    
    Arg:
        database_filepath: database filepath name
    Returns:
        X : Messages Array
        Y : Labels(output) Array
        category_names : Categories column names
    """
    engine = create_engine('sqlite:///'+database_filepath)
    df = pd.read_sql_table('disaster_messages',engine)
    X = df.message.values
    Y = df.drop(columns=['id','message','original','genre']).values
    category_names = df.drop(columns=['id','message','original','genre']).columns
    
    return X, Y, category_names
    


def tokenize(text):
    """Initiliaze messages for transformatipn
    1. Tokenize messages
    2. Lemmatize messages
    3. Normalize and strip messages
    4. Remove stopwords
    
    args:
        text : input text
     returns:
        clean_tokens : cleaned text 
    
    """
    # Initialization
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    stopWords = set(stopwords.words('english'))
    
    # Get clean tokens after lemmatization, normalization, stripping and stop words removal
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        if tok not in stopWords:
            clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    """ 
        A pipeline for vectorization, tfidf tranformation and randomforest classification.
        Args: none
        
        returns:
            cv: GridSearchCV
    """
    pipeline = Pipeline([('vect', CountVectorizer(tokenizer=tokenize)),
                ('tfidf', TfidfTransformer()),
                   ('clf', MultiOutputClassifier(RandomForestClassifier(n_jobs=-1)))])

    # specify parameters for grid search
    parameters = {
        'vect__ngram_range': ((1, 1),(1,2))
    }
 
    # create grid search object
    cv = GridSearchCV(pipeline, param_grid=parameters, n_jobs=-1, cv=3)
    
    return cv
    


def evaluate_model(model, X_test, Y_test, category_names):
    """Evaluate model over test data
    
        Args: 
            model: built model
            X_test: test data for messages
            Y_test: test data for labels
            category_names: category names of labels
        Returns none
        
        """
    
    # Use model to predict
    Y_pred = model.predict(X_test)
    # Print Results
    print(classification_report(Y_test, Y_pred, target_names=category_names))


def save_model(model, model_filepath):
    """ Save model to filepath
    
        args: 
            model : model name
            model_filepath : pathname to save model
    """
    joblib.dump(model, model_filepath)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()