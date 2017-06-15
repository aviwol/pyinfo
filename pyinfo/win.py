import time as t
import platform
import getpass
from os import popen
import socket
import sys
import uuid
import re

startTime = t.time()
LOG = []
COMMANDS = {

    'system': platform.system, 
    'processor': platform.processor, 
    'machine': platform.machine, 
    'platform-release': platform.release, 
    'platform-version': platform.version, 
	'username': getpass.getuser, 
	'wmic:cpu': 'wmic cpu get name',
	'wmic:serial-number': "wmic bios get serialnumber", 
	'alone:Has-ipv6': socket.has_ipv6, 
    'alone:ipv4': socket.gethostbyname(socket.gethostname()), 
    'hostname': socket.gethostname,
	'alone:mac-address': ':'.join(re.findall('..', '%012x' % uuid.getnode()))
}

def run_popen(command):
	local_command = popen(command).read()
	return local_command.split("\n")[1]


def excute(command, command_name):
	
	if(command_name.find("wmic:") > -1):
		command_name = command_name.split("wmic:")[1]
		local_query = run_popen(command)
		write_to_log({command_name: local_query})
	
	elif command_name.find("alone:") > -1:
		new_command_name = command_name.split("alone:")[1]
		write_to_log({new_command_name: COMMANDS[command_name]})

	else:
	    if type(command) == bool:
	        local_query = command
	    elif type(command) == str:
	        local_query = command
	    else:
	        local_query = command()
		write_to_log({command_name : local_query})


def run_commands(commands_to_run="all"):
	if commands_to_run ==  "all":
		for command in COMMANDS.keys():
			excute(COMMANDS[command], command)
	else:
		for command in commands_to_run.split("+"):
			excute(COMMANDS[command], command)


def write_to_log(info):
	LOG.append(info)


def write_html(log):
	base_html = '''
	<!DOCTYPE html>
	<html>
	<head>
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
		<link rel="stylesheet" href="./main.css" />
		<title>Log for {0}</title>
	</head>
	<body>
	<div class="jumbotron">
	<h2>Log info for <code class="purplfy">{0}</code>:</h2>
	<table class="table table-bordered table-striped">
	<thead>
		<th>Title</th>
		<th>Value</th>
	</thead>
	<tbody>
	'''.format(t.ctime())
	for i in log:
		base_html += "<tr><td><code class='greenfy'>{0}:</code></td><td><code>{1}</code></td></tr>".format(i.keys()[0], i[i.keys()[0]])
	end_html = '''
	</tbody>
	</table>
	</div>
	</body>
	</html>
	<!-- Generated in around {0} seconds -->
	'''.format(t.time() - startTime)
	f = open('info.html', 'wb')
	f.write(base_html + end_html)
	f.close()

def check_arguments():
	if len(sys.argv) <= 1:
		run_commands()
	else:
		run_commands(sys.argv[1])

if __name__ == '__main__':
	check_arguments()
	# run_commands()
	write_html(LOG)

