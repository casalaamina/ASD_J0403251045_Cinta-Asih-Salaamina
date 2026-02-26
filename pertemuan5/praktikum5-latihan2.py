#===================================================================================
#Nama : Cinta Asih S
#NIM : J0403251045
#Kelas : B2
#===================================================================================

# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================
def countdown(n):
    # Fungsi rekursif untuk menghitung mundur dari n ke 0
    # n: angka awal hitung mundur

    # Base case: jika n == 0, cetak 'Selesai' dan akhiri rekursi
    if n == 0:
        print("Selesai")  # Menandakan akhir hitung mundur
        return           # Mengakhiri rekursi

    print("Masuk:", n)      # Menandakan masuk ke level rekursi dengan nilai n saat ini
    countdown(n - 1)        # Recursive call: panggil countdown dengan n dikurangi 1
    print("Keluar:", n)     # Menandakan keluar dari level rekursi dengan nilai n saat ini

# Contoh pemanggilan fungsi countdown
# Akan menampilkan urutan masuk dan keluar rekursi dari 3 ke 0
countdown(3)

# Penjelasan mengapa output 'Keluar' muncul terbalik:
#
# Pada setiap pemanggilan rekursif, program akan mengeksekusi print('Masuk:', n),
# lalu memanggil countdown(n-1) sebelum mengeksekusi print('Keluar:', n).
# Artinya, semua pemanggilan rekursif akan terus masuk ke level lebih dalam
# hingga mencapai base case (n == 0). Setelah base case tercapai dan fungsi mulai
# kembali (return) ke atas, barulah print('Keluar:', n) dieksekusi secara berurutan
# dari pemanggilan terdalam ke terluar. Inilah yang menyebabkan output 'Keluar'
# muncul dari n terkecil ke n terbesar (terbalik dari urutan 'Masuk').
