#===================================================================================
#Nama : Cinta Asih S
#NIM : J0403251045
#Kelas : B2
#===================================================================================

# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================
def kombinasi(n, hasil=""):
    # Fungsi rekursif untuk menghasilkan semua kombinasi huruf 'A' dan 'B' sepanjang n
    # n: panjang kombinasi yang diinginkan
    # hasil: string kombinasi yang sedang dibentuk

    # Base case: jika panjang hasil sudah sama dengan n
    if len(hasil) == n:
        print(hasil)      # Cetak kombinasi yang sudah lengkap
        return           # Akhiri rekursi untuk cabang ini

    # Recursive call: tambahkan 'A' ke hasil, lanjutkan rekursi
    kombinasi(n, hasil + "A")
    # Recursive call: tambahkan 'B' ke hasil, lanjutkan rekursi
    kombinasi(n, hasil + "B")

# Contoh pemanggilan fungsi kombinasi
kombinasi(2)

# Penjelasan jumlah kombinasi yang dihasilkan:
# Untuk setiap posisi dalam string hasil, ada 2 kemungkinan (yaitu 'A' atau 'B').
# Jika n adalah panjang kombinasi, maka jumlah total kombinasi yang dihasilkan adalah 2^n.
# Misal n=2, maka kombinasi yang dihasilkan: 'AA', 'AB', 'BA', 'BB' (total 4 kombinasi).
# Secara umum, jika n=3 maka kombinasi = 2^3 = 8, dst.
