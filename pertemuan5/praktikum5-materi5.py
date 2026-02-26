#===================================================================================
#Nama : Cinta Asih S
#NIM : J0403251045
#Kelas : B2
#===================================================================================

# ==========================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Fungsi rekursif untuk menghasilkan kombinasi biner sepanjang n dengan batas jumlah '1'
    # n: panjang kombinasi biner yang diinginkan
    # batas: jumlah maksimal karakter '1' yang boleh ada dalam kombinasi
    # hasil: string biner yang sedang dibentuk
    # jumlah_1: jumlah karakter '1' yang sudah ada di hasil

    # Pruning: jika jumlah_1 sudah melewati batas, hentikan rekursi
    if jumlah_1 > batas:
        return  # Tidak lanjutkan jika jumlah '1' melebihi batas

    # Base case: jika panjang string hasil sudah sama dengan n
    if len(hasil) == n:
        print(hasil)  # Cetak kombinasi biner yang memenuhi syarat
        return        # Kembalikan ke pemanggil sebelumnya (akhiri rekursi)

    # Pilihan menambah '0' ke hasil, jumlah_1 tetap
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # Pilihan menambah '1' ke hasil, jumlah_1 bertambah satu
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

# Pemanggilan fungsi biner_batas untuk menghasilkan semua kombinasi biner sepanjang 4
# dengan maksimal 2 karakter '1' di setiap kombinasi
biner_batas(4, 2)
