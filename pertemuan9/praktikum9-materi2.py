#===========================================
# latihan 2 : membuat node
#===========================================


#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menampilkan isi node
print("data pada root : ", root.data)
print("data kiri root : ", root.left.data)
print("data kanan root : ", root.right.data)
print("data kiri root : ", root.left.left.data)
print("data kanan root : ", root.left.right.data)    

#Lanjutkan 
#penjelasan setiap proses :
# Program ini membuat struktur tree sederhana dengan root "A"

# Pertama, dibuat root dengan isi "A"
# Lalu ditambahkan child level 1
# - kiri root = "B"
# - kanan root = "C"

# Setelah itu ditambahkan child level 2
# - kiri dari B = "D"
# - kanan dari B = "E"

# Selanjutnya program menampilkan isi tiap node

# print pertama menampilkan data root, yaitu A
# print kedua menampilkan child kiri root, yaitu B
# print ketiga menampilkan child kanan root, yaitu C

# print keempat menampilkan child kiri dari B, yaitu D
# print kelima menampilkan child kanan dari B, yaitu E

# Semua data berhasil ditampilkan karena node-nya memang sudah dibuat.
# Jadi outputnya:
# data pada root : A
# data kiri root : B
# data kanan root : C
# data kiri root : D
# data kanan root : E