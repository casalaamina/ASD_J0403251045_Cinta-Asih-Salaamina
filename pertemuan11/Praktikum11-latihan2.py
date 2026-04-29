graph = {
 'A': ['B', 'C'],
 'B': ['D', 'E'],
 'C': ['F'],
 'D': [],
 'E': [],
 'F': []
}

def dfs(graph, node, visited):
    # Tandai node saat ini sebagai sudah dikunjungi agar tidak diproses ulang [cite: 730, 766, 784, 791]
    visited.add(node)
    # Tampilkan node yang sedang dikunjungi [cite: 768, 791]
    print(node, end=" ")
    
    # Periksa semua tetangga dari node saat ini [cite: 732, 770, 791]
    for neighbor in graph[node]:
        # Jika tetangga belum dikunjungi, lakukan pemanggilan rekursif (masuk lebih dalam) [cite: 733, 772, 774, 791]
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Set kosong untuk melacak node yang sudah dikunjungi [cite: 765, 775, 791]
visited = set()
print("DFS dari A:")
dfs(graph, 'A', visited)

"""
# ============================================ #
# jawaban soal 
# ============================================ #

1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
Jawab: Karena DFS menggunakan prinsip stack atau rekursi, di mana algoritma 
akan segera mengunjungi tetangga pertama yang ditemukan dan langsung 
mengeksplorasi jalur tersebut hingga mencapai titik buntu (dead end) 
sebelum melakukan backtrack. [cite: 654, 655, 709, 785]

2. Apa yang terjadi jika urutan neighbor diubah?
Jawab: Jalur penelusuran akan berubah total. DFS akan mengikuti "cabang" 
pertama yang tersedia dalam daftar. Jika urutannya berbeda, maka cabang 
yang dieksplorasi hingga ke dasar juga akan berbeda. [cite: 781, 792]

3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
Jawab: 
- BFS akan menghasilkan urutan: A B C D E F (menelusuri tetangga langsung A terlebih dahulu). [cite: 646]
#    - DFS menghasilkan urutan: A B D E C F (masuk dari A ke B, lalu menghabiskan 
#      semua turunan B sebelum pindah ke C). [cite: 780, 781]
"""
