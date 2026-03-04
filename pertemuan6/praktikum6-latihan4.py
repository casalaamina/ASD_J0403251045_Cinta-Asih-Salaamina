#==
# Nama : Cinta Asih Salaamina
# NIM : J0403251045
# Kelas : B2
#==

from heapq import merge


def merge_sort(data):
    # Base case
    if len(data) <= 1:
        return data

    # Membagi data menjadi dua bagian (kiri dan kanan)
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    # Memanggil dirinya sendiri (rekursi)
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Menggabungkan dua bagian yang sudah terurut
    return merge(left_sorted, right_sorted)

# ==========================================
# JAWABAN SOAL LATIHAN 4
# ==========================================

# 1. Apa yang dimaksud dengan base case?
# Jawab:
# Base case itu kondisi berhenti dalam rekursi.
# Jadi biar fungsi gak manggil dirinya sendiri terus-terusan tanpa akhir.
# Di kode Merge Sort, base case-nya itu:
# if len(data) <= 1
# Logikanya simpel: kalau list cuma ada 1 elemen (atau kosong),
# ya udah pasti terurut. Jadi gak perlu dipecah lagi.

# 2. Mengapa fungsi memanggil dirinya sendiri?
# Jawab:
# Karena Merge Sort pakai konsep bagi dulu, beresin belakangan.
# List yang panjang dipecah jadi dua bagian (left dan right),
# terus masing-masing bagian itu disortir lagi dengan cara yang sama.
# Proses ini terus diulang sampai ukurannya kecil banget (kena base case).
# Intinya, lebih gampang ngurus list kecil dulu,
# baru nanti digabung lagi jadi rapi.

# 3. Apa tujuan fungsi merge()?
# Jawab:
# Fungsi merge() itu tugasnya nyatuin lagi.
# Setelah list dipecah-pecah dan masing-masing udah terurut,
# merge() bakal bandingin elemen dari dua sisi (left dan right)
# satu per satu, lalu masukin ke list baru secara berurutan.
# Jadi hasil akhirnya tetap urut dengan benar.