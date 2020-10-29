import pandas as pd
from itertools import chain
from training_code.connected_file import training_data
from training_code.multiprocees_training_model import multiprocess_data

class training_html_data:
    def __init__(self,list_data):
        self.list_data=list_data
    def check_data(self):
        key_list = list(self.list_data.keys())
        dat_list=[] 
        file_data=self.list_data.get("file_name")
        read_data=training_data(file_data)
        vocab_siz,padd_sequence,rating_data=read_data.training_model()
        print(type(padd_sequence))
        add_file={"vocab_siz":vocab_siz,"padd_seq":padd_sequence,"rating_data":rating_data}
        if "neural_network" in key_list:
            data_o="single"
            key_data=['neural_network','file_name']
            out = {x: self.list_data[x] for x in key_data}
            out.update(add_file)
            dat_list.append(out)
        if "lstm_model" in key_list:
            data_o="lstm"
            key_data=['lstm_model','file_name']
            out = {x: self.list_data[x] for x in key_data}
            out.update(add_file)
            dat_list.append(out)

        if "Conv_network" in key_list:
            data_o="conv"
            key_data=['Conv_network','file_name']
            out = {x: self.list_data[x] for x in key_data}
            out.update(add_file)
            dat_list.append(out)
        len_data=len(dat_list)
        
        #print(len_data,dat_list)
        return dat_list,len_data
    def run_files(self):
        data_list,len_data=self.check_data()
        multiprocess_data_detail=multiprocess_data(data_list,len_data)
        worker_start=multiprocess_data_detail.worker()
