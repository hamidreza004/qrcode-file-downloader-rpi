from pySmartDL import SmartDL
import threading
import time
import os

class DownloadManager:
	def __init__(self): 
		self.files = []
		self.selected = 0

	def pause(self):
		self.files[self.selected].pause()

	def resume(self):
		self.files[self.selected].resume()

	def delete(self):
		if len(self.files) == 0:
			return
		del self.files[self.selected]
		if self.selected == 0:
			return
		if self.selected == len(self.files):
			self.selected -= 1

	def later(self):
		if self.selected == len(self.files) - 1:
			return
		self.files[self.selected + 1], self.files[self.selected] = self.files[self.selected], self.files[self.selected + 1]
		self.selected += 1

	def sooner(self):
		if self.selected == 0:
			return
		self.files[self.selected - 1], self.files[self.selected] = self.files[self.selected], self.files[self.selected - 1]
		self.selected -= 1

	def move_up(self):
		self.selected = max(0,self.selected - 1)
	
	def move_down(self):
		self.selected = max(0, min(len(self.files) - 1, self.selected + 1))
	
	def add_link(self, link):
		f = SmartDL(link, "./Downloads", progress_bar=False)
		f.start(blocking=False)
		self.files.append(f)

	def display(self):
		os.system('clear') # ToDo Kiarash! 
		print("""Help:  
	1: Pause selected link
	2: Resume selected link
	3: Delete the selected link
	4: Later download the link
	5: Sooner download the link
	6: Move up
	7: Move down
	8: Add new link
	0: Turn off""")
		s = 0
		for f in self.files:
			if s == self.selected:
				print("[*]",end=" ")
			else:
				print("[ ]",end=" ")
			print(f.dest,end=" ")
			if f.isFinished():
				if f.isSuccessful():
					print("Complete")
				else:
					print("Failed")
			else:
				print(f.get_progress_bar(),end=" ")
				print(f.get_dl_size(human=True),"/",f.get_final_filesize(human=True),end=" ")
				if f.status == "paused":
					print("||")
				else:
					print(">>",f.get_speed(human=True))
			s += 1

	def loop_display(self):
		while True:
			self.display()
			time.sleep(2)
	
def get_event():
	# TODO Kiarash!
	# 1: Pause selected link
	# 2: Resume selected link
	# 3: Delete the selected link
	# 4: Later download the link
	# 5: Sooner download the link
	# 6: Move up
	# 7: Move down 
	# 8: Add new link 
	# 0: Turn off  
	return int(input())


if __name__ == '__main__':
	download_manager = DownloadManager()
	th = threading.Thread(target=download_manager.loop_display)
	th.start()	
	while True:
		e = get_event()
		if e == 0:
			print("Bye!")
			break
		if e == 8:
			download_manager.add_link(input())
			# TODO Kiarash!
		if e == 1:
			download_manager.pause()
		if e == 2:
			download_manager.resume()
		if e == 3:
			download_manager.delete()
		if e == 4:
			download_manager.later()
		if e == 5:
			download_manager.sooner()
		if e == 6:
			download_manager.move_up()
		if e == 7:
			download_manager.move_down()
	

