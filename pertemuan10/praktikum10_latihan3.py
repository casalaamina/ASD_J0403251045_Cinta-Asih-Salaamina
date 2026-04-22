# ==========================================================
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
# ==========================================================
# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Fungsi preorder untuk melihat isi tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# Fungsi rotasi kiri
def rotate_left(x):
    # x adalah root lama
    y = x.right # y adalah child kanan x
    T2 = y.left # subtree kiri milik y disimpan sementara
    
    # Proses rotasi
    y.left = x # x menjadi child kiri dari y
    x.right = T2 # child kanan x diganti dengan T2
    # y menjadi root baru
    return y
# -----------------------------
# Program utama
# -----------------------------
# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)
print("Preorder sebelum rotasi kiri:")
preorder(root)
print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)
# Melakukan rotasi kiri pada root
root = rotate_left(root)
print("\nPreorder sesudah rotasi kiri:")
preorder(root)
print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)

#######################
#penjelasan??????
# pertama masih ada class Node
# tapi sekarang ditambah height (tinggi node)
# buat ngecek keseimbangan
# fungsi height() buat ngambil tinggi node
# kalo node kosong, dianggap 0
# getBalance() buat ngitung selisih tinggi kiri dan kanan
# ini yang nanti dipake buat tau tree nya miring atau engga
# insert() masih mirip BST
# masukin data ke kiri kalo lebih kecil
# ke kanan kalo lebih besar
# bedanya:
# setelah insert, height diupdate
# terus dicek balance nya
# kalo balance > 1 atau < -1
# berarti tree nya gak seimbang
# terus ada 4 kondisi:
# LL (kiri-kiri) -> rotasi kanan
# RR (kanan-kanan) -> rotasi kiri
# LR (kiri-kanan) -> rotasi kiri dulu baru kanan
# RL (kanan-kiri) -> rotasi kanan dulu baru kiri
# rotasi itu intinya kayak muterin posisi node
# biar tree nya balik seimbang lagi
# jadi walaupun data dimasukin urut,
# AVL bakal otomatis ngebenerin strukturnya

#bisa dibilang ini solusi untuk di latihan 4, biar treenya semibang