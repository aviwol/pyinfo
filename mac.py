import time as t
import platform
import os
import socket
import psutil
import getpass
from os import popen

LOG = []
COMMANDS = {}
WINDOWS_COMMANDS = {'system': platform.system, 'processor': platform.processor, 'machine': platform.machine, 'release': platform.release, 'version': platform.version, 'login': os.getlogin, 'ipv6': socket.has_ipv6, 'ipv4': socket.gethostbyname(socket.gethostname()), 'host': socket.gethostname}
MAC_COMMANDS = {'system': platform.system, 'processor': platform.processor, 'machine': platform.machine, 'release': platform.release, 'version': platform.version, 'login': os.getlogin, 'ipv6': socket.has_ipv6, 'ipv4': socket.gethostbyname(socket.gethostname()), 'host': socket.gethostname}

if platform.system() == 'Darwin':
    COMMANDS = MAC_COMMANDS
elif platform.system() == 'Windows':
    COMMANDS = WINDOWS_COMMANDS

def excute(command, command_name):
    if type(command) == bool:
        local_query = command
    elif type(command) == str:
        local_query = command
    else:
        local_query = command()
    write_to_log({command_name: local_query})


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
		<title>Log for{0}</title>
	</head>
	<body>
	<h1>Log info for {0}</h1>
	<table>
	<thead>
		<th>Title</th>
		<th>Value</th>
	</thead>
	<tbody>
	'''.format(t.ctime())
	for i in log:
		base_html += "<tr><td>{0}</td><td>{1}</td></tr>".format(i.keys()[0], i[i.keys()[0]])
	end_html = '''
	</tbody>
	</table>
	</body>
	</html>
	'''
	f = open('info.html', 'wb')
	f.write(base_html + end_html)
	f.close()


if __name__ == '__main__':
	run_commands()
	write_html(LOG)
