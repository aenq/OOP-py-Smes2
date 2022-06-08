list1 = ['UNJANI', 'Sistem Informasi', 2019, 2018]
list2 = [4, 1, 2, 5, 3]
list3 = ["a", "b", "c", "d"]
print("List 1: ",list1)
print("List 2: ",list2)
print("List 3: ",list3)

# perintah mengurutkan list 2
list2.sort()

# perintah menambahkan elemen list 3
list3.append("e")

# menghapus elemen dari list 1
list1.remove(2019)

print("Panjang List 1: ", len(list1))
print("Nilai terbesar pada List 2: ", max(list2))
print("Mengurutkan List 2: ", list2)
print("Menambahkan elemen pada List 3: ", list3)
print("Menghapus elemen pada List 1: ", list1)

print()
print("=====MAPPING=====")
print()

d_nilai = {
'andi':'A',
'budi':'B',
'citra':'C',
'hendra':'A',
'baron':'D'}

print("daftar nilai: ",d_nilai)
# mengecek panjang dictionary
print("panjang dictionary: ",len(d_nilai),"\n")
# merubah entry yang sudah ada
d_nilai['citra']='B'
print("perubahan 1: ",d_nilai)
# menambah entry baru
d_nilai['tony']='A'
print("perubahan 2: ",d_nilai)
# mengecek panjang dictionary

print("panjang dictionary: ",len(d_nilai),"\n")
# menghapus entry
del d_nilai['citra']
print("perubahan 3: ",d_nilai)
print("panjang dictionary: ",len(d_nilai),"\n")
# mengosongkan dictionary
d_nilai.clear()
print("perubahan 4: ",d_nilai)
print("panjang dictionary: ",len(d_nilai),"\n")




print()
print("=====SET=====")
print()

# set data campuran 
data = {1, 2.0, "jarvis", (3,4,5)} 
print('Set gabungan: ',data) 
# bila kita mengisi duplikasi, set akan menghilangkan salah satu
# output: {1,2,3} 
angka = {1,2,2,3,3,3} 
print('Set angka:',angka) 
# set tidak bisa berisi anggota list 
# contoh berikut akan muncul error TypeError 
# set_baru = {1,2,[3,4,5]} 
# supaya bisa program bisa jalan, baris diatas dikomen atau dihapus
# menambah anggota baru pada set angka
angka.add(4) 
print('Set angka perubahan 1:',angka)
# menambah beberapa anggota sekaligus
angka.update([3,4,5,6]) 
print('Set angka perubahan 2:',angka)
# mengosongkan set
angka.clear()
print('Set angka perubahan 3:',angka)



print()
print("=====SET HIMPUNAN=====")
print()

# Membuat set A and B 
A = {1, 2, 3, 4, 5} 
B = {4, 5, 6, 7, 8} 
print('A:',A)
print('B:',B)
# Gabungan menggunakan operator | 
print('A gabung B: ',(A | B))
# Irisan menggunakan operator &
print('A irisan B: ',(A & B))
# operasi selisih
print('A - B: ',(A - B))
# operasi komplemen
print('A komplemen B: ',(A ^ B))


print()
print("=====HERO=====")
print()

class Hero(object):
 """__init__() functions as the class constructor"""
 def __init__(self, nama=None, alias=None, kelompok=None):
	 self.nama = nama
	 self.alias = alias
	 self.kelompok = kelompok
 
listHero = []
listHero.append(Hero("Anthony Edward Stark","Iron Man","Avengers"))
listHero.append(Hero("Peter Jason Quill","Star-Lord","Guardians of Galaxy"))
listHero.append(Hero("Barry Allen","The Flash","Justice League"))
listHero.append(Hero("Thor Odinson","God of Thunder","Avengers"))
listHero.append(Hero("Bruce Wayne","Batman","Justice League"))
print ("Hero pertama:", listHero[0].nama,"\n")
print("Daftar superhero:")
for Hero in listHero:
	print("Nama: {}\nAlias: {}\nKelompok: {}\n".format(Hero.nama, Hero.alias, Hero.kelompok))

print()
print("===== Latihan No 1 =====")
print()

class Hero(object):
 	"""init() functions as the class constructor"""
 	def _init_(self, nama=None, alias=None, kelompok=None):
 		self.nama = nama
 		self.alias = alias
 		self.kelompok = kelompok

listHero = []
hero = True
while hero :
	listHero.append(Hero(input("Nama Hero :"), input("Alias Hero: "), input("Kelompok Hero:")))
	a = input("Lagi? (y/n):")
	if a == "n":
		hero = False

print()
print("SUPER HERO", listHero[0].nama,"\n")
for Hero in listHero :
	print(" Nama: {}\n Alias: {}\n Kelompok: {}\n\n".format(
		Hero.nama, Hero.alias, Hero.kelompok))
		