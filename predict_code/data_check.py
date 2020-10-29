import pandas as pd
from itertools import chain
from predict_code.multiprocess_model import send_data
class check_html_data:
    def __init__(self,list_data):
        self.list_data=list_data
    def check_data(self):
       # print(self.list_data)
        key_list = list(self.list_data.keys())
        dat_list=[] 
        if "neural_network" in key_list:
            data_o="single"
            key_data=['neural_network','text_data','file_name']
            out = {x: self.list_data[x] for x in key_data}
            dat_list.append(out)

        if "lstm_model" in key_list:
            data_o="lstm"
            key_data=['lstm_model','text_data','file_name']
            out = {x: self.list_data[x] for x in key_data}
            dat_list.append(out)

        if "Conv_network" in key_list:
            data_o="conv"
            key_data=['Conv_network','text_data','file_name']
            out = {x: self.list_data[x] for x in key_data}
            dat_list.append(out)
        len_data=len(dat_list)
        send_value3=send_data(len_data,dat_list)
        data_out=send_value3.worker()
        data_value=list(chain.from_iterable(data_out))
        conv_data_v = list(filter(lambda x: x['model'] in ['Conv_network'], data_value))
        neural_network = list(filter(lambda x: x['model'] in ['neural_network'], data_value))
        lstm_data_v = list(filter(lambda x: x['model'] in ['Lstm_model'], data_value))
        data_save=[]
        if (len(conv_data_v)>0):
            conv_neural_sort=[d for d in conv_data_v if d['sentiment_type']=="Positive"] 
            conv_neural_sort2=[d for d in conv_data_v if d['sentiment_type']=="Negative"] 
            conv_data_positive=len(conv_neural_sort)
            conv_data_negative=len(conv_neural_sort2)
            data_output={"conv_network_positive":conv_data_positive,"conv_network_negative":conv_data_negative,"model":"Conv_network"}
            data_save.append(data_output)

        if (len(neural_network)>0):
            neural_network_sort=[d for d in neural_network if d['sentiment_type']=="Positive"] 
            neural_network_sort2=[d for d in neural_network if d['sentiment_type']=="Negative"]
            neural_data_positive=len(neural_network_sort)
            neural_data_negative=len(neural_network_sort2)
            data_output={"neural_network_positive":neural_data_positive,"neural_network_negative":neural_data_negative,"model":"neural_network"}
            data_save.append(data_output)
        if (len(lstm_data_v)>0):
            lstm_network_sort=[d for d in lstm_data_v if d['sentiment_type']=="Positive"] 
            lstm_network_sort2=[d for d in lstm_data_v if d['sentiment_type']=="Negative"] 
            lstm_data_positive=len(lstm_network_sort)
            lstm_data_negative=len(lstm_network_sort2)
            data_output={"lstm_network_positive":lstm_data_positive,"lstm_network_negative":lstm_data_negative,"model":"lstm_network"}
            data_save.append(data_output)
        return data_save    

            









 



        



