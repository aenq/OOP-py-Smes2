# NO 2

class Indonesia():
    def ibukota(self):
        print("DKI Jakarta adalah ibukota negara Indonesia")

    def bahasa(self):
        print("Bahasa Indonesia merupakan bahasa Nasional")

    def suku_asli(self):
        print("Suku asli atau Pribumi Indonesia adalah Jawa")



class USA():
    def ibukota(self):
        print("Washington DC adalah ibukota negara Amerka Serikat")

    def bahasa(self):
        print("Bahasa Inggris merupakan bahasa utama yang digunakan di Amerika Serikat")

    def suku_asli(self):
        print("Suku asli Amerika adalah SUku Indian")

ina = Indonesia()
usa = USA()

for country in (ina, usa):
    country.ibukota()
    country.bahasa()
    country.suku_asli()
    print()

# NO 3



class Bird():
    def intro(self):
        print("Ada banyak jenis burung")

    def flight(self):
        print("Sebagian besar burung bisa terbang, sebagian lagi tidak")

class sparrow(Bird):
    def flight(self):
        print("Burung gereja bisa terbang")

class ostrich(Bird):
    def flight(self):
        print("Burung unta tidak bisa terbang")

Burung = Bird()
sparrow = sparrow()
ostrich = ostrich()

print()
Burung.intro()
Burung.flight()
print()
sparrow.flight()
print()
ostrich.flight()

# NO 8

import tkinter

rachel = tkinter.Tk()

mantap = tkinter.Label(rachel, text = "Python mantap sekali bah!!!")
mantap.pack()

rachel.mainloop()

# No 11

class Nilai(object):
    def __init__(self, nama= None, matakuliah = None, NilaiMahasiswa = None):
        self.nama = nama
        self.matakuliah = matakuliah
        self.NilaiMahasiswa = NilaiMahasiswa
        
# membuat list dg nama listNilai
print("=====Nilai=====")
print()

class Nilai(object):
    def __init__(self, nama=None, matakuliah=None, nilaimatkul=None):
        self.nama = nama
        self.matakuliah = matakuliah
        self.nilaimatkul = nilaimatkul
 
listNilai = []
listNilai.append(Nilai("Lala", "PBO", "B"))
listNilai.append(Nilai("Ani", "PBO", "A"))
listNilai.append(Nilai("Edo", "PBD", "C"))
listNilai.append(Nilai("Willy", "Kalkulus", "B"))
listNilai.append(Nilai("Ani", "Kalkulus", "B"))
print ("Nilai pertama:", listNilai[0].nama,"\n")
print("Daftar superNilai:")
for Nilai in listNilai:
    print("Nama: {}\nMatakuliah: {}\nNilaimatkul: {}\n".format(Nilai.nama, Nilai.matakuliah, Nilai.nilaimatkul))