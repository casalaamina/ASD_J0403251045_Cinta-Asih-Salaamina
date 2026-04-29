# Representasi hubungan antar lokasi menggunakan adjacency list (dictionary) [cite: 495, 786]
graph = {
 'Rumah': ['Sekolah', 'Toko'],
 'Sekolah': ['Perpustakaan'],
 'Toko': ['Pasar'],
 'Perpustakaan': [],
 'Pasar': []
}

from collections import deque
def bfs(graph, start):
    # Set untuk melacak node yang sudah dikunjungi agar tidak terjadi loop tak terbatas [cite: 625, 784, 788]
    visited = set()
    
    # Antrean (Queue) untuk menyimpan node yang akan diproses selanjutnya [cite: 591, 626, 788]
    queue = deque([start])
    
    # Tandai node awal sebagai sudah dikunjungi [cite: 592, 629, 788]
    visited.add(start)
 
    while queue:
        # Ambil node paling depan dari antrean [cite: 593, 633, 788]
        node = queue.popleft()
        # Tampilkan node yang sedang dikunjungi [cite: 638, 788]
        print(node, end=" ")
        
        # Periksa semua tetangga dari node saat ini [cite: 594, 640, 788]
        for neighbor in graph[node]:
            # Jika tetangga belum dikunjungi, masukkan ke antrean [cite: 595, 642, 644, 788]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
print("BFS dari Rumah:")
bfs(graph, 'Rumah')




"""
# ============================================ #
# jawaban soal 
# ============================================ #

1.Node mana yang dikunjungi pertama?
Jawaban: Node yang dikunjungi pertama adalah 'Rumah' karena kita memulai penelusuran dari node tersebut.

2. Mengapa BFS cocok untuk mencari jalur terdekat?
Jawaban: BFS cocok untuk mencari jalur terdekat karena BFS mengeksplorasi semua node pada tingkat yang sama sebelum melanjutkan ke tingkat berikutnya. Dengan cara ini, BFS akan menemukan jalur terpendek (dalam hal jumlah edge) dari node awal ke node tujuan jika ada.

3. Apa perbedaan urutan BFS jika struktur graph diubah?
Jawaban: Urutan BFS akan berubah jika struktur graph diubah karena BFS mengikuti urutan tetangga yang ada dalam graph. Jika kita mengubah urutan tetangga atau menambahkan/menghapus node dan edge, maka urutan kunjungan BFS juga akan berubah sesuai dengan struktur baru dari graph tersebut.
"""
