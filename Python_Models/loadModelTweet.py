import json
import numpy as np
import keras
import keras.preprocessing.text as kpt
from keras.preprocessing.text import Tokenizer
from keras.models import model_from_json

# we're still going to use a Tokenizer here, but we don't need to fit it
tokenizer = Tokenizer(num_words=3000)
# for human-friendly printing
labels = ['fake', 'real']

# read in our saved dictionary
with open('dictionary.json', 'r') as dictionary_file:
    dictionary = json.load(dictionary_file)

# this utility makes sure that all the words in your input
# are registered in the dictionary
# before trying to turn them into a matrix.
def convert_text_to_index_array(text):
    words = kpt.text_to_word_sequence(text)
    wordIndices = []
    for word in words:
        if word in dictionary:
            wordIndices.append(dictionary[word])
        # else:
        #     print("'%s' not in training corpus; ignoring." %(word))
    return wordIndices

# read in your saved model structure
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
# and create a model from that
model = model_from_json(loaded_model_json)
# and weight your nodes with your saved values
model.load_weights('model.h5')


# while 1:
    # evalSentence = input('Input a sentence to be evaluated, or Enter to quit: ')
evalT = np.genfromtxt('./testf.csv', delimiter=',', skip_header=1, usecols=(0, 3), dtype=None)
    # evalSentence = input("do the thing")
eval_x = [str(x[1]) for x in evalT]
eval_y = [str(x[0]) for x in evalT]
# if len(evalT) == 0:
#     break
f = open("output.txt","w")
for index_of_interest, text1 in enumerate(eval_x):
    # format your input for the neural net
    testArr = convert_text_to_index_array(text1)
    input = tokenizer.sequences_to_matrix([testArr], mode='binary')
    # predict which bucket your input belongs in

    # format your input for the neural net
    testArr = convert_text_to_index_array(text1)
    input = tokenizer.sequences_to_matrix([testArr], mode='binary')
        # predict which bucket your input belongs in
    pred = model.predict(input)
        # and print it for the humons
    print("line: %s the %s sentiment; %f%% confidence" % (eval_y[index_of_interest] ,labels[np.argmax(pred)], pred[0][np.argmax(pred)] * 100))
    f.write("line: %s; - %s tweet; %f%% confidence \n" % (eval_y[index_of_interest] ,labels[np.argmax(pred)], pred[0][np.argmax(pred)] * 100))