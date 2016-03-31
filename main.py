import time as t
import platform
import getpass
from os import popen
import socket as s

LOG = []
COMMANDS = {}
WINDOWS_COMMANDS = {

'platform' : platform.system, 
'processor': platform.processor, 
'username': getpass.getuser, 
'wmic:cpu': 'wmic cpu get name',
'wmic:serial number': "wmic bios get serialnumber", 
'hostname': s.gethostname

}

MAC_COMMANDS = {'platform' : platform.system, 'processor': platform.processor}

if platform.system == 'Darwin':
    COMMANDS = MAC_COMMANDS
elif platform.system() == 'Windows':
    COMMANDS = WINDOWS_COMMANDS

def run_popen(command):
	local_command = popen(command).read()
	return local_command.split("\n")[1]


def excute(command, command_name):
	if(command_name.find("wmic:") > -1):
		command_name = command_name.split("wmic:")[1]
		local_query = run_popen(command)
		write_to_log({command_name: local_query})
	else:
		local_query = command()
		write_to_log({command_name : local_query})


def run_commands():
	for command in COMMANDS.keys():
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
		<title>Log for{0}</title>
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
	'''
	f = open('info.html', 'wb')
	f.write(base_html + end_html)
	f.close()


if __name__ == '__main__':
	run_commands()
	write_html(LOG)