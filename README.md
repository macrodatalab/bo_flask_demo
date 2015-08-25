# bo_flask_demo
A simple demo to demonstrate how to use BigObject by python flask framework

System requirements

Python 2.7

package: requests, flask
    
    pip install requests flask
    
How to use :

1. pull and run BigObject docker image

    docker pull macrodata/bigobject
    
    docker run -t -d --name bigobject -p 9090:9090 macrodata/bigobject

2. run the demo
    
    python todo.py

3. use a browser to visit http://localhost:5000

    
**todo.py**: a simple todo list demo

	1. When the table "todo" does not exist, create it.
	2. Push the button / Enter to add one row in BigObject as fellows: 
		"category", "title", "detail", "date", "completion"
           The date and completion are randomly generated.
	3. The textarea 1 shows all data in BigObject.
	   The textarea 2 show the average completion based on different categories and weeks.

**bo_restful.py**: send statments to the BigObject server by restful API 

**templates/todo.html** : a html template to show data

Refer to the full documentation [here](https://docs.bigobject.io/)



