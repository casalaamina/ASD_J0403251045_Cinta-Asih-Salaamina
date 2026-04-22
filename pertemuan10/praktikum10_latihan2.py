# ==========================================================
# Latihan 4: Membuat BST yang Tidak Seimbang
# ==========================================================

# Class Node untuk menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data # nilai pada node
        self.left = None # child kiri
        self.right = None # child kanan

# Fungsi insert untuk BST
def insert(root, data):
    # Jika root kosong, buat node baru
    if root is None:
        return Node(data)
    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)
    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

# Fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# -----------------------------
# Program utama
# -----------------------------

root = None

# Data dimasukkan berurutan naik
data_list = [10, 20, 30]
for data in data_list:
    root = insert(root, data)
print("Preorder BST:")
preorder(root)
print("\n\nStruktur BST:")
tampil_struktur(root)

# ==================================

# ================= PENJELASAN KODE =================
# awalna bikin class Node dulu buat nyimpen data
# tiap node punya data, sama pointer ke kiri dan kanan
# terus ada fungsi insert
# fungsinya buat masukin data ke BST sesuai aturan
# kalo root masih kosong, langsung bikin node baru
# kalo data lebih kecil dari root, masukkin datanya ke kiri
# kalo lebih besar, masukin datanya ke kannan
# dia bakal terus manggil dirinya sendiri
# sampe nemu posisi kosong buat naro data
# di bagian program utama
# memasukin data [10, 20, 30] satu-satu
# karena urut naik, tiap data selalu lebih besar dari sebelumnya
# jadi selalu masuk ke kanan terus
# makanya hasil akhirnya jadi gak seimbang
# bentuknya lurus ke kanan semua
