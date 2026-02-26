#===================================================================================
#Nama : Cinta Asih S
#NIM : J0403251045
#Kelas : B2
#======
# ==========================================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# ==========================================================
def biner(n, hasil=""):
    # Fungsi rekursif untuk menghasilkan kombinasi biner sepanjang n
    # n: panjang kombinasi biner yang diinginkan
    # hasil: string biner yang sedang dibentuk
    if len(hasil) == n:  # Jika panjang string hasil sudah sama dengan n
        print(hasil)     # Cetak kombinasi biner yang sudah lengkap
        return           # Kembalikan ke pemanggil sebelumnya (akhiri rekursi)
    
    biner(n, hasil + "0")  # Tambahkan '0' ke hasil, lanjutkan rekursi
    biner(n, hasil + "1")  # Tambahkan '1' ke hasil, lanjutkan rekursi

# Pemanggilan fungsi biner untuk menghasilkan semua kombinasi biner sepanjang 3
biner(3)  # Akan mencetak semua kombinasi biner dengan panjang 3