class Buku:
    def __init__(self, judul, tahun, jumlah_halaman, bahan_material, diskon):
        self._judul = judul
        self._tahun = tahun
        self._jumlah_halaman = jumlah_halaman
        self._bahan_material = bahan_material
        self._diskon = diskon

    def get_judul(self):
        return self._judul

    def get_tahun(self):
        return self._tahun

    def get_jumlah_halaman(self):
        return self._jumlah_halaman

    def get_bahan_material(self):
        return self._bahan_material

    def get_diskon(self):
        return self._diskon

    def set_diskon(self, diskon):
        self._diskon = diskon

    def cek_harga(self):
        if self._tahun <= 5 and self._jumlah_halaman <= 100:
            harga = 300000
        elif 5 <= self._tahun <= 10 and self._jumlah_halaman <= 100:
            harga = 50000
        elif 5 <= self._tahun <= 10 and self._jumlah_halaman >= 500:
            harga = 250000
        elif 5 <= self._tahun <= 10 and 100 <= self._jumlah_halaman <= 500:
            harga = 15000
        else:
            harga = 1000

        harga -= harga * self._diskon / 100
        return harga


class Komik(Buku):
    def __init__(self, judul, tahun, jumlah_halaman, bahan_material, diskon, is_colorful):
        super().__init__(judul, tahun, jumlah_halaman, bahan_material, diskon)
        self._is_colorful = is_colorful

    @classmethod
    def create_buku(cls, judul, tahun, jumlah_halaman, bahan_material, diskon, is_colorful):
        return cls(judul, tahun, jumlah_halaman, bahan_material, diskon, is_colorful)

    def get_is_colorful(self):
        return self._is_colorful


# Contoh penggunaan
buku = Buku("Calculus", 2024, 1000, "Kertas", 0)
print("Judul buku:", buku.get_judul())

komik = Komik.create_buku("One Piece", 1998, 500, "Kertas", 0, True)
print("Judul komik:", komik.get_judul())
