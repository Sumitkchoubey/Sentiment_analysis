import os
import sys
sys.path.append('./data')
import pandas as pd
#read file
class read_file:
    def __init__(self,file_path):
        self.file_path=file_path
    def read_data(self):
        if ".csv" in self.file_path:
            os.chdir("data")
            data_value=pd.read_csv(self.file_path)
           
            return data_value
        else:
            return "Please give the correct file path and save one column must be review  where comment is present"
#file_data=read_file("C:/Users/USER/Desktop/check/data/my_startup/Sentimentation_analysis/sentiment_analysis/data/IMDB_Dataset.csv")
#data_value=file_data.read_data()
#print(data_value)
