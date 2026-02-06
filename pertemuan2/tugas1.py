# =====================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File.txt)
#
# Nama : Cinta Asih Salaamina
# NIM : J0403251045
# Kelas : B2
# =====================================
# Program ini membaca data stok barang dari file .txt, menyimpan dalam dictionary,
# dan memungkinkan pengguna untuk melakukan operasi seperti mencari, menambah,
# dan mengupdate stok barang secara interaktif.
# =====================================

# Konstanta nama file yang berisi data stok barang
NAMA_FILE = "stok_barang.txt"

# ----------------------------------------------------
# Fungsi: Validasi format kode barang
# ----------------------------------------------------
def validasi_kode_barang(kode):
    """
    Validasi format kode barang.
    Format: BRG + 3 digit angka (contoh: BRG001, BRG123, BRG999)
    Panjang total: 6 karakter.
    
    Parameter:
        kode (string): Kode barang yang akan divalidasi
    
    Return:
        tuple: (bool, str) - (valid, pesan_error)
    """
    # Validasi panjang kode harus tepat 6 karakter
    if len(kode) != 6:
        return False, "Kode barang harus memiliki panjang 6 karakter (BRG + 3 digit)."
    
    # Validasi 3 karakter pertama harus 'BRG'
    if kode[:3] != "BRG":
        return False, "Kode barang harus diawali dengan 'BRG'."
    
    # Validasi 3 karakter terakhir harus berupa angka
    if not kode[3:].isdigit():
        return False, "3 karakter terakhir kode barang harus berupa angka (0-9)."
    
    return True, ""

# ----------------------------------------------------
# Fungsi: Membaca data dari file
# ----------------------------------------------------
def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang, NamaBarang, Stok
    Output:
        stok_dict (dictionary)
        key = kode_barang
        value = {"nama": nama_barang, "stok": stok_int}
    """
    # Inisialisasi dictionary kosong untuk menyimpan data stok
    stok_dict = {}
    
    # Membuka file dengan exception handling untuk menangani file yang tidak ada
    # Menggunakan encoding utf-8 untuk mendukung karakter khusus
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            for baris in f:
                baris = baris.strip() # menghilangkan \n dan spasi di awal/akhir
                
                # Lewati baris kosong untuk menghindari error parsing
                if not baris:
                    continue
                
                # Memisahkan data berdasarkan delimiter koma (KodeBarang,NamaBarang,Stok)
                parts = baris.split(",")
                
                # Memvalidasi bahwa format data memiliki 3 komponen
                if len(parts) != 3:
                    continue
                    
                # Unpacking data dari baris file
                kode, nama, stok_str = parts
                
                # Konversi data stok dari string ke integer, lewati jika format salah
                try:
                    stok_int = int(stok_str)
                except ValueError:
                    continue
                
                # Menyimpan data ke dalam dictionary dengan kode barang sebagai key
                # Value berupa dictionary dengan nama dan stok sebagai sub-key
                stok_dict[kode.strip()] = {"nama": nama.strip(), "stok": stok_int}
                
    except FileNotFoundError:
        # Jika file tidak ditemukan, tampilkan pesan dan lanjutkan dengan dictionary kosong
        # Ini memungkinkan program untuk tetap berjalan meskipun file tidak ada
        print(f"File '{nama_file}' tidak ditemukan. Memulai dengan data kosong.")
        
    return stok_dict

# ----------------------------------------------------
# Fungsi: Menyimpan data ke file
# ----------------------------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok dari dictionary ke file teks.
    Format per baris: KodeBarang, Nama Barang, Stok
    """
    # Membuka file dalam mode write (mengesampingkan isi lama) dengan encoding utf-8
    with open(nama_file, "w", encoding="utf-8") as f:
        # Mengurutkan kunci dictionary berdasarkan kode barang secara alfabetis
        # Untuk memastikan data tersimpan dengan terstruktur dan konsisten
        for kode in sorted(stok_dict.keys()):
            # Mengambil nama barang dan stok dari dictionary
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            
            # Menulis ke file dengan format: KodeBarang,NamaBarang,Stok (satu baris per barang)
            f.write(f"{kode},{nama},{stok}\n")
    

