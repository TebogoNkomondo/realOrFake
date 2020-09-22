import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

nltk.download('stopwords')
nltk.download('punkt')
stopword = nltk.corpus.stopwords.words('english')

porter =  PorterStemmer()

#punctutation removal
def clean_text(text):
    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text
#end clean_text

# Tockenization
def tokenization(text):
    text = re.split('\W+', text)
    return text
#end tokenization

# stopword removal
def remove_stopwords(text):
    text = [word for word in text if word not in stopword]
    return text

# return to string
def listToString(s):     
    # initialize an empty string 
    str1 = " " 
    # return string   
    return (str1.join(s))
#end listToString

def sentenceStemmer(text):
    words = word_tokenize(text)
    corpus = []
    for word in words:
        corpus.append(porter.stem(word))
        corpus.append(" ")
    #end for
    return "".join(corpus)
#end sentenceStemmer

def convert_text_to_index_array(text):
    words = kpt.text_to_word_sequence(text)
    # words = pad_sequences(words, padding='post', maxlen=23)
    # print(text)
    wordIndices = []
    for word in words:
        if word in dictionary:
            wordIndices.append(dictionary[word])
    return wordIndices
#end convert_text_to_index_array
