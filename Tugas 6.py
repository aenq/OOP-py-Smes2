class Person:
	#atribut
	#self.nama
	#self.tempat_lahir
	#self.tanggal_lahir
	#self.jenisKelamin
	#self.nik
	#self.tinggiBadan
	#self.beratBadan
	#self.golonganDarah
	#self.alamat
	def inputDataPerson(self):
		self.nama = str(input("Nama :"))
		self.tempat_lahir = str(input("Tempat Lahir :"))
		self.tanggal_lahir = str(input("Tanggal Lahir :"))
		self.jenisKelamin = str(input("Jenis Kelamin :"))
		self.nik = str(input("NIK :"))
		self.tinggiBadan =  int(input("Tinggi Badan :"))
		self.beratBadan = int(input("Berat Badan :"))
		self.golonganDarah = str(input("Golongan Darah :"))
		self.alamat = str(input("Alamat :"))

	def tampilDataPerson():
		print("Nama :", self.nama)
		print("Tempat Lahir :",self.tempat_lahir)
		print("Tanggal Lahir :",self.tanggal_lahir)
		print("Jenis Kelamin :",self.jenisKelamin)
		print("NIK :",self.nik)
		print("Tinggi Badan :",self.tinggiBadan,"cm")
		print("Berat Badan :",self.beratBadan,"kg")
		print("Golongan Darah :",self.golonganDarah)
		print("Alamat :",self.alamat)

class Employee(Person):
	#atribut
	#self.id_employee
	#self.pekerjaan
	#self.gaji
	#self.tahun_masuk
	#self.status

	def inputDataEmployee(self):
		Person.inputDataPerson(self)
		self.id_employee = str(input("ID Employee :"))
		self.pekerjaan = str(input("ID Pekerjaan :"))
		self.gaji = int(input("Gaji :"))
		self.tahun_masuk = int(input("Tahun Masuk :"))
		self.status = str(input("Status :"))

	def tampilDataEmployee(self):
		print("Nama :",self.nama)
		print("Tempat Lahir :",self.tempat_lahir)
		print("Tanggal Lahir :",self.tanggal_lahir)
		print("Jenis Kelamin :",self.jenisKelamin)
		print("NIK :",self.nik)
		print("Tinggi Badan :",self.tinggiBadan,"cm")
		print("Berat Badan :",self.beratBadan,"kg")
		print("Golongan Darah :",self.golonganDarah)
		print("Alamat :",self.alamat)
		print("ID Employee :",self.id_employee)
		print("Pekerjaan :",self.pekerjaan)
		print("Gaji :","Rp.",self.gaji)
		print("Tahun Masuk :",self.tahun_masuk)
		print("Status :", self.status)

	def hitungMasaKerja(self,tahun_masuk):
		self.tahunSekarang = int(input("Tahun sekarang :"))
		lama = self.tahunSekarang - self.tahun_masuk
		print("Masa Kerja :", lama, "Tahun")

class Customer(Person):
	#atribut
	#self.id_cutomer
	#self.poin
	def inputDataCustomer(self):
		Person.inputDataPerson(self)
		self.id_customer = str(input("ID Customer :"))
		self.poin = int(input("Poin :"))

	def tampilDataCustomer(self):
		print("Nama :",self.nama)
		print("Tempat Lahir :",self.tempat_lahir)
		print("Tanggal Lahir :",self.tanggal_lahir)
		print("Jenis Kelamin :",self.jenisKelamin)
		print("NIK :",self.nik)
		print("Tinggi Badan :",self.tinggiBadan,"cm")
		print("Berat Badan :",self.beratBadan,"kg")
		print("Golongan Darah :",self.golonganDarah)
		print("Alamat :",self.alamat)
		print("ID Customer :",self.id_customer)
		print("Poin :",self.poin)

	def tambahPoin(self,poin):
		self.tambahPoin = int(input("Tambah Poin :"))
		totalPoin = self.tambahPoin + self.poin
		print("Total Poin :", totalPoin, "Poin")
		
a = Employee()
a.inputDataEmployee()
a.tampilDataEmployee()
a.hitungMasaKerja('tahun_masuk')
b = Customer()
b.inputDataCustomer()
b.tambahPoin('poin')
b.tampilDataCustomer()