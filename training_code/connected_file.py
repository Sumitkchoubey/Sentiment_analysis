import os
import numpy as np
from  training_code.read_file import read_file
from training_code.data_preprocess import pre_processing,create_rating
from training_code.create_model2 import create_model_setup
class training_data:
    def __init__(self,file_data):
        self.file_data=file_data
        
    def processing_training_file(self):
        
        file_data=read_file(self.file_data)
        data_value=file_data.read_data()
        data_pre_processing=pre_processing(data_value)
        data_pre_process_output=data_pre_processing.cleaning_file_data()
        create_rating_value=create_rating(data_value)
        rating_data=create_rating_value.rating_value()
        #rating_value=np.array(rating_data)
        comment_data_value=data_pre_process_output.to_frame()
        comment_data_v = comment_data_value.review.values
        cwd = os.getcwd()   
        path="./model"
        isdir = os.path.isdir(path)  
        if isdir==True:
            pass
        else:
            os.mkdir("model")
        comment_save=np.save("./model/comment",comment_data_v)
        return comment_data_v,rating_data
    def training_model(self):
        comment_data,rating_data=self.processing_training_file()
        tokenise_data=create_model_setup(comment_data)
        vocab_siz,padding_sequence=tokenise_data.create_tokenize()
        return vocab_siz,padding_sequence,rating_data

        

