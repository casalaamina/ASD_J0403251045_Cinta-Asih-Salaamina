# ==========================================================
# materi 1: 
# ==========================================================

import heapq  # Mengimpor library heapq untuk membuat priority queue (antrian prioritas)

# Representasi graph dalam bentuk dictionary (adjacency list)
graph = {
    'A': {'B': 4, 'C': 2},  # Node A terhubung ke B (4) dan C (2)
    'B': {'D': 5},          # Node B terhubung ke D (5)
    'C': {'D': 1},          # Node C terhubung ke D (1)
    'D': {}                 # Node D tidak punya tetangga
}

def dijkstra(graph, start):
    # Membuat dictionary untuk menyimpan jarak minimum dari start ke semua node
    distances = {node: float('inf') for node in graph}  # Default jarak = tak hingga
    
    # Set jarak node awal menjadi 0
    distances[start] = 0
    
    # Membuat priority queue (heap), berisi tuple (jarak, node)
    pq = [(0, start)]
    
    # Selama masih ada node dalam priority queue
    while pq:
        # Ambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(pq)
        
        # Iterasi semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak baru ke tetangga
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil
            if distance < distances[neighbor]:
                # Update jarak
                distances[neighbor] = distance
                
                # Masukkan ke priority queue untuk diproses lagi
                heapq.heappush(pq, (distance, neighbor))
    
    # Mengembalikan hasil jarak terpendek ke semua node
    return distances

# Memanggil fungsi dijkstra dengan node awal 'A'
hasil = dijkstra(graph, 'A')

# Menampilkan hasil
print(hasil)


# penjelasan langkah-langkah algoritma Dijkstra pada graph di atas:
#Program mulai dari node 'A'
#Jarak awal:
#  A = 0, B = ∞, C = ∞, D = ∞
#
#Dari A:
# Ke B = 4 → update
# Ke C = 2 → update
#
#Node dengan jarak terkecil berikutnya: C (2)
# Dari C ke D = 2 + 1 = 3 → update
#
#Node berikutnya: B (4)
# Dari B ke D = 4 + 5 = 9 (tidak dipakai karena sudah ada 3 yang lebih kecil)
#
#Node berikutnya: D (3)
# Tidak ada tetangga → selesai
#
#Hasil akhir:
# A = 0
# B = 4
# C = 2
# D = 3
#
#Jadi, jalur tercepat dari A ke D adalah:
# A → C → D dengan total jarak = 3