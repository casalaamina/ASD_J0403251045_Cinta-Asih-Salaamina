# Nama  : Cinta Asih Salaamina
# NIM   : J0403251045
# Kelas : B-2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']  # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']  # A -> C -> D

# Menampilkan hasil perhitungan
print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

# Menentukan jalur terpendek
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Berapa total bobot jalur A -> B -> D?
# Jawab : 4 (A ke B) + 5 (B ke D) = 9

# 2. Berapa total bobot jalur A -> C -> D?
# Jawab : 2 (A ke C) + 1 (C ke D) = 3

# 3. Jalur mana yang dipilih sebagai jalur terpendek?
# Jawab : Jalur terpendek adalah A -> C -> D karena total bobotnya lebih kecil (3)

# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
# Jawab : Karena yang menentukan adalah total bobot (weight), bukan jumlah langkah.
#         Bisa saja jalur dengan sedikit edge memiliki bobot besar,
#         sedangkan jalur dengan lebih banyak edge justru memiliki total bobot lebih kecil.
#         Jadi, algoritma shortest path selalu mempertimbangkan nilai bobot, bukan jumlah edge.