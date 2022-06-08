class mahasiswa:
	jml_mhs = 0
	
	def __init__ (self, nama, jurusan, npm, j_kelamin):
		self.nama = nama
		self.jurusan = jurusan
		self.npm = npm
		self.j_kelamin = j_kelamin
		

		mahasiswa.jml_mhs += 1

	def tampilJml(self):
		print("Total Mahasiswa: ", mahasiswa.jml_mhs)

	def tampilProfil(self):
		print("Nama: ", self.nama)
		print("Jurusan: ", self.jurusan)
		print("NPM: ", self.npm)
		print("Jenis Kelamin:", self.j_kelamin)
		print()

maha1 = mahasiswa("Rachel Marta Maria", "S1 Sistem informasi", 202103015, "Perempuan")
maha1.tampilProfil()
print(maha1.__dict__)

print(delattr(maha1, "nama"))
print(hasattr(maha1, "nama"))

# Cek atribut


print()

print(hasattr(maha1,"Nama"))
print(hasattr(maha1,"Jurusan"))
print(hasattr(maha1,"Nim"))
print(hasattr(maha1,"Jenis_Kelamin"))

print("c")
print(getattr(maha1,"j_kelamin"))

print("d")
print(delattr(maha1,"j_kelamin"))