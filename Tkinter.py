import tkinter

main_window = tkinter.Tk()

def event_tekan():
	label = tkinter.Label(main_window, text = "aku ditekan ^-^")
	labell = tkinter.Label(main_window, text = "Oke deh")
	label.pack()
	labell.pack()

label1 = tkinter.Label(main_window, text = "Label 1")
label2 = tkinter.Label(main_window, text = "Label 2")

button1 = tkinter.Button(main_window, text = "tombol1", command = event_tekan)
button2 = tkinter.Button(main_window, text = "tombol2", command = event_tekan)

# method positioning
label1.pack()
label2.pack()

button1.pack()
button2.pack()

# method menampilkan GUI
main_window.mainloop()