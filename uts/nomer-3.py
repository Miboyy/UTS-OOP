class Laptop:
    def _init_(self, merk, ram, processor):
        self.merk = merk
        self.ram = ram  # GB
        self.processor = processor
        print(f"Laptop {self.merk} ({self.ram}GB, {self.processor}) dibuat.")

    def _del_(self):
        print(f"Laptop {self.merk} dihancurkan.")

# Contoh penggunaan
laptop1 = Laptop("Dell", 16, "Intel i7")
del laptop1  # Menghapus objek secara eksplisit
