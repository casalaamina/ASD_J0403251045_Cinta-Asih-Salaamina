# ======
# implementasi DFS (Depth First Search)
# =======

#struktur data untuk membuat antrian, menggunakan library collections bawaan python yaitu deque (double ended queue)

from collections import deque
from platform import node


#representasi graph
graph ={
    'A': ['B', 'C'],
    'B': ['D', 'E',],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []

}

def dfs(graph, node, visited=None):
#fungsi untuk melakukan penelusuran graph menggunakan DFS 
#graph : dictionary yang menyimpan graph
#node : menyimpan node yang sedang dikunjungi
#visited : menyimpan node yang sudah dikunjungi

    #tandai node saat ini sebagai sudah dikunjungi
    visited.add(node)

    #tampilkan node yang sedang dikunjungi
    print(node, end=" ")

        #periksa semua tetangga dari node saat ini 
    for neighbor in graph [node]:
        #jika tetangga belum dikunjungi
        if neighbor not in visited:
            #panggil fungsi DFS secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)
            #tandai sebagai sudah dikunjungi
            #visited.add(neighbor)

#menjalankan DFS dari graph A
#set untuk menyimpan node yang sudah dikunjungi
visited = set() 
dfs(graph, 'A', visited)

            