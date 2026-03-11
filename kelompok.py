# Mengimpor modul ABC untuk membuat Abstract Class
from abc import ABC, abstractmethod


# ======================================================
# ABSTRACT CLASS (ABSTRACTION)
# ======================================================
# Class ini menjadi kerangka dasar.
# Tidak boleh dibuat objek langsung.
class BarangElektronik(ABC):

    def __init__(self, nama, stok, harga_dasar):
        # ENCAPSULATION (data dibuat private dengan __)
        self.__nama = nama
        self.__stok = stok
        self.__harga_dasar = harga_dasar

    # ========================
    # GETTER (untuk membaca data private)
    # ========================
    def get_nama(self):
        return self.__nama

    def get_stok(self):
        return self.__stok

    def get_harga_dasar(self):
        return self.__harga_dasar

    # ========================
    # SETTER dengan validasi
    # ========================
    # Method ini untuk menambah stok
    # Stok tidak boleh negatif
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.__nama}: Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.__nama}: {self.__stok} unit.")

    # ========================
    # ABSTRACT METHOD
    # ========================
    # Method ini WAJIB dioverride oleh class turunan
    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


# ======================================================
# CLASS LAPTOP (INHERITANCE)
# ======================================================
# Laptop mewarisi BarangElektronik
class Laptop(BarangElektronik):

    def __init__(self, nama, stok, harga_dasar, processor):
        # Memanggil constructor parent
        super().__init__(nama, stok, harga_dasar)
        self.processor = processor  # atribut tambahan khusus Laptop

    # POLYMORPHISM
    # Method sama dengan parent, tapi implementasi berbeda
    def tampilkan_detail(self):
        print(f"[LAPTOP] {self.get_nama()} | Proc: {self.processor}")

    # Pajak Laptop = 10%
    def hitung_harga_total(self, jumlah):
        pajak = 0.10 * self.get_harga_dasar()
        subtotal = (self.get_harga_dasar() + pajak) * jumlah

        print(f"Harga Dasar: Rp {self.get_harga_dasar():,} | Pajak(10%): Rp {pajak:,.0f}")
        print(f"Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}")

        return subtotal


# ======================================================
# CLASS SMARTPHONE (INHERITANCE)
# ======================================================
# Smartphone juga mewarisi BarangElektronik
class Smartphone(BarangElektronik):

    def __init__(self, nama, stok, harga_dasar, kamera):
        super().__init__(nama, stok, harga_dasar)
        self.kamera = kamera  # atribut tambahan khusus Smartphone

    # POLYMORPHISM
    # Implementasi berbeda dari Laptop
    def tampilkan_detail(self):
        print(f"[SMARTPHONE] {self.get_nama()} | Cam: {self.kamera}")

    # Pajak Smartphone = 5%
    def hitung_harga_total(self, jumlah):
        pajak = 0.05 * self.get_harga_dasar()
        subtotal = (self.get_harga_dasar() + pajak) * jumlah

        print(f"Harga Dasar: Rp {self.get_harga_dasar():,} | Pajak(5%): Rp {pajak:,.0f}")
        print(f"Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}")

        return subtotal


# ======================================================
# FUNGSI DI LUAR CLASS (FITUR KERANJANG BELANJA)
# ======================================================
# Fungsi ini menerima list berisi objek Laptop dan Smartphone
# Ini contoh POLYMORPHISM karena memanggil method yang sama
# tapi hasilnya berbeda tergantung objeknya
def proses_transaksi(daftar_belanja):

    print("\n--- STRUK TRANSAKSI ---")
    total = 0
    no = 1

    for barang, jumlah in daftar_belanja:
        print(f"{no}. ", end="")
        barang.tampilkan_detail()  # method dipanggil sesuai tipe objek
        total += barang.hitung_harga_total(jumlah)
        print()
        no += 1

    print("-" * 35)
    print(f"TOTAL TAGIHAN: Rp {total:,.0f}")
    print("-" * 35)


# ======================================================
# MAIN PROGRAM (USER STORY)
# ======================================================
print("--- SETUP DATA ---")

# Membuat 1 Laptop dan 1 Smartphone
laptop1 = Laptop("ROG Zephyrus", 10, 20000000, "Ryzen 9")
hp1 = Smartphone("iPhone 13", 15, 15000000, "12MP")

# Mencoba input stok negatif (harus ditolak)
hp1.tambah_stok(-5)

# Update stok yang benar
hp1.tambah_stok(5)

# User membeli 2 Laptop dan 1 Smartphone
keranjang = [
    (laptop1, 2),
    (hp1, 1)
]

# Memproses transaksi
proses_transaksi(keranjang)