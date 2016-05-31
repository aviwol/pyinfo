# pyinfo
Python script to generate an html with system data.

The "Pyinfo" script generates an html page of the data about the system using built in functions. <br>
The script came up as a personal need and I decided to share it to the public. <br>
It is very usefull for IT people who want to get info on the system they are checking manually and to see the data nicely and organized. <br>
The project currently only supports Windows computers but later it will support Mac's and Linux computers as well. <br>
Notice that there is no install file in order to make it as easy as possible to edit the code. <br>

The data will be generated into an html file named "info.html" at the projects folder. <br>

# Running the code from the command line:

In order to run your code from the command line you need to navigate to the "pyinfo" folder and run the "win.py".<br>
By default the script will run all the commands but if you would like to get specific data you have these two options:
  - If you want to get data on a specific attribute you can write it as following: "```python win.py ipv4```".
  - If you would like to get more then one attribute you can use the ```"+"``` sign as follows: ```"python win.py ipv4+ipv6+username"```.

# Adding your command:
Adding your own command can be done in the `"COMMANDS"` dictionary. <br>
By default the script will act to your input as a function and try excuting it. If you would like to input a variable or a "wmic" command you have the following options:
  - ``` "wmic:xxx" ``` (Where xxx is your command) - This will run your comamnd as a wmic command.
  - ``` "alone:xxx" ``` (Where xxx is your command) - The script will act towards this as a variable. (Returning the value of ```COMMANDS[xxx]```)

# List of data you can get as of now:

  ```'system'``` - Will return the system OS <br>
  ```'processor'``` - Will return the processor information <br>
  ```'machine'``` - Returns machine type <br>
  ```'platform-release'``` - Returns platforms name <br>
  ```'platform-version'``` - Returns platforms version <br>
	```'username' - Returns``` current logged in username <br>
	```'wmic:cpu'``` - Returns CPU type <br>
	```'wmic:serial-number'``` - Returns computer S/N (Notice that if your computer is home built there will not be a S/N) <br>
	```'alone:Has-ipv6'``` - Checks if ipv6 is supported, returns "True"/"False" <br>
  ```'alone:ipv4'``` - Gets ipv4 of the computer <br>
  ```'hostname'``` - Returns the hostname <br>
	```'alone:mac-address'``` - Returns the computers mac address <br>



