from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import pandas as pd

df = pd.read_excel("/home/anonymous/Internship/Delhi.xlsx",index_col=[0], parse_dates=[0],skiprows=2)
## reading a xlsx file using pandas library
df['pm25']=pd.to_numeric(df['pm25'],errors='coerce')
df.sort_values(by=['date'],ascending=True,inplace=True)
rolling_airquality=df['pm25'].fillna(df.pm25.rolling(36,min_periods=1).mean(),inplace=True)

app = Flask(__name__)

model=pickle.load(open('model.p','rb'))



@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/predict',methods=['GET'])
def predict():
      #output=model.predict([[str(request.args['predict']),]])
        
     #int_features=[int(x) for x in request.args['predict']]
     
     int_features=str(request.args['predict'])
     index_future_dates=pd.date_range(start='2018-04-20 00:00:00',periods=int(int_features),freq='H')
     output=model.predict(start=len(df),end=len(df)+int(int_features)-1,typ='levels').rename('ARIMA Predictions')
     output.index=index_future_dates
     
  
     return str(output)
    


if __name__ == '__main__':
    app.run(debug=True)
