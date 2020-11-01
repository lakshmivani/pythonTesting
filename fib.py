import mysql.connector as mdb
from flask import Flask
app=Flask(__name__)
def querysql(cnt):
	mydb=mdb.connect(host="127.0.0.1",user='root',password='root',db='automaton')
#print(dir(mydb))
	try:
		cursor=mydb.cursor(buffered=True,dictionary=True)
		print(cursor)
		print("tyy")
		query=cnt
		print(query)
		cursor.execute(query)
		print('res')
		fname = cursor.fetchone()
		
		cursor.close()
		mydb.commit()
		mydb.close()
		return fname
	except mdb.Error as e:
		import traceback
		print(traceback.format_exc())
		print(e)
@app.route('/')
def get():
	query='select * from `atm-scripts`;'
	res=querysql(query)
	print(res)
	return res.__str__()
@app.route('/hello')	
def post():
	query="insert into testing(ts_name,ts_id) values('krishna', 698)"
	querysql(query)
	return "post method"

if __name__ == '__main__':
	
	app.run(debug=True)

