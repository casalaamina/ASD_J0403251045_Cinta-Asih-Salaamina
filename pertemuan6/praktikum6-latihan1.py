#==
# Nama : Cinta Asih Salaamina
# NIM : J0403251045
# Kelas : B2
#==

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data

# ==========================================
# JAWABAN SOAL LATIHAN 1
# ==========================================

# 1. Mengapa perulangan dimulai dari indeks 1?
# Jawab: Karena elemen pertama (indeks 0) itu udah kita anggap beres/urut.
# Jadi kita mulai dari indeks 1 supaya bisa bandingin elemen kedua
# ke bagian kiri yang udah dianggap terurut tadi. Intinya, kita mau
# nyisipin elemen baru ke tempat yang seharusnya di bagian kiri.

# 2. Apa fungsi variabel key?
# Jawab: `key` itu buat nyimpen sementara nilai yang lagi kita proses.
# Soalnya pas kita geser-geser elemen yang lebih besar ke kanan,
# posisi awal si key bisa ketimpa. Jadi dia harus "diamankan" dulu
# biar nanti bisa ditaruh lagi di posisi yang tepat.

# 3. Mengapa digunakan while, bukan for?
# Jawab: Karena kita gak tau harus geser berapa kali.
# Selama masih di dalam batas array (j >= 0)
# dan selama angkanya masih lebih besar dari key,
# ya kita terus mundur ke kiri.
# Jadi lebih fleksibel pakai while daripada for yang biasanya
# jumlah perulangannya udah fix dari awal.

# 4. Operasi apa yang terjadi di dalam while?
# Jawab: Di dalam while itu intinya lagi geser-geser elemen.
# Kalau elemen di kiri lebih besar dari key,
# dia digeser satu langkah ke kanan biar kasih ruang.
# Terus j dikurangin 1 supaya bisa cek lagi ke kiri.
# Proses ini diulang sampai ketemu posisi yang pas buat key.