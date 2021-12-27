from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
import pandas as pd 
app = Flask(__name__)
df = pd.read_csv('base.csv')
df = df.head(5)

df_diff =pd.read_csv('coin_diff.csv')

colnames = ['datetime','coin_name','coin_price']
colnames_diff = ['coin_name','coin_diff','coin_diff_pct']

@app.route('/',methods=['POST','GET'])
def main():
	return render_template('result.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/diff',methods=['POST','GET'])
def diff():
	return render_template('result.html',  tables=[df_diff.to_html(classes='data')], titles=df_diff.columns.values)


if __name__ == "__main__":
    app.run()
