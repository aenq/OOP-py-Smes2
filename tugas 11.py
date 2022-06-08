print("Nomor 1")
from tkinter import *
rachel = Tk()

class Hero(object):
	def __init__(self, nama= None, alias = None, kelompok = None, kondisi = None):
		self.nama = nama
		self.alias = alias
		self.kelompok = kelompok
		self.kondisi = kondisi

i = 0
def input():
	for i in range(ask.get()):
		labelNama = Label(rachel, text="Nama Hero :")
		labelAlias = Label(rachel, text="Alias Hero :")
		labelKelompok = Label(rachel, text="Kelompok Hero :")
		labelKondisi = Label(rachel, text="Kondisi Hero :")
		nama = Entry(rachel)
		alias = Entry(rachel)
		kelompok = Entry(rachel)
		kondisi = Entry(rachel)
		labelNama.grid()
		nama.grid()
		labelAlias.grid()
		alias.grid()
		labelKelompok.grid()
		kelompok.grid()
		labelKondisi.grid()
		kondisi.grid()
			
		listHero.append(Hero(nama, alias, kelompok, kondisi))
	button2 = Button(rachel, text="Cetak", command=tampil).grid(sticky=W)
	button3 = Button(rachel, text="EXIT", command=rachel.quit).grid(sticky=E)
	
def tampil():
	for Hero in listHero:
		print("Nama: {}\nAlias: {}\nKelompok: {}\nKondisi: {}\n\n".format(Hero.nama.get(), 
		Hero.alias.get(), 
		Hero.kelompok.get(), 
		Hero.kondisi.get()))

listHero = []
labeljumlah  = Label(rachel, text="Ada berapa Hero?").grid(column = 0, row = 0)
ask =IntVar()
question = Entry(rachel,text = ask).grid(column = 1, row = 0)

rachel.title("Rachel 1")
button1 = Button(rachel, text="Enter", command=input).grid(columnspan=2)
rachel.mainloop()


print("Nomor 2")

from tkinter import *
rachel = Tk()

class Hero(object):
	def __init__(self, nama= None, alias = None, kelompok = None, kondisi = None):
		self.nama = nama
		self.alias = alias
		self.kelompok = kelompok
		self.kondisi = kondisi
		
# membuat list dg nama listHero
listHero = []
labeljumlah  = Label(rachel, text="Ada berapa Hero?")
labeljumlah.grid(column = 0, row = 0)
ask =IntVar()
question = Entry(rachel,text = ask)
question.grid(column = 1, row = 0)

i = 0
def input():
	for i in range(ask.get()):
		labelNama = Label(rachel, text="Nama Hero :")
		labelAlias = Label(rachel, text="Alias Hero :")
		labelKelompok = Label(rachel, text="Kelompok Hero :")
		labelKondisi = Label(rachel, text="Kondisi Hero :")
			
		nama = Entry(rachel)
		alias = Entry(rachel)
		kelompok = Entry(rachel)
		kondisi = Entry(rachel)
		
		labelNama.grid()
		nama.grid()
		labelAlias.grid()
		alias.grid()
		labelKelompok.grid()
		kelompok.grid()
		labelKondisi.grid()
		kondisi.grid()
			
		listHero.append(Hero(nama, alias, kelompok, kondisi))
		button2 = Button(rachel, text="Cetak", command=panggilHero)
		button3 = Button(rachel, text="EXIT", command=rachel.quit)
		button2.grid(sticky=W)
		button3.grid(sticky=E)
		
def panggilHero():
	for Hero in listHero:
		print("Nama Hero: {}\nAlias Hero: {}\nKelompok Hero: {}\nKondisi Hero: {}\n\n".format(Hero.nama.get(), 
		Hero.alias.get(), 
		Hero.kelompok.get(), 
		Hero.kondisi.get()
		))
	assert(Hero.kondisi.get() == "Hidup"), "Hero Meninggal"
	return print("Hero ada disini")

rachel.title("Rachel 2")
button1 = Button(rachel, text="Enter", command=input)
button1.grid(columnspan=2)
rachel.mainloop()

print("Nomor 3")
from tkinter import *
rachel = Tk()
class Hero(object):
	def init(self, nama= None, alias = None, kelompok = None, kondisi = None):
		self.nama = nama
		self.alias = alias
		self.kelompok = kelompok
		self.kondisi = kondisi
listHero = []
labeljumlah  = Label(rachel, text="Ada berapa Hero?").grid(column = 0, row = 0)
ask =IntVar()
question = Entry(rachel,text = ask).grid(column = 1, row = 0)
i = 0
def input():
	for i in range(ask.get()):
		labelNama = Label(rachel, text="Nama Hero :")
		labelAlias = Label(rachel, text="Alias Hero :")
		labelKelompok = Label(rachel, text="Kelompok Hero :")
		labelKondisi = Label(rachel, text="Kondisi Hero :")
		nama = Entry(rachel)
		alias = Entry(rachel)
		kelompok = Entry(rachel)
		kondisi = Entry(rachel)
		labelNama.grid()
		nama.grid()
		labelAlias.grid()
		alias.grid()
		labelKelompok.grid()
		kelompok.grid()
		labelKondisi.grid()
		kondisi.grid()
		listHero.append(Hero(nama, alias, kelompok, kondisi))
		button2 = Button(rachel, text="Cetak", command=panggilHero).grid(sticky=W)
		button3 = Button(rachel, text="EXIT", command=rachel.quit).grid(sticky=E)
		
def panggilHero():
	for Hero in listHero:
		print("Nama Hero: {}\nAlias Hero: {}\nKelompok Hero: {}\nKondisi Hero: {}\n\n".format(Hero.nama.get(), 
		Hero.alias.get(), 
		Hero.kelompok.get(), 
		Hero.kondisi.get()))
def mainloop():
	try:
		hero = input("panggilHero: ")
		panggilHero(hero)
	except:
		print("Hero bukan bagian dari Avengers! ")
	else :
		print("sytax Error")
	finally :
		isHero = false
		for i in listHero:
			if hero == i.nama :
				print(f"Hero Bagian dari{i.klompok}")
				isHero = True
		if not isHero:
			print("Bukan Hero")

	assert(Hero.kondisi.get() == "Hidup"), "Hero Meninggal"
	return print("Hero ada disini")

rachel.title("Rachel 3")
button1 = Button(rachel, text="Enter", command=input)
button1.grid(columnspan=2)
rachel.mainloop()