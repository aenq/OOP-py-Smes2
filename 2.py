from tkinter import *
root = Tk()
root.title("Rachel Marta Maria")

def cetak():
 	Label(root, text="Nama :").grid(column=0, row=5)
 	Label(root, text="NIM :").grid(column=0, row=6)
 	Label(root, text="Prodi :").grid(column=0, row=7)
 	Label(root, text=inputNama.get()).grid(column=1, row=5)
 	Label(root, text=inputNim.get()).grid(column=1, row=6)
 	Label(root, text=inputProdi.get()).grid(column=1, row=7)

#Label
label = Label(root, text="Identitas").grid(column = 1,  row = 0)
labelNama = Label(root, text="Nama").grid(column = 0,  row = 1)
labelNim = Label(root, text="NIM").grid(column = 0,  row = 2)
labelProdi = Label(root, text="Prodi").grid(column = 0,  row = 3)
#################################################
#Inputan
#1
inputNama = Entry(root)
inputNama.grid(column = 1, row = 1)
#2
inputNim = Entry(root)
inputNim.grid(column = 1, row = 2)
#3
inputProdi = Entry(root)
inputProdi.grid(column = 1, row = 3)
#################################################
#Button
Button(root, text='Cetak', command=cetak).grid(column = 1, row = 4)

mainloop()