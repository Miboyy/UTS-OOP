class Laptop:
    def __init__(self, merk, ram, processor):  # Perbaikan pada nama konstruktor
        self.merk = merk
        self.ram = ram  # GB
        self.processor = processor
        print(f"Laptop {self.merk} ({self.ram}GB, {self.processor}) dibuat.")

    def __del__(self):  # Perbaikan pada nama destruktor
        print(f"Laptop {self.merk} dihancurkan.")

# Contoh penggunaan
laptop1 = Laptop("Dell", 16, "Intel i7")
del laptop1  # Menghapus objek secara eksplisit
