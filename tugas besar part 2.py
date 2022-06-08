""" Final project dilaksanakan secara berkelompok. (maksimal 3 orang)
Pilihlah satu topik sebagai tema pengembangan sistem.
Minimal terdiri dari 3 kelas, ada hubungan inheritance
Implementasikan ke dalam kode program (lebih disukai jika dapat mengimplementasikan dalam GUI menggunakan tkinter)
Buatlah laporan final project (FP_NIM.pdf) dan presentasinya.
Presentasi diunggah melalui YouTube (paling lambat sehari sebelum jadwal UAS). """

from tkinter import * 

class Zul:
	def tampilprofil_zul(self):
		labeltampilprofil = Label(cek, text = "Nama     : {}\n Gender   : {}\n Umur     : {}\n Alamat   : {}\n".format(self.nama, self.gender, self.umur, self.alamat), fg = "purple").pack()

class Sela:
	def tampilprofil_sela(self):
		labeltampilprofil = Label(cek, text = "Nama     : {}\n Gender   : {}\n Umur     : {}\n Alamat   : {}\n".format(self.nama1, self.gender1, self.umur1, self.alamat1), fg = "purple").pack()

class RacheL:
	def tampilprofil_rachel(self):
		labeltampilprofil = Label(cek, text = "Nama     : {}\n Gender   : {}\n Umur     : {}\n Alamat   : {}\n".format(self.nama2, self.gender2, self.umur2, self.alamat2), fg = "purple").pack()

class GengUburUbur(Zul, Sela, RacheL):
	def __init__(self):
		self.v = IntVar()
		self.label = Label(cek, text = "Halo, ini adalah profil Geng Ubur Ubur", fg = "blue").pack()
		self.label1 = Label(cek, text = "Mau kenal anggota Geng Ubur Ubur lebih dekat?", fg = "blue").pack(pady=10)
		self.buttonyes = Button(cek, text = "Yes baby", command = self.pilih).pack(pady=5)
		self.buttonno = Button(cek, text = "Gk dulu", command = cek.quit).pack()

	def pilih(self):
		self.v = IntVar()
		Label(cek, text = "SILAHKAN DIPILIH SHAY!!!", fg = "blue").pack(pady=5)
		Radiobutton(cek, text= "Zul", variable=self.v, value = 1, command=self.tampilprofil_zul).pack()
		Radiobutton(cek, text= "Sela", variable=self.v, value  = 2, command=self.tampilprofil_sela).pack()
		Radiobutton(cek, text= "Rachel", variable=self.v, value = 3, command=self.tampilprofil_rachel).pack()
		labelPesan = Label(cek, text = "Pesan untuk Geng Ubur-Ubur:", fg = "blue").pack()
		pesan = Entry(cek).pack()
		cetak = Button(cek, text = "Kirim", command = self.terkirim).pack()
		Button(cek, text="Keluar", command=cek.quit).pack(anchor=S, pady=15, padx=5)

		self.nama = "M Zul Khabani"
		self.gender = "Pria"
		self.umur = "20"
		self.alamat = "Korea Utara"

		self.nama1 = "Sela Banzira"
		self.gender1 = "Wanita"
		self.umur1 = "20"
		self.alamat1 = "Zimbabwe"

		self.nama2 = "Rachel Marta"
		self.gender2 = "Wanita"
		self.umur2 = "20"
		self.alamat2 = "Indonesia"

	def terkirim(self):
		labelterkirim = Label(cek, text= "Terkirim!", fg = "red").pack(pady = 10)


cek = Tk()
cek.title("Kelompok Berapa Ya Lupa")
GengUburUbur()
cek.mainloop()