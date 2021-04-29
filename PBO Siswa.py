# PBO Siswa Basic 
class siswa: 
    #class variable 
    jumlah_siswa = 0 
    #konstruktor 
    def __init__(self, nama, kelas, alamat, nilai): 
        self.nama = nama 
        self.kelas = kelas 
        self.alamat = alamat 
        self.nilai = nilai 
        siswa.jumlah_siswa += 1 
    #methode 
    def viewSiswa(self): 
        print("----------------------")
        print("Data Siswa")
        print("Nama  :", self.nama)
        print("Kelas :", self.kelas)
        print("Alamat:", self.alamat) 
        print("----------------------")

    def viewNilai(self):
        print("Data Nilai")
        print("Nama   :", self.nama)
        for nilai in self.nilai:
            print("Nilai  :", nilai)
        print("---------------------")

    def viewketerangan(self):
        print("Keterangan")
        print("Nama  :", self.nama)
        print("Kelas  :", self.kelas)
        rata = sum(self.nilai)/len(self.nilai)
        print("Rata-rata  : ", rata)
        if rata >= 75: 
            keterangan = "Lulus."
        else: 
            keterangan = "Tidak lulus."
        print("Keterangan  :", keterangan)
        print("---------------------")
    
#intansiasi objek 
siswa1 = siswa("Ani", "XI MIPA 5", "Yogyakarta", [90,81,80,40])
siswa2 = siswa("Arkan", "XI MIPA 5", "Sleman", [70,45,85,65])
#pemanggilan objek siswa 1 
siswa1.viewSiswa()
siswa1.viewNilai()
siswa1.viewketerangan()
print("Jumlah siswa: ", siswa.jumlah_siswa)
#pemanggilan objek siswa 2 
siswa2.viewSiswa()
siswa2.viewNilai()
siswa2.viewketerangan()
print("Jumlah siswa : ", siswa.jumlah_siswa)