# Real Or Fake: Detecting whether Tweets are reporting on disaster or not.

- Different feature extraction technqiues were investigated.
- The feature extraction techniques were combined with different Neural Network Architectures.

### Feature Extration Techniques

- One Hot Encodings
- Word Embeddings:
  - Keras Embedding Layer
  - Pre-Trained Embeddings:
    - Word2Vec
    - Glove

### Neural Network Architechtures

- Multi-Layer Perceptron(MLP)
- Recurrent Neural Networks(RNN)
- Long Short-Term Memory(LSTM) Networks

### Files

- A base model which uses One-Hot Encodings and MLP is found on the BaseModel.ipynb file.
- Models using the Keras Embedding Layer are found on the Keras_Embedding_Layer.ipynb files.
- Models using Pre-Trained Embeddings are found on the Word2VecModels.ipynb and GloveModels.ipynb files

### Live Prediction

- The python Tweepy library was used to connect to Twitter's API.
- Twitter's API was used to extract tweets and classify them in real time as shown on the livePredictor.ipynb file.
- The credentials.py file has been ommitted from the github repo as this file contains personal Twitter developer account credentials.
