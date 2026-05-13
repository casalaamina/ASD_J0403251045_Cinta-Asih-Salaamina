# Nama  : Cinta Asih Salaamina
# NIM   : J0403251045
# Kelas : B-2
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0
connected = set()

# Proses Kruskal
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nMinimum Spanning Tree:")
for edge in mst:
    print(edge)

print("\nTotal bobot =", total_weight)

# Jawaban Analisis

# 1. Edge mana yang dipilih pertama kali?
#    Edge pertama yang dipilih adalah ('C', 'D')
#    dengan bobot 1 karena memiliki bobot paling kecil.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Karena algoritma Kruskal bekerja dengan cara
#    memilih edge berbobot terkecil terlebih dahulu
#    agar total bobot spanning tree menjadi minimum.

# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobot MST yang dihasilkan adalah 6.

# 4. Mengapa edge tertentu tidak dipilih?
#    Karena edge tersebut dapat membentuk cycle
#    atau sudah ada jalur yang menghubungkan node-node tersebut,
#    sehingga edge tidak diperlukan lagi dalam MST.
