import bo_restful
import random
from flask import Flask
from flask import render_template
from flask import request 
from random import randint
from datetime import datetime, timedelta


connargs={}
connargs["host"]="localhost"
connargs["port"]=9090
connargs["timeout"]=9999
connargs["workspace"]=""

app = Flask(__name__)

@app.route("/" , methods=['POST', 'GET'])
def todo():
	username = "testuser"
	ping = bo_restful.shell_return(connargs , "" , "select * from todo limit 1")
	if ping == "\"Object doesn't exist: table 'todo'\"":
		ret = bo_restful.shell_return(connargs , "" , "create table todo(user STRING, category STRING , title STRING ,detail STRING, time DATETIME32, completion DOUBLE) ")
		print("create table")

	message = "\n** show all data **\n" + bo_restful.shell_return(connargs , "" , "select * from todo")
	message2 = "\n** weekly avg. completion by category **\n" + bo_restful.shell_return(connargs , "" , "find category, week(time), avg(completion) from todo")
	if request.method == 'POST':
		category = request.form['category']
		title = request.form['title']	
		detail = request.form['detail']
		random_date = datetime.now() + timedelta(seconds=randint(0,2000000))

		insert_stmt = "insert into todo values ('" + username + "','" + category + "','" + title + "','" + detail + "','" + datetime.strftime( random_date,"%Y-%m-%d %H:%M:%S") + "','" + str(random.random()) + ")"
		ret = bo_restful.shell_return(connargs , "" , insert_stmt)
		message = "\n** show all data **\n" + bo_restful.shell_return(connargs , "" , "select * from todo where 'user'='" + username + "'")			
		message2 = "\n** weekly avg. completion by category **\n" + bo_restful.shell_return(connargs , "" , "find category, week(time), avg(completion) from todo")
		return render_template('todo.html', username=username, msg=message, msg2=message2, cate=category, title=title,  deta=detail)

	return render_template('todo.html', username=username , msg=message, msg2=message2)


if __name__ == "__main__":
	app.debug = True
	app.run()
