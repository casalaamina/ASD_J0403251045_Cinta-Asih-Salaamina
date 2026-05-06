# Nama  : Cinta Asih Salaamina
# NIM   : J0403251045
# Kelas : B-2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Menjalankan program
hasil = dijkstra(graph, 'Gerbang')

# Menampilkan hasil
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Lokasi mana yang paling dekat dari Gerbang?
# Jawab : Kantin, dengan waktu tempuh 2 menit.

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# Jawab : 7 menit, melalui jalur Gerbang -> Kantin -> Lab -> Aula
#         (2 + 4 + 1 = 7)

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# Jawab : Tidak selalu.
#         Contohnya dari Gerbang ke Aula:
#         Jalur langsung melalui Kantin = 2 + 7 = 9 menit
#         Tetapi jalur tidak langsung (melewati Lab) = 2 + 4 + 1 = 7 menit
#         Jadi, jalur dengan lebih banyak langkah bisa lebih cepat jika bobotnya lebih kecil.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
# Jawab : Karena semua bobot bernilai positif (waktu tempuh tidak mungkin negatif),
#         sehingga Dijkstra dapat bekerja dengan optimal untuk mencari jalur tercepat
#         dari satu lokasi ke lokasi lainnya secara efisien.