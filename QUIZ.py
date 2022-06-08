print("RACHEL MARTA MARIA")
print("202103015")
print()
print("No 1")
class Pelanggan:

	def __init__(self, id_pelanggan, nama, alamat):
		self.id = id_pelanggan
		self.nama = nama
		self.alamat = alamat

	def tambahPelanggan(self):
		print("Pelanggan baru telah ditambahkan dengan profil: \n\t",
		"ID: {}, NAMA: {}, ALAMAT: {}".format(self.id,self.nama, self.alamat))

	def getNamaPelanggan(self):
		return self.nama

rachel = Pelanggan(15, "rachel", "bogor")
print(rachel.__dict__)
diki = Pelanggan(1, "diki", "hongkong")
print(diki.tambahPelanggan())
print("Nama pelanggan :", rachel.getNamaPelanggan())


print()
print("No 2")

class Motor:
	#produsen
	def __init__(self, produsen):
		self.produsen = produsen
	def getProdusen(self):
		print("Produsen motor tersebut :" )
		return self.produsen

class Matic(Motor):
	def __init__(self, tipe):
		self.tipe = tipe
	def getTipe(self):
		print("Tipe motor tersebut :")
		return self.tipe

Motor1 = Motor("Honda")
print(Motor1.getProdusen())
Motor1 = Matic("Matic")
print(Motor1.getTipe())






print()
print("NO 3")

class Pendaftaran:

	def pendaftaranService(self, produsen ,tipe, nama):
		self.produsen = produsen
		self.tipe = tipe
		self.nama = nama

	def lihatDataPendaftar(self):
		print("Produsen :", self.produsen)
		print("Tipe :", self.tipe)
		print("Nama Pelanggan :", self.nama)

print()
Pendaftar1 = Pendaftaran()
Pendaftar1.pendaftaranService("Honda", "Motor" ,"Rachel")
Pendaftar1.lihatDataPendaftar()







print()

print("NOMOR 4")

class Motor():
	def setProdusen(self):
		self.id_produsen = input('ID Produsen: ')
		self.jenis_kelamin = input('Jenis Kelamin: ')
		self.alamat = input('Alamat: ')

	def getProdusen(self):
		print('ID Produsen:', self.id_produsen)
		print('Jenis Kelamin:',self.jenis_kelamin)
		print('Alamat:', self.alamat)

#anak
class Matic(Motor):
	def setTipe(self):
		Motor.setProdusen(self)
		self.merk = str(input('Merek:'))
		self.warna = str(input('Warna:'))

	def getTipe(self):
		print('ID Produsen:', self.id_produsen)
		print('Jenis Kelamin:',self.jenis_kelamin)
		print('Alamat:', self.alamat)
		print('Merek:', self.merk)
		print('Warna:', self.warna)

MotorMberrr = Matic()
MotorMberrr.setProdusen()
MotorMberrr.getProdusen()
MotorMberrr.setTipe()
MotorMberrr.getTipe()



