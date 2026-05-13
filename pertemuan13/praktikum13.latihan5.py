# Nama  : Cinta Asih Salaamina
# NIM   : J0403251045
# Kelas : B-2
# Praktikum 13 - Graph III: Spanning Tree

# KASUS 1 : JARINGAN JALAN ANTAR KOTA

# Daftar edge: (bobot, node1, node2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

edges.sort()

mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

print("Daftar Edge Graph:\n")

for edge in edges:
    print(edge)

print("\nMinimum Spanning Tree:\n")

for edge in mst:
    print(edge)

print("\nTotal bobot minimum =", total_weight)

# 1. Kasus apa yang dipilih?
#    Kasus yang dipilih adalah
#    Jaringan Jalan Antar Kota.

# 2. Algoritma apa yang digunakan?
#    Algoritma yang digunakan adalah Kruskal.

# 3. Edge mana saja yang dipilih dalam MST?
#    Edge yang dipilih yaitu:
#    - Bogor ke Depok dengan bobot 2
#    - Depok ke Jakarta dengan bobot 3
#    - Depok ke Bandung dengan bobot 4

# 4. Berapa total bobot MST?
#    Total bobot MST adalah 9.

# 5. Mengapa edge tertentu tidak dipilih?
#    Karena edge tersebut memiliki bobot lebih besar
#    atau dapat membentuk cycle sehingga tidak diperlukan
#    dalam Minimum Spanning Tree.
