# script no 2
class Computer:
	def __init__(self):
		self.__prosesor = 'Intel Core i7-6700K'
		self.__memory = '16GB DDR4'
		self.os = 'Windows 10 Pro'
		self.keyboard = 'Razer'
		self.mouse = 'Logitech'
		print(self.__prosesor)

	def tampilData(self):
		print("Prosesor 	: ", self.__prosesor)
		print("Memory 		: ", self.__memory)
		print("OS 			: ", self.os)
		print("Keyboard 	: ", self.keyboard)
		print("Mouse 		: ", self.mouse)
	def setProsesor(self,Prosesor):
		self.__prosesor = Prosesor
	def setMemory(self,Memory):
		self.__memory = Memory

print("===Sebelum===")
comput1 = Computer()
comput1.tampilData()

print()
print("===Setelah===")
comput1.setProsesor("Intel Core i3-8130U")
comput1.setMemory("4GB, HDD 1TB")
setattr(comput1, "os", "Windows 10")
setattr(comput1, "keyboard", "KEYBOARD")
setattr(comput1, "mouse", "Prolink")
comput1.tampilData()

print(100*"=")
print()
print("Nomor 3")
print()
class mahasiswa:
	def __init__ (self):
		self.__nama = "Rachel Marta Maria"
		self.__jurusan = "Sistem Informasi"
		self.__npm = "202103015"
		self.__j_kelamin = "Perempuan"
		self.__hobby = "Belajar"
	def tampilProfil(self):
		print("Nama 			: ", self.__nama)
		print("Jurusan 		: ", self.__jurusan)
		print("NPM 			: ", self.__npm)
		print("Jenis Kelamin 	: ", self.__j_kelamin)
		print("Hobby 			: ", self.__hobby)
		print()
#Private
	def getProfile(self, nama, jurusan, npm, j_kelamin, hobby):
		self.__nama = nama
		self.__jurusan = jurusan
		self.__npm = npm
		self.__j_kelamin = j_kelamin
		self.__hobby = hobby

print("===Sebelum===")
profil1 = mahasiswa()
profil1.tampilProfil()

print("===Sesudah===")
profil1.getProfile("Aeng", "SI", "015", "P", "Mancing Keributan")
profil1.tampilProfil()


print()
print("Nomer 4")
print()

# script nomor 4
class computer :
	def __init__ (self):
		self.__procesor = None
		self.__memory = None
		self.os = None
		self.keyboard = None
		self.mouse = None

	def __setPros (self,newPros):
		self.__procesor = newPros
	def __setMemo (self, newMemo):
		self.__memory = newMemo

	def tampilData (self):
		print('Procesor 	:',self.__procesor)
		print('Memory 		:',self.__memory)
		print('os			:',self.os)
		print('Keyboard 	:',self.keyboard)
		print('Mouse 		:',self.mouse)
		print()

print("===Modify===")
class modify :
	pc= computer()
	pc.tampilData()

	newPros = input("Prosesor 	:")
	newMemo = input("Memory 	:")

#No 6
	pc._computer__setPros(newPro)
	pc._computer__setMemo(newMem)
	pc.tampilData()