#===========================================
# latihan 1 : membuat node
#===========================================


#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat root
root = Node("A")

#menampilkan isi node
print("data pada root : ", root.data)
print("data kiri root : ", root.left)
print("data kanan root : ", root.right)

#penjelasan setiap proses :
# membuat satu node sebagai root dengan isi "A"
# Saat node dibuat, otomatis child kiri (left) dan kanan (right)
# masih kosong (None), karena belum diisi node lain

# Lalu program menampilkan data yang ada di root
# yaitu "A"

# Setelah itu, program juga menampilkan child kiri dan kanan dari root
# Karena belum ada node tambahan, maka nilainya masih None

# Jadi outputnya:
# data pada root : A
# data kiri root : None
# data kanan root : None