class Karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.jumlah_karyawan += 1
    def tampilkan_jumlah(self):
        print("Total karyawan", Karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)

#membuat objek pertama dari kelas karyawan 
karyawan1 = Karyawan("Sarah", 1000000)
#membuat objek kedua dari kelas karyawan
karyawan2 = Karyawan("Budi", 2000000)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
print("Total karyawan :", Karyawan.jumlah_karyawan)