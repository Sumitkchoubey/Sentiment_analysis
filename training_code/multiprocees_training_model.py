import os
import pandas as pd
import numpy as np
from multiprocessing import Process ,Lock,Pool
from training_code.connected_file import training_data
from training_code.model_file import simple_neural_model,lstm_model,cnn_model,model_traing
class multiprocess_data:
    def __init__(self,data_list,len_data):
        self.data_list=data_list
        self.len_data=len_data
    def send_data(self,list_data):
        
            key_list = list(list_data.keys())
            vocab_siz=int(list_data.get("vocab_siz"))
            print((vocab_siz))
            padd_sequence=(list_data.get("padd_seq"))
            print(type(padd_sequence))
            rating_data=np.array(list_data.get("rating_data"))
            if "neural_network" in key_list:
                file_data=list_data.get("file_name")
                model_type=list_data.get("neural_network")
                print("neural_network")
                cwd = os.getcwd()   
                print(cwd)
                #read_data=training_data(file_data,model_type)
                #vocab_siz,padd_sequence,rating_data=read_data.training_model()
                simple_neural_model_data=simple_neural_model(vocab_siz)
                create_simple_neural_model=simple_neural_model_data.create_model()
                model_training_data=model_traing(padd_sequence,rating_data,create_simple_neural_model,model_type)
                model_training=model_training_data.training()
               
                model_training.save("model/simple_neural_network_model")
            if "lstm_model" in key_list:
                file_data=list_data.get("file_name")
                model_type=list_data.get("lstm_model")
                cwd = os.getcwd()   
                lstm_model_data=lstm_model(vocab_siz)
                create_lstm_model=lstm_model_data.create_model()
                print(create_lstm_model)
                model_training_data=model_traing(padd_sequence,rating_data,create_lstm_model,model_type)
                model_training=model_training_data.training()
               
                model_training.save("model/lstm4_network_model")
            if "Conv_network" in key_list:
                file_data=list_data.get("file_name")
                model_type=list_data.get("Conv_network")
                
                cnn_model_data=cnn_model(vocab_siz)
                create_cnn_model=cnn_model_data.create_model()
                model_training_data=model_traing(padd_sequence,rating_data,create_cnn_model,model_type)
                model_training=model_training_data.training()
               
                model_training.save("model/Conv_network_model")
           
    def worker(self):
        with Pool(self.len_data) as p:
               r=(p.map(self.send_data,self.data_list))
        return r
       # d=self.send_data(self.data_list)



