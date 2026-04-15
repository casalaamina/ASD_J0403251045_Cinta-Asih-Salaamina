#===========================================
# latihan 5 : membuat traversal postorder
#===========================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan


#fungsi postorder : left ==> right ==> root
def postorder(node):
    if node is not None:
        postorder(node.left) #traversal ke child kiri
        postorder(node.right) #traversal ke child kanan
        print(node.data, end=" ") #menampilkan data node

#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan traversal postorder
print("postorder traversal : ", end="")
postorder(root)

#penjelasan setiap proses :
# Traversal postorder dimulai dari root A
# Karena aturan postorder itu (kiri → kanan → root)
# program bakal ke kiri dulu dari A, yaitu ke B
# Dari B, lanjut ke kiri ke D
# D tidak punya anak kiri maupun kanan
# jadi langsung ditampilkan dulu (D)
# Setelah itu balik ke B, lalu ke kanan yaitu E
# E juga tidak punya anak, jadi langsung ditampilkan (E)
# Setelah kiri dan kanan B selesai
# baru B ditampilkan
# Lanjut ke kanan dari A, yaitu ke C
# C tidak punya anak, jadi langsung ditampilkan (C)
# Terakhir, setelah semua selesai
# kembali ke A dan tampilkan A
# Jadi urutan akhirnya adalah: D E B C A