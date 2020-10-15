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

### Repo Directory:

All of the important models in this project are found on the following directories within the repo:

1. Base model: BaseModel.ipynb
2. Word2Vec models: Word2VecModels.ipynb
3. Keras Embedding Layer Models: Keras_Embedding_Layer.ipynb
4. GloVe Models: GloveModels.ipynb
5. Live Prediction using Glove+LSTM model: livePredictor.ipynb 
6. Comparison of feature extraction techniques: miscellaneous/feature_extraction_techniques_comparison.ipynb
7. Investigation of influence of location on classification: 
  - miscellaneous/influence_location_performance.ipynb
  - Keras_Embedding_Layer_With_Location_Feature.ipynb
8. Correction of location names: miscellaneous/namesCorrection.ipynb
9. Optimization of Word2vec models: miscellaneous/word2vecOptimization.ipynb
10. Data Exploration: Exploring dataset.ipynb
11. Dictionary models: /Dictionary_Models/
12. Embedding Layer models: /Embedding_Models/
13. Neural network models and weights: /NN_Models/
14. Licenses: /Licenses/
15. Datasets: /nlp-getting-started/
