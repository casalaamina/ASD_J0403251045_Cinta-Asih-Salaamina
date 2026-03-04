#==
# Nama : Cinta Asih Salaamina
# NIM : J0403251045
# Kelas : B2
#==

def insertion_sort_trace(data):
    print(f"Data awal : {data}")
    
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        # buat ngitung berapa kali dia geser
        shifts = 0 

        # selama masih di kiri dan angkanya lebih besar dari key
        # ya kita geser terus
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            shifts += 1  

        # setelah selesai geser-geser, key masuk ke posisi yang pas
        data[j + 1] = key
        
        print(f"Iterasi i = {i} | key = {key} | geser = {shifts} | list = {data}")

    return data


# Menjalankan program
data_soal = [5, 2, 4, 6, 1, 3]
print("Mulai Tracing:")
insertion_sort_trace(data_soal)


# ==========================================
# JAWABAN SOAL LATIHAN 3
# ==========================================

# 1. Isi list setelah iterasi i = 1
# Jawab: [2, 5, 4, 6, 1, 3]
# Karena key = 2 dibandingin sama 5.
# 5 lebih besar, jadi digeser ke kanan.
# Terus 2 masuk ke depan.

# 2. Isi list setelah iterasi i = 3
# Jawab: [2, 4, 5, 6, 1, 3]
# Di i = 2, key = 4 → dia masuk di antara 2 dan 5.
# Di i = 3, key = 6 → gak ada yang perlu digeser
# karena 6 memang udah lebih besar dari 5.
# Jadi list-nya tetap.

# 3. Berapa kali pergeseran pada iterasi i = 4?
# Jawab: 4 kali.
# Di i = 4, key = 1.
# Sebelum iterasi ini, list = [2, 4, 5, 6, 1, 3]
# Karena 1 lebih kecil dari semua angka di kiri,
# maka 6 geser, 5 geser, 4 geser, dan 2 geser.
# Total ada 4 pergeseran sebelum 1 akhirnya masuk ke depan.