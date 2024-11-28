class Hewan:
    def suara(self):
        return "Hewan mengeluarkan suara."

class Kucing(Hewan):
    def suara(self):
        return "Meong!"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk!"

# Contoh penggunaan
print(Hewan().suara())   
print(Kucing().suara()) 
print(Anjing().suara()) 