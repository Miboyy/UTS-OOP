class AkunBank:
    def _init_(self, nomor_rekening, saldo):
        self.nomor_rekening = nomor_rekening
        self._saldo = saldo  # Atribut privat

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, nilai):
        if nilai < 0:
            print("Saldo tidak boleh negatif.")
        else:
            self._saldo = nilai

    def tambah_saldo(self, jumlah):
        if jumlah > 0:
            self._saldo += jumlah
            print(f"Saldo berhasil ditambahkan. Saldo saat ini: {self._saldo}")
        else:
            print("Jumlah harus positif.")

    def tarik_saldo(self, jumlah):
        if 0 < jumlah <= self._saldo:
            self._saldo -= jumlah
            print(f"Saldo berhasil ditarik. Saldo saat ini: {self._saldo}")
        else:
            print("Jumlah tidak valid atau saldo tidak mencukupi.")

# Contoh Penggunaan
akun = AkunBank("12345678", 1000.0)
print("Saldo awal:", akun.get_saldo())
akun.set_saldo(1200.0)
akun.tambah_saldo(500.0)
akun.tarik_saldo(300.0)