# ----------------------------------------------------
# Fungsi: Menampilkan semua data (Menu 1)
# ----------------------------------------------------
def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict dalam format tabel.
    Jika stok kosong, tampilkan pesan pemberitahuan.
    """
    # Validasi: jika dictionary kosong, tampilkan pesan dan keluar dari fungsi
    if not stok_dict:
        print("\nStok barang kosong.")
        return
    
    # Menampilkan header tabel dengan judul yang jelas
    print("\n=== DAFTAR STOK BARANG ===")
    
    # Format header tabel dengan kolom yang rapi dan align
    print(f"{'Kode': <10} | {'Nama Barang': <20} | {'Stok': >5}")
    print("-" * 39)
    
    # Menampilkan setiap item barang dalam format tabel yang tersusun rapi
    # Data disort berdasarkan kode barang agar lebih terstruktur
    for kode in sorted(stok_dict.keys()):
        # Mengambil data nama dan stok dari dictionary
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        # Menampilkan data dalam format rapi menggunakan f-string dengan alignment
        print(f"{kode: <10} | {nama: <20} | {stok: >5}")


# ----------------------------------------------------
# Fungsi: Cari barang berdasarkan kode (Menu 2)
# ----------------------------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    Menampilkan detail barang jika ditemukan, atau pesan error jika tidak ditemukan.
    """
    # Meminta input kode barang dari pengguna dan menghilangkan whitespace
    kode_cari = input("Masukkan kode barang yang ingin dicari: ").strip().upper()
    
    # Validasi: mengecek format kode barang (harus BRG + 3 digit)
    valid, pesan_error = validasi_kode_barang(kode_cari)
    if not valid:
        print(f"Format kode barang tidak valid. {pesan_error}")
        return
    
    # Validasi: mengecek apakah kode barang ada dalam dictionary
    if kode_cari in stok_dict:
        # Jika kode ditemukan: ambil data nama dan stok
        nama = stok_dict[kode_cari]["nama"]
        stok = stok_dict[kode_cari]["stok"]
        # Tampilkan detail barang yang ditemukan dalam format yang rapi
        print("\n=== Barang Ditemukan ===")
        print(f"Kode : {kode_cari}")
        print(f"Nama : {nama}")
        print(f"Stok : {stok}")
    else:
        # Jika kode tidak ditemukan: tampilkan pesan error
        print("\nBarang tidak ditemukan.")


