import re
import numpy as np
from predict_code.multiprocess_model import read_file
class pre_processing:
    def __init__(self,data_value):
        self.data_value=data_value
    def cleaning_file_data(self):
            TAG_RE = re.compile(r'<[^>]+>')
            self.data_value['review']=self.data_value['review'].apply(lambda elem: TAG_RE.sub('',elem))
            self.data_value['review'] = self.data_value['review'].map(lambda x: x.lower())
            self.data_value['review'] = self.data_value['review'].apply(lambda elem: re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", elem))  
            # remove numbers
            self.data_value['review'] = self.data_value['review'].apply(lambda elem: re.sub(r"\d+", "", elem))
            comment_data=self.data_value['review']
            return comment_data
class create_rating:
    def __init__(self,data_value):
            self.data_value=data_value
    def to_sentiment(self,rating_data):
            if rating_data=="positive":
                return 1
            elif rating_data=="netural":
                return 2
            else:
                return 0
    def rating_value(self):
            modified_rating=self.data_value.sentiment.apply(self.to_sentiment)
            return modified_rating

