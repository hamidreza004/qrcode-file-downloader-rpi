from pySmartDL import SmartDL

class DownloadManager:
	def __init__(self): 
		self.files = []
		self.selected = 0

	def pause(self):
		self.files[self.selected].pause()

	def resume(self):
		self.files[self.selected].unpause()

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
		f = SmartDL(link, "./Downloads")
		f.start(blocking=False)
		self.files.append(f)

	def update_display(self):
		# TODO
		pass

	
def get_event():
	# TODO
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
	while True:
		e = get_event()
		if e == 0:
			print("Bye!")
			break
		if e == 8:
			download_manager.add_link(input())
