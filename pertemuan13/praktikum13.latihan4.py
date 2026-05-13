# Nama  : Cinta Asih Salaamina
# NIM   : J0403251045
# Kelas : B-2
# Praktikum 13 - Graph III: Spanning Tree
# Praktikum 13 - Graph III: Studi Kasus MST Jaringan Kabel Kampus

import heapq

graph = {
    'GedungA': {
        'GedungB': 4,
        'GedungC': 2,
        'GedungD': 5
    },

    'GedungB': {
        'GedungA': 4,
        'GedungD': 3
    },

    'GedungC': {
        'GedungA': 2,
        'GedungD': 1
    },

    'GedungD': {
        'GedungA': 5,
        'GedungB': 3,
        'GedungC': 1
    }
}

def prim(graph, start):

    visited = set([start])
    edges = []

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_cost = 0

    # Proses pembentukan MST
    while edges:

        weight, u, v = heapq.heappop(edges)

        # Memilih edge yang tidak membentuk cycle
        if v not in visited:

            visited.add(v)

            mst.append((u, v, weight))
            total_cost += weight

            # Menambahkan edge baru ke priority queue
            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_cost

mst, total = prim(graph, 'GedungA')

print("Jaringan Kabel Minimum:\n")

for edge in mst:
    print(edge)

print("\nTotal biaya minimum =", total)

# 1. Algoritma apa yang digunakan?
#    Algoritma yang digunakan adalah Algoritma Prim.

# 2. Edge mana saja yang dipilih?
#    Edge yang dipilih yaitu:
#    - GedungA ke GedungC dengan biaya 2
#    - GedungC ke GedungD dengan biaya 1
#    - GedungD ke GedungB dengan biaya 3

# 3. Berapa total biaya minimum?
#    Total biaya minimum yang dihasilkan adalah 6.

# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Karena MST dapat menghubungkan semua gedung
#    dengan total biaya pemasangan kabel paling minimum
#    tanpa adanya jalur yang berulang (cycle),
#    sehingga lebih efisien dan hemat biaya.