# ----------------------------------------------------
# Fungsi: Tambah barang baru (Menu 3)
# ----------------------------------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    Melakukan validasi kode duplikat dan format input data.
    """
    # Menampilkan header menu untuk penambahan barang baru
    print("\n--- TAMBAH BARANG BARU ---")
    # Meminta kode barang dari pengguna dan mengubahnya ke uppercase untuk konsistensi
    kode = input("Masukkan kode barang baru (format: BRG###): ").strip().upper()
    
    # Validasi: mengecek format kode barang (harus BRG + 3 digit)
    valid, pesan_error = validasi_kode_barang(kode)
    if not valid:
        print(f"Format kode barang tidak valid. {pesan_error} Penambahan dibatalkan.")
        return
    
    # Validasi: mengecek apakah kode barang sudah ada dalam dictionary (duplikat)
    if kode in stok_dict:
        # Jika kode sudah ada: tampilkan pesan error dan batalkan operasi
        print("Kode sudah digunakan. Penambahan dibatalkan.")
        return
        
    # Meminta nama barang dari pengguna
    nama = input("Masukkan nama barang: ").strip()
    
    # Meminta stok awal barang dengan validasi tipe data integer
    try:
        # Mengkonversi input stok ke integer
        stok_awal = int(input("Masukkan stok awal (angka): ").strip())
        # Validasi: stok tidak boleh negatif
        if stok_awal < 0:
            print("Stok awal tidak boleh negatif. Penambahan dibatalkan.")
            return
    except ValueError:
        # Jika input bukan angka: tampilkan error dan batalkan
        print("Stok harus berupa angka. Penambahan dibatalkan.")
        return
    
    # Menyimpan data barang baru ke dalam dictionary
    # Key: kode barang, Value: dictionary dengan nama dan stok
    stok_dict[kode] = {"nama": nama, "stok": stok_awal}
    print(f"Barang {nama} dengan kode {kode} berhasil ditambahkan.")


# ----------------------------------------------------
# Fungsi: Update stok barang (Menu 4)
# ----------------------------------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    Validasi stok tidak boleh menjadi negatif setelah operasi.
    """
    # Menampilkan header menu untuk update stok
    print("\n--- UPDATE STOK BARANG ---")
    # Meminta kode barang yang ingin diupdate
    kode = input("Masukkan kode barang yang ingin diupdate (format: BRG###): ").strip().upper()
    
    # Validasi: mengecek format kode barang (harus BRG + 3 digit)
    valid, pesan_error = validasi_kode_barang(kode)
    if not valid:
        print(f"Format kode barang tidak valid. {pesan_error} Update dibatalkan.")
        return
    
    # Validasi: mengecek apakah kode barang ada dalam dictionary
    if kode not in stok_dict:
        # Jika kode tidak ditemukan: tampilkan error dan batalkan
        print("Kode barang tidak ditemukan. Update dibatalkan.")
        return
        
    # Mengambil data nama dan stok barang dari dictionary
    nama_barang = stok_dict[kode]["nama"]
    stok_lama = stok_dict[kode]["stok"]
    
    # Menampilkan informasi barang yang dipilih
    print(f"Barang terpilih: {nama_barang} (Stok saat ini: {stok_lama})")
    # Menampilkan pilihan jenis update (tambah atau kurangi)
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    
    # Meminta pilihan dari pengguna
    pilihan = input("Masukkan pilihan (1/2): ").strip()
    
    # Validasi: pilihan harus 1 atau 2
    if pilihan not in ["1", "2"]:
        print("Pilihan tidak valid. Update dibatalkan.")
        return
        
    try:
        # Meminta jumlah perubahan stok dari pengguna (harus positif)
        jumlah_perubahan = int(input("Masukkan jumlah perubahan stok (angka): ").strip())
        # Validasi: jumlah perubahan tidak boleh negatif
        if jumlah_perubahan < 0:
            print("Jumlah perubahan harus positif. Update dibatalkan.")
            return
    except ValueError:
        # Jika input bukan angka: tampilkan error
        print("Jumlah harus berupa angka. Update dibatalkan.")
        return
    
    # Inisialisasi variabel stok_baru dengan nilai stok lama
    stok_baru = stok_lama
    
    # Logika perubahan stok berdasarkan pilihan pengguna
    if pilihan == "1":
        # Pilihan 1: Menambah stok (stok_baru = stok_lama + jumlah_perubahan)
        stok_baru = stok_lama + jumlah_perubahan
        aksi = "ditambah"
    elif pilihan == "2":
        # Pilihan 2: Mengurangi stok (stok_baru = stok_lama - jumlah_perubahan)
        stok_baru = stok_lama - jumlah_perubahan
        aksi = "dikurangi"
        
        # Validasi: stok tidak boleh menjadi negatif setelah pengurangan
        # Jika hasil perhitungan negatif: batalkan dan tampilkan error
        if stok_baru < 0:
            print(f"Gagal update: Stok tidak boleh negatif (Hasil: {stok_baru}). Update dibatalkan.")
            return
    
    # Jika semua validasi lolos: update stok di dictionary
    stok_dict[kode]["stok"] = stok_baru
    # Tampilkan pesan sukses dengan detail perubahan stok
    print(f"Update berhasil. Stok {nama_barang} {aksi} {jumlah_perubahan}, stok baru: {stok_baru}.")


# ----------------------------------------------------
# ====================================================
# PROGRAM UTAMA
# ====================================================
def main():
    """
    Fungsi utama yang menjalankan program stok barang kantin.
    Menampilkan menu interaktif dan menghandle pilihan pengguna.
    """
    # Membaca data stok barang dari file saat program dimulai
    stok_barang = baca_stok(NAMA_FILE)

    # Loop utama untuk menampilkan menu dan memproses pilihan pengguna
    while True:
        # Menampilkan menu utama dengan semua pilihan yang tersedia
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        
        # Meminta input pilihan menu dari pengguna
        pilihan = input("Pilih menu: ").strip()
        
        # Proses pilihan menu
        if pilihan == "1":
            # Menu 1: Menampilkan semua barang
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            # Menu 2: Mencari barang berdasarkan kode
            cari_barang(stok_barang)
        elif pilihan == "3":
            # Menu 3: Menambahkan barang baru
            tambah_barang(stok_barang)
        elif pilihan == "4":
            # Menu 4: Mengupdate stok barang (tambah/kurangi)
            update_stok(stok_barang)
        elif pilihan == "5":
            # Menu 5: Menyimpan perubahan data ke file
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan ke file.")
        elif pilihan == "0":
            # Menu 0: Keluar dari program dan tampilkan pesan
            print("Program selesai.")
            break
        else:
            # Jika pilihan tidak valid: tampilkan pesan error
            print("Pilihan tidak valid. Silakan coba lagi.")

# ====================================================
# ENTRY POINT PROGRAM
# ====================================================
# Mengecek apakah file dijalankan sebagai main program (bukan import)
if __name__ == "__main__":
    # Memanggil fungsi main untuk memulai program
    main()