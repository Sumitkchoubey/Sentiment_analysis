
from predict_code.data_check import check_html_data
from training_code.data_checking import training_html_data
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import os
import time
start_time = time.time()
app = Flask(__name__,template_folder='template')
UPLOAD_FOLDER = 'upload_file'
TRANING_DATA_FOLDER='data'
app.secret_key = "secret key"
app.config['TRANING_DATA_FOLDER']=TRANING_DATA_FOLDER
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/text_test/')
def student():
   return render_template('page.html')
@app.route('/file_upload/')
def file_upload():
   return render_template('file_upload.html')
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(start_time)
      dict_data=result.to_dict()
      print(dict_data)
      if 'file' not in request.files:
            add_file={"file_name":None}
            dict_data.update(add_file)
            send_data=check_html_data(dict_data)
            send_data_value=send_data.check_data()
            print("--- %s seconds ---" % (time.time() - start_time))

            return render_template("result.html",result = send_data_value)
      
      else:
            file = request.files['file']
            if file.filename == '':
                  add_file={"file_name":None}
                  dict_data.update(add_file)
                  send_data=check_html_data(dict_data)
                  send_data_value=send_data.check_data()

                  return render_template("result.html",result = send_data_value)
            if file and allowed_file(file.filename):

                  filename = secure_filename(file.filename)
                  basedir = os.path.abspath(os.path.dirname(__file__))
                  file.save(os.path.join(basedir,app.config['UPLOAD_FOLDER'], filename))
                  flash('File successfully uploaded')
                  add_file={"file_name":filename}
                  add_file2={"text_data":None}
                  dict_data.update(add_file2)
                  dict_data.update(add_file)
                  send_data=check_html_data(dict_data)
                  send_data_value=send_data.check_data()
                  print(send_data_value)
                  return render_template("result.html",result = send_data_value)
            else:
                  print("dert")

@app.route('/file_training/')
def file_training():
   return render_template('file_training.html')  
@app.route('/training_succ',methods = ['POST']) 
def training_succ():
      if request.method == 'POST':
            result = request.form
           
            dict_data=result.to_dict()
      file = request.files['file']
     
      if file and allowed_file(file.filename):
                  filename = secure_filename(file.filename)
                  basedir = os.path.abspath(os.path.dirname(__file__))
                  isdir = os.path.isdir(app.config['TRANING_DATA_FOLDER'])  
                  if isdir==True:
                        pass
                  else:
                        os.mkdir(app.config['TRANING_DATA_FOLDER'])
                  file.save(os.path.join(basedir,app.config['TRANING_DATA_FOLDER'], filename))
                  flash('File successfully uploaded & training is Done')
                  add_file={"file_name":filename}
                  dict_data.update(add_file)
                 
                  training_html_d=training_html_data(dict_data)
                  run_training=training_html_d.run_files()
                  d={"succ":"yes"}
                  re=[]
                  re.append(d)
                  return render_template("training_succ.html",result = re)



            

if __name__ == '__main__':
   app.run(debug = True)