# encoding=utf8  
import requests
import json
import sys
import time

reload(sys)  
sys.setdefaultencoding('utf8')

def cmd2JSON(cmd , workspace_name=""):
	return json.dumps({'Stmt':cmd,'Workspace':workspace_name,'Opts':{}})

def json_stream(fp):
	for line in fp:
		yield json.loads(line)

def return_getData(server,cmdStr, workspace_name , timeout=9999):
	ret_str = ""
	r = requests.post(server,data=cmd2JSON(cmdStr, workspace_name) , stream=True , timeout=timeout)
	for content in json_stream(r.raw):
		ret_str = ret_str + return_printdata(json.dumps(content))
	return ret_str
	
def return_printdata(data_str):
	data = json.loads(data_str)
	return_str = ""
	if(type(data['Content']) != dict):
		if json.dumps(data['Content']) != "null":
			if data['Content'] != "":
				return_str = json.dumps(data['Content'])
		else:
			if data['Err']!= "":
				return_str = json.dumps(data['Err'])
		return return_str	

	if 'content' in data['Content'].keys():
		for row in data['Content']['content']:
			print_row=""
			for record in row:
				if print_row != "":
					print_row += ","
                    		print_row += str(record).decode('utf-8')
			return_str = return_str + print_row + "\n"
	else:
		if data['Content'] != "":
			return_str = json.dumps(data['Content'])
	
	return return_str
 

def shell_return(connargs, shell_name, command):
	bo_url = "http://" + connargs["host"] + ":" + str(connargs["port"]) + "/cmd"
	return return_getData(bo_url, command, connargs["workspace"] , connargs["timeout"]) 

