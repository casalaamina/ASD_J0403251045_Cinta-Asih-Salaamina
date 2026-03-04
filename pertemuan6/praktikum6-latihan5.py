#==
# Nama : Cinta Asih Salaamina
# NIM : J0403251045
# Kelas : B2
#==

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        # Bagian rumpang diisi dengan: left[i] <= right[j]
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# ==========================================
# JAWABAN SOAL LATIHAN 5
# ==========================================

# 1. Lengkapi kondisi agar menjadi ascending.
# Jawab:
# Kondisi di bagian `if` diisi dengan: left[i] <= right[j]
#
# Kenapa pakai <= ?
# Karena kita mau urut dari kecil ke besar.
# Jadi tiap bandingin elemen paling depan dari left dan right,
# yang lebih kecil (atau sama) dimasukin dulu ke result.
#
# Pakai <= juga bikin sorting tetap stabil.
# Artinya kalau ada angka yang nilainya sama,
# urutannya gak ketukar dari posisi aslinya.


# 2. Jelaskan fungsi result.extend().
# Jawab:
# result.extend() itu tugasnya ngambil sisa elemen
# yang belum sempat masuk ke result.
#
# Soalnya loop while tadi berhenti kalau salah satu list udah habis.
# Misalnya left udah kosong duluan,
# berarti masih ada sisa di right.
#
# Nah daripada dicek satu-satu lagi,
# langsung aja tambahin semuanya sekaligus pakai extend().
#
# left[i:] dan right[j:] itu artinya:
# ambil dari indeks terakhir yang belum diproses sampai akhir.
#
# Salah satu dari extend ini pasti nambahin list kosong,
# tapi itu aman dan gak ngaruh apa-apa.