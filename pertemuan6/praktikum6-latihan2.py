#==
# Nama : Cinta Asih Salaamina
# NIM : J0403251045
# Kelas : B2
#==
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # Bagian rumpang pertama (ascending) diisi dengan: data[j] > key
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        # Bagian rumpang kedua diisi dengan: data[j + 1] = key
        data[j + 1] = key

    return data

# ==========================================
# JAWABAN SOAL LATIHAN 2
# ==========================================

# 1. Lengkapi kondisi agar menjadi sorting ascending.
# Jawab:
# - Rumpang pertama di bagian `while` diisi dengan: `data[j] > key`
#   Kenapa? Karena kita mau urut dari kecil ke besar.
#   Jadi kalau ada angka di kiri yang lebih besar dari key,
#   dia harus digeser dulu ke kanan supaya key bisa masuk
#   ke posisi yang lebih pas.

# - Rumpang kedua diisi dengan: `data[j + 1] = key`
#   Setelah selesai geser-geser, pasti ada satu posisi kosong
#   yang udah siap buat si key. Nah posisi itu ada di j + 1.
#   Jadi key ditaruh di situ biar urutannya rapi.

# 2. Ubah agar menjadi descending.
# Jawab:
# Kalau mau dari besar ke kecil (descending),
# kita cuma perlu ubah tanda pembandingnya aja.
#
# Dari:
# while j >= 0 and data[j] > key:
#
# Jadi:
# while j >= 0 and data[j] < key:
#
# Logikanya kebalik.
# Sekarang yang digeser itu justru angka yang lebih kecil dari key.
# Jadi angka besar bakal stay di kiri,
# dan hasil akhirnya urut dari besar ke kecil.