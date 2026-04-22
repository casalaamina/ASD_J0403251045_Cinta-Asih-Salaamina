# ==========================================================
# Latihan 6: Traversal AVL Tree
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1   # AVL butuh height buat ngecek keseimbangan


def getHeight(node):
    if not node:
        return 0
    return node.height


def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)


def rightRotate(z):
    y = z.left
    T3 = y.right

    # rotasi
    y.right = z
    z.left = T3

    # update height
    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    return y


def leftRotate(z):
    y = z.right
    T2 = y.left

    # rotasi
    y.left = z
    z.right = T2

    # update height
    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    return y


def insert(root, data):
    # insert biasa kayak BST
    if not root:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    # update height
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))

    # cek balance
    balance = getBalance(root)

    # kasus LL
    if balance > 1 and data < root.left.data:
        return rightRotate(root)

    # kasus RR
    if balance < -1 and data > root.right.data:
        return leftRotate(root)

    # kasus LR
    if balance > 1 and data > root.left.data:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # kasus RL
    if balance < -1 and data < root.right.data:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root


# traversal preorder
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# ================= PROGRAM UTAMA =================
root = None

data_list = [10, 20, 30, 40, 50, 25]

for data in data_list:
    root = insert(root, data)

print("Preorder AVL:")
preorder(root)



# ================= PENJELASAN KODE =================
# gabungin semua konsep, dari insert avl, rottasi dan traversal 
# pertama bikin class Node, sama kayak BST, tapi ditambah height lagi???
# buat ngecek keseimbangan nantinya
# data dimasukin satu  satu
# tiap insert langsung dicek balance nya
# kalo miring, langsung dirotasi
# jadi tree nya tetep seimbang
# terakhir pake preorder buat nampilin isi tree
# biar keliatan struktur hasil balancing nya
# beda sama BST biasa,
# ini gak bakal jadi lurus ke kanan/kiri
# karena selalu dibenerin sama rotasi