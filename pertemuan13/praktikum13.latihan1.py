# Nama  : Cinta Asih Salaamina
# NIM   : J0403251045
# Kelas : B-2
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge pada graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Spanning tree yang valid
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis

# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal berisi semua edge yang ada pada graph,
#    sedangkan spanning tree hanya mengambil beberapa edge
#    yang tetap menghubungkan semua node tanpa membentuk cycle.

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Karena tujuan spanning tree adalah membentuk jalur
#    paling sederhana yang menghubungkan semua node.
#    Jika ada cycle, berarti ada jalur yang berputar
#    dan edge menjadi tidak efisien.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Karena spanning tree hanya mengambil edge yang diperlukan
#    untuk menghubungkan semua node.
#    Pada graph dengan n node, spanning tree selalu memiliki
#    n - 1 edge.