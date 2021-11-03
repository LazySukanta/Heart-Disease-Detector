from flask import Flask,render_template,request,url_for,redirect
import pickle
import numpy as np
model=pickle.load(open('heart.pkl','rb'))
app1 = Flask(__name__)

@app1.route('/')
def man2():
    return render_template('index.html')

@app1.route('/check',methods=['GET','POST'])
def man():
    if request.method == 'POST':
        return redirect(url_for('man2'))
    return render_template('form.html')

@app1.route('/CONTACT US',methods=['GET', 'POST'])
def man1():
    if request.method == 'POST':
        return redirect(url_for('man2'))
    return render_template('CONTACT US.html')

@app1.route('/predict',methods=['POST'])
def index():
    data1= request.form['value1']
    data2= request.form['value2']
    data3= request.form['value3']
    data4= request.form['value4']
    data5= request.form['value5']
    data6= request.form['value6']
    data7= request.form['value7']
    data8= request.form['value8']
    data9= request.form['value9']
    data10= request.form['value10']
    data11= request.form['value11']
    data12= request.form['value12']
    data13= request.form['value13']
    arr=np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13]])
    pred=model.predict(arr)
    return render_template('result1.html',data=pred)

if __name__=="__main__":
    app.run(debug=True)

