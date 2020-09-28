import json
import numpy as np
import keras
import keras.preprocessing.text as kpt
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.models import model_from_json

import DataCleaning
import warnings
warnings.filterwarnings("ignore")

tokenizer = Tokenizer(num_words=100000)
# for human-friendly printing
labels = ['fake', 'real']

# read in our saved dictionary
with open('../Dictionary_Models/locdictionary.json', 'r') as dictionary_file:
    dictionary = json.load(dictionary_file)
#end with

# read saved model
json_file = open('../NN_Models/embed_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

# load weights
model.load_weights('../NN_Models/embed_Model.h5')

# function to convert text to index
def convert_text_to_index_array(text):
    words = kpt.text_to_word_sequence(text)
    wordIndices = []
    for word in words:
        if word in dictionary:
            wordIndices.append(dictionary[word])
    return wordIndices
#end convert_text_to_index_array

# function to round off numbers
def rounding(results):
    '''Results needs to be rounded to 0 or 1 for fake or real, respectively'''
    if results < 0.5:
        return 0
    else:
        return 1
#end rounding

while 1:
    #input a text string
    text = input("Enter a text to be evaluated: ")
    
    # check if it is valid string
    if len(text) == 0 or text == 'quit':
        break
        
    tweet = text
    
    # Clean the text
    text = DataCleaning.clean_text(text)
    text = DataCleaning.remove_emoji(text)
    text = DataCleaning.tokenization(text)
    text = DataCleaning.remove_stopwords(text)
    text = DataCleaning.listToString(text)
    text = DataCleaning.sentenceStemmer(text)
    
    # evaluating the text
    text = convert_text_to_index_array(text)

    padded_text = pad_sequences([text], padding='post', maxlen=100)
    
    pred = model.predict(padded_text)

   predictions_final = [rounding(x) for x in pred]
    print(f"Sentiment: {labels[np.argmax(pred)]};  Confident: {pred[0][np.argmax(pred)]*100}")
    
#end while    
