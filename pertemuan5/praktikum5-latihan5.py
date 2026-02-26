#===================================================================================
#Nama : Cinta Asih S
#NIM : J0403251045
#Kelas : B2
#===================================================================================

# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================
def buat_pin(panjang, hasil=""):
    # Fungsi rekursif untuk menghasilkan semua kombinasi PIN dengan angka 0, 1, 2
    # panjang: panjang PIN yang diinginkan
    # hasil: string PIN yang sedang dibentuk

    # Base case: jika panjang hasil sudah sama dengan panjang PIN yang diinginkan
    if len(hasil) == panjang:
        print("PIN:", hasil)  # Cetak PIN yang sudah lengkap
        return                # Akhiri rekursi untuk cabang ini

    # Loop untuk setiap angka yang mungkin dimasukkan ke PIN
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)  # Rekursi dengan menambah angka ke hasil

# Contoh pemanggilan fungsi buat_pin
buat_pin(3)

# Penjelasan cara mencegah angka yang sama muncul berulang:
#
# Untuk mencegah angka yang sama muncul berurutan (misal '00', '11', '22'),
# kita perlu menambahkan pengecekan sebelum menambah angka ke hasil.
# Caranya, sebelum memanggil rekursi, cek apakah angka yang akan ditambahkan
# sama dengan karakter terakhir pada hasil. Jika sama, lewati angka tersebut.
# Contoh modifikasi pada loop:
#
#    for angka in ["0", "1", "2"]:
#        if len(hasil) == 0 or hasil[-1] != angka:
#            buat_pin(panjang, hasil + angka)
#
# Dengan cara ini, angka yang sama tidak akan muncul secara berurutan dalam PIN.
