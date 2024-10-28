class Karyawan:
    def __init__(self, nama, umur, gaji):
        self.nama = nama
        self.umur = umur
        self.gaji = gaji

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur}, Gaji: {self.gaji}"


class Manajer(Karyawan):
    def __init__(self, nama, umur, gaji, departemen):
        super().__init__(nama, umur, gaji)
        self.departemen = departemen

    def info(self):
        return f"{super().info()}, Departemen: {self.departemen}"


class Staf(Karyawan):
    def __init__(self, nama, umur, gaji, shift):
        super().__init__(nama, umur, gaji)
        self.shift = shift

karyawan_umum = Karyawan("Dairot", 30, 5000000)
manajer = Manajer("Saber Roam", 45, 10000000, "Keuangan")
staf = Staf("Zilong", 25, 4000000, "Malam")

print(karyawan_umum.info())
print(manajer.info())
print(staf.info())
