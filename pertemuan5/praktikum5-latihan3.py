#===================================================================================
#Nama : Cinta Asih S
#NIM : J0403251045
#Kelas : B2
#===================================================================================

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================
def cari_maks(data, index=0):
    # Fungsi rekursif untuk mencari nilai maksimum dalam list data
    # data: list angka yang akan dicari nilai maksimumnya
    # index: posisi elemen yang sedang diperiksa

    # Base case: jika index sudah di elemen terakhir, kembalikan elemen tersebut
    if index == len(data) - 1:
        return data[index]  # Mengembalikan elemen terakhir sebagai nilai maksimum sementara

    # Recursive call: cari nilai maksimum dari sisa elemen setelah index saat ini
    maks_sisa = cari_maks(data, index + 1)

    # Bandingkan elemen saat ini dengan nilai maksimum dari sisa elemen
    if data[index] > maks_sisa:
        return data[index]  # Jika elemen saat ini lebih besar, kembalikan elemen saat ini
    else:
        return maks_sisa   # Jika tidak, kembalikan nilai maksimum dari sisa elemen

# Contoh penggunaan fungsi cari_maks
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

# Penjelasan alur program:
# 1. Fungsi cari_maks dipanggil dengan data = [3, 7, 2, 9, 5], index = 0
# 2. Karena index belum di akhir, rekursi ke index berikutnya hingga index terakhir
# 3. Pada index terakhir (base case), kembalikan nilai elemen tersebut
# 4. Setiap langkah mundur, bandingkan elemen saat ini dengan hasil maksimum dari sisa elemen
# 5. Hasil akhir adalah nilai maksimum dari seluruh elemen list
#
# Base case: index == len(data) - 1 (hanya satu elemen yang tersisa, pasti maksimum)
# Recursive call: cari_maks(data, index + 1) untuk mencari maksimum dari sisa elemen