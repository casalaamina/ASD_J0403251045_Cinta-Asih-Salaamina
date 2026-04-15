#===========================================
# latihan 3 : membuat traversal preorder
#===========================================



#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#fungsi preorder : rott ==> left ==> right
def preorder(node):
    if node is not None:
        print(node.data, end=" ") #menampilkan data node
        preorder(node.left) #traversal ke child kiri
        preorder(node.right) #traversal ke child kanan

#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan traversal preorder
print("preorder traversal : ", end="")
preorder(root)


#penjelasan setiap proses :
# Traversal preorder dimulai dari root yaitu A
# Karena aturan preorder itu (root → kiri → kanan)
# maka A langsung ditampilkan terlebih dahulu

# Setelah itu, program lanjut ke kiri dari A yaitu B
# B langsung ditampilkan

# Dari B, lanjut ke kiri yaitu D
# D tidak punya child, jadi langsung ditampilkan

# Kembali ke B, lalu ke kanan yaitu E
# E juga tidak punya child, jadi langsung ditampilkan

# Setelah bagian kiri dari A selesai
# program lanjut ke kanan yaitu C
# C tidak punya child, jadi langsung ditampilkan

# Jadi urutan akhirnya;
# A B D E C