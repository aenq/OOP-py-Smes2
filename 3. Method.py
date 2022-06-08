print("=== Method ===")

""" Method ada 2,
1. Method interaktif dengan klien, contoh klien bilang Hero untuk bergerak, makan hero bergerak
2. method interaksi antar objek, contoh Hero attack Hero lain, ini interaksi antar objek, tp klien juga """

class Hero:
	# class variable
	Jumlah_hero =0
	def __init__(self, inputName, inputHealth, inputPower, inputArmor):
		# instance variable
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputArmor
		Hero.Jumlah_hero += 1

	# method tanpa return, void function
	def siapa(self):
		print("Namaku adalah " + self.name)

	# method dengan argumen
	def healthUp(self, nilai):
		self.health += nilai

	# method dengan return
	def getHealth(self):
		return self.health

hero1 = Hero("Sniper", 100, 10, 5)
hero2 = Hero("Mario bross", 90, 5, 10)

print(hero1.__dict__)
print(hero2.__dict__)

#tanpa return
hero1.siapa()

#dengan argumen
hero1.healthUp(30)
print(hero1.health)

#dengan return
print(hero1.getHealth())

print()
print(100*"=")
print("====coba bikin sendiri===")

class Perumahan():

	def __init__(self,inputName, inputKamar, inputTv, inputMobil, inputMotor):
		self.name = inputName
		self.kamar = inputKamar
		self.tv = inputTv
		self.mobil = inputMobil
		self.motor = inputMotor

	#method tanpa return
	def rumahsiapa(self):
		print("ini rumah siapa ya? " + self.name)
	#method dengan argumen
	def kamarUp(self, up):
		self.kamar += up

Rumah1 = Perumahan("rachel", 2, "LG", "Volvo", "Scoopy")
print(Rumah1.__dict__)

Rumah1.rumahsiapa()
Rumah1.kamarUp(10)
print(Rumah1.kamar)



print("="*100)
print("/// Nomor 1 ///")

class mahasiswa: # ini adalah  nama kelasnya
	print("dasar kelas untuk semua mahasiswa")
	jmlMhs = 0 # ini adalah class variable, menunjukkan jml mahasiswa dimulai dari 0
	def __init__ (self, nama, prodi): # ini adalah instance
		#ini adalah variable instance
		self.nama = nama
		self.prodi = prodi
		mahasiswa.jmlMhs += 1 #di gunakan untuk menghitung pertambahan jml mahasiswa pada asaat tersebut

	def tampilJml(self): # method tanpa return
		print("Total Mahasiswa: ", mahasiswa.jmlMhs) #mengecek total mahasiswa saat perhitungan tsb

	def tampilProfil(self): # method tanpa return
		print("Nama : ", self.nama) 
		print("Nama : ", self.prodi)
		print()

# ini adalah oject
mhs1 = mahasiswa("Adi",'Teknik Informatika') # object 1
mhs2 = mahasiswa("Budi",'Matematika') # object 2
mhs1.tampilProfil() #menampilkan profil dari object pertama yaitu mhs1 yg bernama Adi
mhs2.tampilProfil() #menampilkan profil dari object kedua yaitu mhs2 yg bernama Budi



print("/// No 2 ///")
###### TUGAS !!!! ######
""" Buatlah sebuah kelas baru bernama buku dan definisikan atribut-atribut yang dimiliki oleh 
sebuah buku. Setelah itu buatlah instance dari buku dan buatlah perintah untuk mengecek 
apakah instance tersebut merupakan bagian dari kelas buku! """

class Book():
	jmlbuku_perpus = 0
	def __init__(self, name, cover, keteranganbuku, daftarisi, chapter, daftarpustaka):
		self.name = name
		self.cover = cover
		self.keteranganbuku = keteranganbuku
		self.daftarisi = daftarisi
		self.chapter = chapter
		self.daftarpustaka = daftarpustaka

Book1 = Book("Dilan", "Cover", "Karya Pidi Baiq", "Daftar Isi", 30, "Daftar Pustaka")
print(Book1.__dict__)

class Book():
	pass

daftarisi = Book()
print("Apakah daftarisi bagian dari sebuah Book?", isinstance(daftarisi, Book))