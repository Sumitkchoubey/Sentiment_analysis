from predict_code.generate_ans import generate_answer
import pandas as pd
from multiprocessing import Pool

class send_data:
    def __init__(self,list_len,data_value):
        self.list_len=list_len
        self.data_value=data_value
    def create_ans(self,data_value):
        data_send=generate_answer(data_value)
        #print(self.data_value)
        #load_model=data_send.load_model()
        #send_data=data_send.send_text_data(data_value)
        #create_padding=data_send.create_padding(send_data)
        gen_data=data_send.test_file_format()
        #gen_data=data_send.generate_sentiment(create_padding,load_model)
        return gen_data
    def worker(self):
        with Pool(5) as p:
                r=(p.map(self.create_ans, self.data_value))
        return r
    