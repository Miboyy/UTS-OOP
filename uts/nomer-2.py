class Mahasiswa:
    def _init_(self, nama, nim, programStudi):
        self.nama = nama
        self.nim = nim
        self.programStudi = programStudi

    def tampilkanInfo(self):
        print(f"Nama: {self.nama}\nNIM: {self.nim}\nProgram Studi: {self.programStudi}")

# Input data
nama = input("Nama: ")
nim = input("NIM: ")
programStudi = input("Program Studi: ")

# Membuat objek
mahasiswa1 = Mahasiswa(nama, nim, programStudi)
mahasiswa1.tampilkanInfo()