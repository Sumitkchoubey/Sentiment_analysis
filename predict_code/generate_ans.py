import os
import re
import pandas as pd
import numpy as np
from numpy import array
from numpy import asarray
from numpy import zeros
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

class generate_answer:
    def __init__(self,data):
          self.data=data
    def load_model(self):
        key_list = list(self.data.values())
        if "neural_network" in key_list:
            load_model=tf.keras.models.load_model('./model/simple_neural_network_model')
            ans_type="neural_network"
            return load_model,ans_type
        if  "lstm_model" in key_list:
            load_model=tf.keras.models.load_model('./model/lstm4_network_model')
            ans_type="Lstm_model"
            return load_model,ans_type
        if "Conv_network" in key_list:
            load_model=tf.keras.models.load_model('./model/Conv_network_model')
            ans_type="Conv_network"
            return load_model,ans_type
            


    def create_padding(self,data_v):
        comment_data=np.load("./model/comment.npy",allow_pickle=True)

        tokenizer = Tokenizer(num_words=5000)
        tokenizer.fit_on_texts(comment_data)
        tw = tokenizer.texts_to_sequences([data_v])
        #print(tw)
        embbed_data = pad_sequences(tw,maxlen=200)
        #print(embbed_data)
        return embbed_data
    def generate_sentiment(self,embbed_data,model,answer_type):
        prediction = (model.predict(embbed_data))
        #print(prediction)
       
        result_value=[]
        if prediction > 0.47:
            result_dict={"sentiment_type":"Positive","sentiment_value":prediction[0][0],"model":answer_type}
            print(result_dict)
            return result_dict
             
        else:
            result_dict={"sentiment_type":"Negative","sentiment_value":prediction[0][0],"model":answer_type}
            print(result_dict)
            return result_dict
        
    def send_text_data(self,text_data):
        text_data_v = self.data.get('text_data')
        return text_data_v
    def cleaning_file_data(self,data_file):
           # print(type(data_file))
            TAG_RE = re.compile(r'<[^>]+>')
            if (type(data_file))==str:
                return re.sub(TAG_RE, '', data_file)
            else:
                data_value=data_file['review'].apply(lambda elem: TAG_RE.sub('',elem))
           # print(data_value)
                return data_value
    def test_file_format(self):
        file_name=self.data.get("file_name")
        text_file=self.data.get("text_data")
        #result_data=[]
        if text_file:
            text_data=self.data.get("text_data")
           # read_file=pd.read_csv(file_name)
            load_file,answer_type=self.load_model()
            clean_file_data=self.cleaning_file_data(text_data)
            #clean_file_data=clean_file_data.to_frame()
            create_padd=self.create_padding(clean_file_data)
            result_data=[]

            
            data=self.generate_sentiment(create_padd,load_file,answer_type)
            result_data.append(data)
            return result_data
        elif file_name==None:
            print("data_text")
            text_data=self.data.get("text_data")
           # read_file=pd.read_csv(file_name)
            load_file,answer_type=self.load_model()
            clean_file_data=self.cleaning_file_data(text_data)
            #clean_file_data=clean_file_data.to_frame()
            create_padd=self.create_padding(clean_file_data)
            #create_padd=create_padd.to_frame()
            result_data=[]

            #data=self.generate_sentiment(create_padd,load_file)
            #for i in (create_padd):
            data=self.generate_sentiment(create_padd,load_file,answer_type)
            result_data.append(data)
            return result_data
        else:

            if ".csv" in file_name:

                read_file=pd.read_csv("upload_file/"+file_name)
                load_file,answer_type=self.load_model()
                clean_file_data=self.cleaning_file_data(read_file)
                clean_file_data=clean_file_data.to_frame()
                create_padd=clean_file_data.review.apply(self.create_padding)
                create_padd=create_padd.to_frame()
                result_data=[]

                #data=self.generate_sentiment(create_padd,load_file)
                for i in (create_padd.review):
                    data=self.generate_sentiment(i,load_file,answer_type)
                    result_data.append(data)
                
                return result_data
            






    


