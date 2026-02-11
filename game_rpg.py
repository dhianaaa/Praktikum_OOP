
# GAME RPG SEDERHANA BERBASIS OOP - PYTHON
# Menggabungkan Tugas Analisis 1 sampai 6
# Materi: Class, Object, Inheritance, Encapsulation,
#          Abstraction, Interface, Polymorphism

# TUGAS 1 & 2
# CLASS HERO + ATRIBUT + INTERAKSI OBJEK

class Hero:
    def __init__(self, name, hp, attack_power):
        # Attribute public (masih bisa diakses bebas)
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    # Method untuk menampilkan info hero
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

    # Method menyerang hero lain
    def serang(self, lawan):
        # lawan berupa OBJEK Hero lain, bukan sekadar string
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    # Method menerima serangan
    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")


# TUGAS 3
# INHERITANCE (PEWARISAN) - CLASS MAGE TURUNAN HERO

class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        # super() memanggil constructor Hero
        # agar name, hp, dan attack_power tetap terbentuk
        super().__init__(name, hp, attack_power)
        self.mana = mana

    # Override method info
    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    # Skill khusus Mage
    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)  # Damage 2x lipat
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")


# TUGAS 4
# ENKAPSULASI - MELINDUNGI DATA HP

class SecureHero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal  # Private Attribute

    # GETTER: untuk melihat HP secara aman
    def get_hp(self):
        return self.__hp

    # SETTER: untuk mengubah HP dengan validasi
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0  # HP tidak boleh negatif
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    # Method menerima serangan dengan sistem aman
    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# TUGAS 5
# ABSTRACTION & INTERFACE DENGAN ABC

from abc import ABC, abstractmethod

class GameUnit(ABC):
    # Kontrak: Semua turunan wajib punya method ini

    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


class HeroUnit(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


# TUGAS 6
# POLYMORPHISM - SATU METHOD, BEDA PERILAKU

class PolyHero:
    def __init__(self, nama):
        self.nama = nama

    def serang(self):
        print("Hero menyerang dengan tangan kosong.")


class PolyMage(PolyHero):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")


class Archer(PolyHero):
    def serang(self):
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")


class Fighter(PolyHero):
    def serang(self):
        print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")


class Healer(PolyHero):
    def serang(self):
        print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!")


# MAIN PROGRAM (PENGUJIAN SEMUA TUGAS)

print("\n TUGAS 1: UBAH ATRIBUT HP ")
hero1 = Hero("Layla", 100, 15)
hero1.hp = 500  # Karena public, bisa diubah bebas
print(hero1.hp)

print("\n TUGAS 2: INTERAKSI OBJEK ")
hero2 = Hero("Zilong", 120, 20)
hero1.serang(hero2)
hero2.serang(hero1)

print("\n TUGAS 3: INHERITANCE ")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)
eudora.info()
eudora.serang(balmond)
eudora.skill_fireball(balmond)

print("\n TUGAS 4: ENKAPSULASI ")
secure = SecureHero("Layla", 100)
secure.set_hp(-50)  # HP tidak boleh negatif
print(secure.get_hp())

# Akses paksa (Name Mangling) - tidak disarankan
print(f"Akses paksa HP: {secure._SecureHero__hp}")

print("\n TUGAS 5: ABSTRACTION & INTERFACE ")
h = HeroUnit("Alucard")
m = Monster("Serigala")
h.info()
m.info()
h.serang("Serigala")
m.serang("Alucard")

print("\n TUGAS 6: POLYMORPHISM ")
pasukan = [
    PolyMage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Healer("Rafaela")
]

for pahlawan in pasukan:
    pahlawan.serang()