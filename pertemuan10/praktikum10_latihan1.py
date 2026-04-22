# ==========================================
# latian 1 : BST
# ========================================== 

# 
# 
# 

class Node:
    def __init__(self, data):
        self.data = data # buat nyimpen nilai data di node
        self.left = None # buat nyimpen child kiri (yg awalnya kosong)
        self.right = None # buat nyimpen child kanan (yg awalnya kosong)

def insert(root, data):
    # kalo root kosong, buat node baru
    if root is None:
        return Node(data)
    
    # Jika data lebih kecil → ke kiri
    if data < root.data:
        root.left = insert(root.left, data)
    # Jika data lebih besar → ke kanan
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

root = None

data_list = [50, 30, 70, 20, 40, 60, 80]

for data in data_list:
    root = insert(root, data) # ini insert/masukkin data satu-satu ke treenya

print(" bst berhasil dibuat")

#penjelasan (kalo lupa dan gak paham)
# awalnya bikin root, yg isinya kosong
# nanti data bakalan masuk satu-satu, daru list
# pertama masuk 50, karena root masih kosong, jadi 50 jadi root
# terus masuk 30, karena 30 < 50, jadi masuk ke kiri root,
# terus masuk 70, karena 70 > 50, jadi masuk ke kanan root
# terus masuk 20, karena 20 < 50, jadi ke kiri root, terus
# dan seterusnya, nanti bakal terbentuk tree sesuai aturan BST

#BST selalu jaga aturan???
# kiri < root < kanan
# root ditengah

# ==========================================================
# Latihan 2: Traversal Inorder
# ==========================================================

from praktikum10_latihan1 import root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print("Hasil inorder:")
inorder(root)
print()

# ==========================================================
# Search pada BST
# ==========================================================

def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)
# Uji pencarian
key = 10
if search(root, key):
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")

    