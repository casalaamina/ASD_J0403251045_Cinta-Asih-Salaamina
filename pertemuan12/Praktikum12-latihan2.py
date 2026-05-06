# Nama  : Cinta Asih Salaamina
# NIM   : J0403251045
# Kelas : B-2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak saat ini lebih besar dari yang sudah tercatat, skip
        if current_distance > distances[current_node]:
            continue
        
        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Update jika lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Menjalankan fungsi
hasil = dijkstra(graph, 'A')

# Menampilkan hasil
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Berapa jarak terpendek dari A ke B?
# Jawab : 4

# 2. Berapa jarak terpendek dari A ke C?
# Jawab : 2

# 3. Berapa jarak terpendek dari A ke D?
# Jawab : 3 (melalui jalur A -> C -> D)

# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# Jawab : Karena total bobot jalur melalui C lebih kecil.
#         A -> C -> D = 2 + 1 = 3
#         A -> B -> D = 4 + 5 = 9
#         Sehingga jalur melalui C dipilih sebagai jalur terpendek.

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# Jawab : Priority queue digunakan untuk mengambil node dengan jarak terkecil terlebih dahulu.
#         Hal ini membuat proses pencarian jalur terpendek menjadi lebih efisien.

# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
# Jawab : Karena algoritma Dijkstra mengasumsikan bahwa jarak yang sudah dipilih adalah yang terbaik.
#         Jika ada bobot negatif, bisa muncul jalur yang lebih pendek setelahnya,
#         sehingga hasil perhitungan bisa menjadi tidak akurat.