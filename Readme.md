# Sentiment Analysis of Positive and Negative Sentences.
## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Result](#result)
## General info
This Sentiment Analysis project is used to identify the positive and negative sentences using three types of model  Simple Neural Network, Convolution Neural Network and Long Short Term Memory Model.
## Technologies
* Python
* Numpy
* Pandas
* Tensorflow keras
* flask

## Setup
  * Run git clone https://github.com/Sumitkchoubey/Sentiment_analysis.git.It Creates an sentiment_analysis folder.
  * Run pip install -r requirements.txt
  * Download any dataset releated to setiment analysis in .csv format where mainly two columns one is review and another is sentiment inside sentiment two types of values one is Positive and another is Negative.Here i use the IMDB dataset that is downloaded from kaggle.
  * Run python app.py
  * For file upload open the link http://127.0.0.1:5000/file_training/ in the Web browser for upload a training data .It saves the dataset into the data folder which is creates during uploading and start trainng training on the based on the selected model.
  * After complete training it return a response in http://127.0.0.1:5000/training_succ in the link as a File upload Successful and the model training is done, and It saves the model file into the model folder that is also creates during training based on selected model during training and it save the review data as a numpy array inside the model folder as a name of comment data.
  * To test the model with a  text file open the link http://127.0.0.1:5000/text_test/ and inside the text box write multiple sentences and select model default select is Lstm Model and the result is display in the http://localhost:5000/result link with a answer as a positive one or negative one because here it is only one sentence.
  * To test with a .csv file upload it through a http://127.0.0.1:5000/file_upload/ in the file there are one column name of review where all the reviews are written and it return a list of positive and negative sentence in the the http://localhost:5000/result  file based on the seletec model.
  * The download link of IMDBdataset and trained model is https://drive.google.com/file/d/16R7cC3GUwqKs4SqVUaSM2Mqp0TxpOemL/view.
  
## Result
  * The Training accuracy of LSTM Model is about 90 precent and validation accuracy about 88 percent
    ![lstm_moel_training_validation2](https://user-images.githubusercontent.com/24955305/97660591-17b4ad00-1a98-11eb-86fb-7da3deb8611c.png)
  * The training accuracy of Simple Neural Network is about 97 Percent but the accuracy in Validation is about 76 percent Which is much lower than LSTM Model
    ![normal_neural_model_training_validation2](https://user-images.githubusercontent.com/24955305/97660891-db358100-1a98-11eb-8133-7113e508ad83.png)
  * The training accuracy of Convolution Neural Network Model is about 97 percent and validation accuracy is about 87 percent
    ![cnn_moel_training_validation2](https://user-images.githubusercontent.com/24955305/97661131-8ba38500-1a99-11eb-802d-6ad6960e43bc.png)


