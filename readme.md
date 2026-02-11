Tugas 1 & 2 (Class, Object, dan Interaksi Objek)
Pada tugas ini dibuat class Hero dengan atribut public (name, hp, attack_power) dan beberapa method (info, serang, diserang). Konsep yang ditunjukkan adalah bagaimana object dibuat dari class dan dapat saling berinteraksi, di mana method serang() menerima parameter berupa object lain lalu memanggil method diserang() milik object tersebut. Karena atribut masih bersifat public, nilai seperti hp bisa diubah langsung dari luar class, sehingga menunjukkan kelemahan tanpa enkapsulasi.

Tugas 3 (Inheritance / Pewarisan)
Class Mage merupakan turunan dari Hero menggunakan konsep inheritance, sehingga mewarisi atribut dan method dari parent class. Penggunaan super() memastikan konstruktor Hero tetap dijalankan. Pada tugas ini juga terdapat method overriding pada info() dan penambahan method khusus skill_fireball(), yang menunjukkan bahwa subclass dapat memodifikasi perilaku parent sekaligus menambahkan kemampuan baru.

Tugas 4 (Encapsulation / Enkapsulasi)
Pada class SecureHero, atribut __hp dibuat private menggunakan double underscore untuk melindungi data dari akses langsung. Akses dan perubahan nilai HP dilakukan melalui getter (get_hp) dan setter (set_hp) yang memiliki validasi agar HP tidak negatif atau melebihi batas maksimum. Praktikum ini menunjukkan pentingnya enkapsulasi untuk menjaga integritas data dan mencegah manipulasi langsung yang tidak aman.

Tugas 5 (Abstraction & Interface dengan ABC)
Class GameUnit menggunakan modul ABC dan @abstractmethod untuk membuat kontrak bahwa setiap turunan wajib mengimplementasikan method serang() dan info(). Class HeroUnit dan Monster menjadi implementasi konkret dari abstraksi tersebut. Konsep ini menunjukkan bahwa abstraksi berfungsi sebagai kerangka dasar (blueprint) yang memaksa struktur method tertentu tanpa mendefinisikan detail implementasinya.

Tugas 6 (Polymorphism)
Pada bagian ini beberapa class seperti PolyMage, Archer, Fighter, dan Healer memiliki method serang() dengan perilaku berbeda meskipun nama method sama. Saat semua object dimasukkan ke dalam satu list dan dipanggil dengan perulangan, Python menjalankan versi method sesuai tipe object masing-masing. Ini menunjukkan konsep polymorphism, yaitu satu interface (method yang sama) dapat memiliki banyak bentuk perilaku berbeda tergantung objectnya.

