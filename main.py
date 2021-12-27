
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
import pandas as pd 
app = Flask(__name__)
df = pd.read_csv('base.csv')
#df = df.head(5)

df_diff =pd.read_csv('coin_diff.csv')

colnames = ['datetime','coin_name','coin_price']
colnames_diff = ['coin_name','coin_diff','coin_diff_pct']

@app.route('/',methods=['POST','GET'])
def main():
    custid_t = request.values.to_dict()
    
    cust_id_dict = {k: v for k, v in custid_t.items() if k.startswith('prodid')}	
    
    key_list = []
    for key in cust_id_dict.values():
        key_list.append(key)	
	
    filter_df = df[df['coin_name'].isin(key_list)] 
    filter_df2 = filter_df.sort_values(by=['coin_name','datetime'])
    return render_template('login.html',  tables=[filter_df2.to_html(classes='data')], titles=filter_df2.columns.values,coin_list=sorted(list(df['coin_name'].unique())))

@app.route('/diff',methods=['POST','GET'])
def diff():
	custid_t = request.values.to_dict()
	cust_id_dict = {k: v for k, v in custid_t.items() if k.startswith('prodid')}
	key_list = []
	for key in cust_id_dict.values():
		key_list.append(key)	
	filter_df = df_diff[df_diff['coin_name'].isin(key_list)] 
	return render_template('result.html',  tables=[filter_df.to_html(classes='data')], titles=df_diff.columns.values,coin_list=sorted(list(df['coin_name'].unique())))

if __name__ == "__main__":
    app.run()
