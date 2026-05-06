def bellman_ford(graph, start):
    # Membuat dictionary untuk menyimpan jarak dari node awal ke semua node
    distances = {node: float('inf') for node in graph}  # Default = tak hingga
    
    # Set jarak node awal menjadi 0
    distances[start] = 0
 
    # Proses relaksasi dilakukan sebanyak (jumlah node - 1) kali
    for _ in range(len(graph) - 1):
        
        # Iterasi setiap node dalam graph
        for node in graph:
            
            # Iterasi setiap tetangga dari node tersebut
            for neighbor, weight in graph[node].items():
                
                # Jika jarak ke node sekarang + bobot edge lebih kecil
                if distances[node] + weight < distances[neighbor]:
                    
                    # Update jarak ke neighbor
                    distances[neighbor] = distances[node] + weight
    
    # Mengembalikan hasil jarak terpendek
    return distances


# penjelasan langkah-langkah algoritma Bellman-Ford:
#Inisialisasi:
# Semua jarak di-set ∞ kecuali node awal (start) = 0
#
#Relaksasi:
# Dilakukan sebanyak (jumlah node - 1) kali
# Kenapa? Karena jalur terpanjang tanpa siklus maksimal melewati (n-1) edge
#
#Di setiap iterasi:
# Cek semua edge dalam graph
# Jika ditemukan jalur lebih pendek → update jarak
#
#Contoh alur sederhana:
# Misal dari A:
#  Iterasi 1: update jarak langsung
#  Iterasi 2: update jalur yang lebih jauh (via node lain)
#  Iterasi berikutnya: memastikan semua jalur optimal
#
#Kelebihan Bellman-Ford:
# Bisa menangani bobot negatif (tidak seperti Dijkstra)
#
#Kekurangan:
# Lebih lambat (O(V * E))
#
#Catatan penting (belum ada di kode ini):
# Biasanya Bellman-Ford juga mengecek "negative cycle"
# dengan satu iterasi tambahan:
# Jika masih bisa relaksasi → berarti ada siklus negatif
#
# Jadi, algoritma ini bekerja dengan "memperbaiki jarak sedikit demi sedikit"
# sampai semua kemungkinan jalur optimal ditemukan.