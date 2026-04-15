#===========================================
# latihan 6 : Struktur Organisasi Perusahaan
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
        preorder(node.right) #traversal ke child kanande

#membuat sebuah node root
root = Node("Direktur")

#membuat child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#membuat child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")
root.right.right = Node("Staff 3")

#menjalankan traversal preorder
print("Struktur Organisasi (preorder) : ", end="")
preorder(root)

#penjelasan setiap proses :
# Traversal preorder dimulai dari root yaitu Direktur
# Karena aturan preorder itu (root → kiri → kanan)
# jadi yang pertama langsung ditampilkan adalah Direktur
# Setelah itu, program lanjut ke kiri dari Direktur yaitu Manajer A
# Manajer A langsung ditampilkan
# Lalu lanjut ke kiri dari Manajer A yaitu Staff 1
# Staff 1 tidak punya anak, jadi langsung ditampilkan
# Kembali ke Manajer A, lalu ke kanan yaitu Staff 2
# Staff 2 juga tidak punya anak, jadi langsung ditampilkan
# Setelah bagian kiri dari Direktur selesai
# program lanjut ke kanan yaitu Manajer B
# Manajer B langsung ditampilkan
# Dari Manajer B, tidak ada child kiri
# jadi langsung ke kanan yaitu Staff 3
# Staff 3 ditampilkan karena tidak punya anak
# Jadi urutan akhirnya adalah
# Direktur Manajer A Staff 1 Staff 2 Manajer B Staff 3