from tkinter import *

class GUIpertama:
	def __init__(self, master):
		self.master = master
		master.title("BAB 10")
		self.label = Label(master, text = "Kelas PBO Python!")
		self.label.pack()
		self.salam_button = Button(master, text = "Salam", command = self.greet)
		self.salam_button.pack()
		self.keluar_button = Button(master, text = "Keluar", command=master.quit)
		self.keluar_button.pack()

	def greet(self):
		print("Selamat Siang!")
		button1 = Button(root, text = "out")
		button1.pack()

root = Tk()
my_gui = GUIpertama(root)
root.mainloop()