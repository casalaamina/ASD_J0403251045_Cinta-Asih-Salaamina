# Nama  : Cinta Asih Salaamina
# NIM   : J0403251045
# Kelas : B-2
# Praktikum 13 - Graph III: Spanning Tree

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):

    visited = set([start])
    edges = []

    # Memasukkan edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    # Proses Prim
    while edges:

        weight, u, v = heapq.heappop(edges)

        if v not in visited:

            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge baru dari node yang dipilih
            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("\nTotal bobot =", total)

# 1. Node awal apa yang digunakan?
#    Node awal yang digunakan adalah node 'A'.

# 2. Edge mana yang dipilih pertama kali?
#    Edge pertama yang dipilih adalah
#    ('A', 'C', 2) karena memiliki bobot terkecil
#    dari node awal.

# 3. Bagaimana Prim menentukan edge berikutnya?
#    Prim memilih edge dengan bobot terkecil
#    yang terhubung ke node yang sudah dikunjungi
#    dan tidak membentuk cycle.

# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobot MST yang dihasilkan adalah 6.

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Prim membangun MST mulai dari satu node
#    lalu memperluas graph sedikit demi sedikit.
#    Sedangkan Kruskal memilih edge dengan bobot
#    terkecil secara global tanpa memulai dari node tertentu.