class Pegawai:

    def __init__(self, id, nama):

        self.id = id

        self.nama = nama


class SistemGaji:

    def hitung_gaji(self, pegawai):

        print('Hitung Gaji')

        print('===================')

        for employee in pegawai:

            print('Gaji untuk: {employee.id} - {employee.nama}')

            print('- Besaran: {employee.hitung_gaji()}')

            print('')

class GajiMingguan(Pegawai):

    def __init__(self, id, nama, gaji_mingguan):

        super().__init__(id, nama)

        self.gaji_mingguan= gaji_mingguan



    def hitung_gaji(self):

        return self.gaji_mingguan


class GajiSales(GajiMingguan):

    def __init__(self, id, nama, gaji_mingguan, komisi):

        super().__init__(id, nama, gaji_mingguan)

        self.komisi = komisi



    def hitung_gaji(self):

        fixed = super().hitung_gaji()

        return fixed + self.komisi



class UpahPerJam(Pegawai):

    def __init__(self, id, nama, jam_kerja, tarif):

        super().__init__(id, nama)

        self.jam_kerja= jam_kerja

        self.tarif = tarif



    def hitung_gaji(self):

        return self.jam_kerja * self.tarif


gaji_mingguan = UpahPerJam(2, 'Mark', 40, 15)

komisi_pegawai = GajiSales(3, 'Jackson', 1000, 250)

sistem_gaji = SistemGaji()

sistem_gaji.hitung_gaji([