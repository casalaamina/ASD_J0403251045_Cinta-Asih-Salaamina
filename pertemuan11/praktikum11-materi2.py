# ======
# implementasi BFS (Breadth First Search)
# =======

#struktur data untuk membuat antrian, menggunakan library collections bawaan python yaitu deque (double ended queue)

from collections import deque


#representasi graph
graph ={
    'A': ['B', 'C'],
    'B': ['A', 'D',],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def bsf(graph, start):
    #fungsi untuk melakukan penelusuran BFS pada graph
    # graph: dictionary yang menyimpan struktur dari graph
    # start: node awal untuk memulai penelusuran
    
    #quque untuk menyimpan node yang akan diproses / di baca
    queue = deque()
    
    # variabel yang digunakan untuk menyimpan node yang sudah diproses/dikunjung
    visited = set()

    #memasukkan node awal ke dalam antrian
    queue.append(start)

    # tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start) 

    while queue:
        #mengambil node paling depan dari queue
        node = queue.popleft() 

        #tampilkan node yang sedang dikunjungi
        print(node, end=" ")

        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            #jika tetangga belum dikunjungi
            if neighbor not in visited: #jika tetangga belum dikunjungi

                #print(neighbor) #menampilkan tetangga yang dikunjungi
                #tandai sebagai sudah dikunjungi
                visited.add(neighbor) 
                #masukkan tetangga ke dalam queue untuk diproses nanti
                queue.append(neighbor) 

#menjalankan BFS dari graph A
bsf(graph, 'A') 