#===========================================
# latihan 4 : membuat traversal inorder
#===========================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan


#fungsi inorder : left ==> root ==> right
def inorder(node):
    if node is not None:
        inorder(node.left) #traversal ke child kiri
        print(node.data, end=" ") #menampilkan data node
        inorder(node.right) #traversal ke child kanan


#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan traversal inorder
print("inorder traversal : ", end="")
inorder(root)


#penjelasan setiap proses :
# Traversal inorder dimulai dari root A
# Karena aturan inorder itu (kiri → root → kanan)
# program bakal jalan ke kiri dulu dari A, yaitu ke B
# Dari B, lanjut lagi ke kiri ke D
# D ini tidak punya anak, jadi langsung ditampilkan dulu (D)
# Setelah itu balik ke B, lalu B ditampilkan
# Habis itu lanjut ke kanan dari B, yaitu ke E
# E juga tidak punya anak, jadi langsung ditampilkan (E)
# Setelah semua bagian kiri dari A selesai
# balik ke A dan tampilkan A
# Terakhir, lanjut ke kanan dari A yaitu ke C
# C juga tidak punya anak, jadi langsung ditampilkan
# Jadi urutan akhirnya adalah: D B E A C