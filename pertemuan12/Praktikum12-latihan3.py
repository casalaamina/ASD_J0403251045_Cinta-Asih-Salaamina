# Nama  : Cinta Asih Salaamina
# NIM   : J0403251045
# Kelas : B-2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    
    # Relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                
                # Jika ada jarak lebih kecil, update
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    
    return distances

# Menjalankan fungsi
hasil = bellman_ford(graph, 'A')

# Menampilkan hasil
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Berapa bobot langsung dari A ke B?
# Jawab : 5

# 2. Berapa total bobot jalur A -> C -> B?
# Jawab : 4 (A ke C) + (-2) (C ke B) = 2

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
# Jawab : Jalur A -> C -> B karena total bobotnya lebih kecil (2 dibanding 5)

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
# Jawab : Karena Bellman-Ford tidak mengasumsikan bahwa jarak yang sudah ditemukan pasti optimal.
#         Algoritma ini terus melakukan relaksasi sehingga bisa menemukan jalur lebih pendek
#         meskipun terdapat bobot negatif.

# 5. Apa yang dimaksud dengan proses relaksasi edge?
# Jawab : Relaksasi adalah proses membandingkan jarak lama dengan jarak baru yang lebih kecil,
#         lalu memperbarui jarak tersebut jika ditemukan jalur yang lebih pendek.

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
# Jawab : Bellman-Ford dapat menangani bobot negatif, sedangkan Dijkstra tidak.
#         Namun, Bellman-Ford lebih lambat karena memeriksa semua edge berulang kali,
#         sedangkan Dijkstra lebih cepat karena menggunakan priority queue.