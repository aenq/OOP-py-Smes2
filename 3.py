import tkinter
from tkinter import *

root = Tk()
root.title("Sigitiga")
root.title("Rachel Marta Maria")
def hitungLuas():
    print("Luas = ",0.5*a.get()*c.get(),'cm2')

alas = Label(root, text='Sisi Alas   :').place(x=10,y=10,height=37)
a = IntVar()
b = Entry( root , text = a ).place(x=180,y=10,height=37)

tinggi = Label(root, text='Sisi Tinggi :').place(x=5,y=70,height=37)
c = IntVar()
d = Entry( root , text = c ).place(x=180,y=70,height=37)

e = Button( root , text = ' Luas Segitiga ' , command = hitungLuas ).place(x=150,y=120,height= 45)

root.mainloop()