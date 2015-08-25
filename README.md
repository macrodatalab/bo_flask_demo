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
    
