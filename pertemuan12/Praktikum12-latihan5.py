# Nama  : Cinta Asih Salaamina
# NIM   : J0403251045
# Kelas : B-2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Studi Kasus: Jalur Terpendek Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq  # Digunakan untuk priority queue

# 1. Representasi graph berbobot (dictionary)
# Setiap kota memiliki tetangga dengan bobot (jarak/waktu)
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    # Inisialisasi jarak semua node = tak hingga
    distances = {node: float('inf') for node in graph}
    
    # Jarak ke node awal = 0
    distances[start] = 0
    
    # Priority queue untuk memilih jarak terkecil
    priority_queue = [(0, start)]
    
    # Proses selama queue masih ada isi
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip jika jarak lebih besar dari yang sudah tercatat
        if current_distance > distances[current_node]:
            continue
        
        # Cek semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika ditemukan jarak lebih kecil → update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# 3. Menentukan node awal
start_node = 'Bogor'

# Menjalankan algoritma
hasil = dijkstra(graph, start_node)

# 4. Output hasil
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print("Bogor ->", kota, "=", jarak)


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Node awal yang digunakan apa?
# Jawab : Bogor

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# Jawab : Depok, dengan jarak 2

# 3. Node mana yang memiliki jarak paling besar dari node awal?
# Jawab : Bandung, dengan jarak 8

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Jawab : Algoritma dimulai dari node Bogor dengan jarak 0.
#         Kemudian memeriksa semua tetangga terdekat (Jakarta dan Depok).
#         Dipilih node dengan jarak paling kecil terlebih dahulu, yaitu Depok (2).
#         Dari Depok, diperiksa jalur ke Jakarta dan Bandung.
#         Jalur ke Jakarta menjadi lebih pendek (2 + 2 = 4 dibanding 5 langsung).
#         Selanjutnya, diperiksa jalur ke Bandung melalui Depok (2 + 6 = 8)
#         dan melalui Jakarta (4 + 7 = 11), sehingga dipilih jalur melalui Depok.
#         Proses ini terus berlanjut hingga semua node mendapatkan jarak terpendek.