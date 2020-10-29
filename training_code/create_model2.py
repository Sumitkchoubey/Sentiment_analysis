from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
class create_model_setup:
    def __init__(self,data_value):
        self.comment=data_value
    def create_tokenize(self):
        tokenizer = Tokenizer(num_words=5000)
        tokenizer.fit_on_texts(self.comment)
        vocab_size = len(tokenizer.word_index) + 1
        encoded_docs = tokenizer.texts_to_sequences(self.comment)
        padded_sequence = pad_sequences(encoded_docs, maxlen=200)
        return vocab_size,padded_sequence
    
