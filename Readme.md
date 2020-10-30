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
  * Run python app.py and It Start a server in the port number  http://127.0.0.1:5000/
  * For file upload open the link http://127.0.0.1:5000/file_training/ in the Web browser for upload a training data .It saves the dataset into the data folder which is creates during uploading and start trainng training on the based on the selected model.
  * After complete training it return a response in http://127.0.0.1:5000/training_succ in the link as a File upload Successful and the model training is done, and It saves the model file into the model folder that is also creates during training based on selected model during training and it save the review data as a numpy array inside the model folder as a name of comment data.
  * To test the model with a  text file open the link http://127.0.0.1:5000/text_test/ and inside the text box write multiple sentences and select model default select is Lstm Model and the result is display in the http://localhost:5000/result link with a answer as a positive one or negative one because here it is only one sentence.
  * To test with a .csv file upload it through a http://127.0.0.1:5000/file_upload/ in the file there are one column name of review where all the reviews are written and it return a list of positive and negative sentence in the the http://localhost:5000/result  file based on the seletec model.
  * The download link of IMDBdataset and trained model is https://drive.google.com/file/d/16R7cC3GUwqKs4SqVUaSM2Mqp0TxpOemL/view.
  
## Result
 ## The training Result 
  * The Training accuracy of LSTM Model is about 90 precent and validation accuracy about 88 percent
    ![lstm_moel_training_validation2](https://user-images.githubusercontent.com/24955305/97660591-17b4ad00-1a98-11eb-86fb-7da3deb8611c.png)
  * The training accuracy of Simple Neural Network is about 98 Percent but the accuracy in Validation is about 87 percent
    ![normal_neural_model_training_validation2](https://user-images.githubusercontent.com/24955305/97660891-db358100-1a98-11eb-8133-7113e508ad83.png)
  * The training accuracy of Convolution Neural Network Model is about 97 percent and validation accuracy is about 87 percent
    ![cnn_moel_training_validation2](https://user-images.githubusercontent.com/24955305/97661131-8ba38500-1a99-11eb-802d-6ad6960e43bc.png)
 ## The testing result
 * I create a sample test3.csv file consist  of 10 reviews on that and test with this three model and get the accuracy above 90 percent and the backend output of each model is    about 
 * For Convolution Neural Network output sample
  [{'sentiment_type': 'Positive', 'sentiment_value': 0.842661, 'model': 'Conv_network'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.99748635, 'model': 'Conv_network'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.9881045, 'model': 'Conv_network'}, {'sentiment_type': 'Negative', 'sentiment_value': 0.013912744, 'model': 'Conv_network'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.9523934, 'model': 'Conv_network'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.98041373, 'model': 'Conv_network'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.5237386, 'model': 'Conv_network'}, {'sentiment_type': 'Negative', 'sentiment_value': 0.0031370197, 'model': 'Conv_network'}, {'sentiment_type': 'Negative', 'sentiment_value': 0.00025191973, 'model': 'Conv_network'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.9984534, 'model': 'Conv_network'}]
* For Simple Neural Network Output sample 
[{'sentiment_type': 'Positive', 'sentiment_value': 0.93726605, 'model': 'neural_network'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.9978155, 'model': 'neural_network'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.8757394, 'model': 'neural_network'}, {'sentiment_type': 'Negative', 'sentiment_value': 0.0027215637, 'model': 'neural_network'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.9884432, 'model': 'neural_network'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.99449086, 'model': 'neural_network'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.48256207, 'model': 'neural_network'}, {'sentiment_type': 'Negative', 'sentiment_value': 0.06593483, 'model': 'neural_network'}, {'sentiment_type': 'Negative', 'sentiment_value': 6.535258e-07, 'model': 'neural_network'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.9747069, 'model': 'neural_network'}]
* For LSTM output Sample
[{'sentiment_type': 'Positive', 'sentiment_value': 0.97845876, 'model': 'Lstm_model'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.96153134, 'model': 'Lstm_model'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.9662111, 'model': 'Lstm_model'}, {'sentiment_type': 'Negative', 'sentiment_value': 0.03642609, 'model': 'Lstm_model'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.9755795, 'model': 'Lstm_model'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.98600125, 'model': 'Lstm_model'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.88367355, 'model': 'Lstm_model'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.7367587, 'model': 'Lstm_model'}, {'sentiment_type': 'Negative', 'sentiment_value': 0.011675335, 'model': 'Lstm_model'}, {'sentiment_type': 'Positive', 'sentiment_value': 0.9355718, 'model': 'Lstm_model'}]
* And the Final output Which is Dispay in brower is  the Count of Positive and Negative in Every Model
[{'conv_network_positive': 7, 'conv_network_negative': 3, 'model': 'Conv_network'}, {'neural_network_positive': 7, 'neural_network_negative': 3, 'model': 'neural_network'}, {'lstm_network_positive': 8, 'lstm_network_negative': 2, 'model': 'lstm_network'}]
* Test with a single text data of some hole reviews It get a good Result on predection sample like 
 text: "Family of 4 with 2 teenage boys stayed here for 1 week in august. Hotel COVID secure at all times. Queues for restaurant and bars all socially distanced. Meal times split so never too busy, socially distanced seating in the restaurant. The manager of the hotel oversaw thus at all times. Great variation of food. Great variety of drinks on the all inclusive. All staff in the hotel speak English, they always assist you with a smile, nothings ever too much. Dimitra at the pool bar was great, really friendly, made great toasties. The entertainment for good for the whole week, lots of quizzes and shows. Cleaners were really friendly, always said hello. Assisted you with toilet rolls, pillows etc... if you needed them. Nothing was ever any bother. Free water park entry (great fun) and you could also eat there for free in the evening if you booked in. Free bottled water at the front reception desk if you needed any. Fridge in room which was stocked with water. Rooms massive with a separate dividing section/partition if needed. We had a pole view and sea view. Very quiet at night when sleeping. Would definitely recommend this hotel as we had a brilliant holiday and will return. Thank you everyone for a lovely stay."
 All these Three model predict it as a Positive sentence with Good Accuracy.
 
