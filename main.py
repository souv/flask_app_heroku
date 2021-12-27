from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
import pandas as pd 
app = Flask(__name__)
df = pd.read_csv('base.csv')
df = df.head(5)

colnames = ['datetime','coin_name','coin_price']

@app.route('/',methods=['POST','GET'])
def main():
	return render_template('result.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == "__main__":
    app.run()
