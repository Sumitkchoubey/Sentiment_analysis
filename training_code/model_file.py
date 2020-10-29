import pandas as pd
import numpy as np
import re
import os
import nltk
import tensorflow as tf
from tensorflow import keras
from numpy import array
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dropout, Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import GlobalMaxPooling1D
from tensorflow.keras.layers import Embedding
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

from tensorflow.keras.layers import SpatialDropout1D
from tensorflow.keras.layers import Embedding

class simple_neural_model:
    def __init__(self,vocab_size):
        self.vocab_size=vocab_size
    def create_model(self):
        embedding_vector_length = 32
        model = Sequential()
        model.add(Embedding(self.vocab_size, embedding_vector_length,     
                                            input_length=200) )   

        model.add(Flatten())
        model.add(Dense(1, activation='sigmoid'))                           
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])   
        return model
class cnn_model:
    def __init__(self,vocab_size):
        self.vocab_size=vocab_size
    def create_model(self):
        embedding_vector_length = 32
        model = Sequential()
        model.add(Embedding(self.vocab_size, embedding_vector_length,     
                                            input_length=200) )
        model.add(tf.keras.layers.Conv1D(32, 5, activation='relu'))
        model.add(GlobalMaxPooling1D())
        model.add(Dense(1, activation='sigmoid'))
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
        return model
class lstm_model:
    def __init__(self,vocab_size):
        self.vocab_size=vocab_size
    def create_model(self):
        embedding_vector_length = 32
        model = Sequential()
        model.add(Embedding(self.vocab_size, embedding_vector_length,     
                                            input_length=200) )
        model.add(SpatialDropout1D(0.25))
        model.add(LSTM(50, dropout=0.5, recurrent_dropout=0.5))
        model.add(Dropout(0.2))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy',optimizer='adam', 
                                metrics=['accuracy'])
        return model

class model_traing:
    def __init__(self,padd_sequence,rating_data,model,model_type):
        self.padd_sequence=padd_sequence
        self.rating_data=rating_data
        self.model=model
        self.model_type=model_type
        print(type(self.padd_sequence))
    def training(self):
        data=self.model.fit(self.padd_sequence,self.rating_data,
                  validation_split=0.2, epochs=5,)
       
        return self.model