class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # latihan 1: fungsi untuk menghapus node berdasarkan nilai (key)
    def delete_node(self, key):
        temp = self.head
        
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # kalo key gak ditemukan (temp is None) klo gk slh 
        if temp is None:
            print(f"Elemen {key} tidak ditemukan.")
            return

        prev.next = temp.next
        temp = None 
        print(f"Elemen {key} berhasil dihapus.")

# contoh penggunaan latihan 1
print("--- Latihan 1: Menghapus Node Berdasarkan Nilai ---")
ll = LinkedList()
ll.insert_at_end(3)
ll.insert_at_end(7)
ll.insert_at_end(12)
ll.insert_at_end(19)
ll.insert_at_end(25)

print("Linked List Awal:")
ll.display() # outputnya: 3 -> 7 -> 12 -> 19 -> 25 -> null

# apus elemen 12 ( ygtengah???)
ll.delete_node(12)
print("Setelah hapus 12:")
ll.display() # Output: 3 -> 7 -> 19 -> 25 -> null

# apus elemen 3 (awal)
ll.delete_node(3)
print("Setelah hapus 3:")
ll.display() # Output: 7 -> 19 -> 25 -> null

# apus elemen 25 (yg akhir)
ll.delete_node(25)
print("Setelah hapus 25:")
ll.display() # Output: 7 -> 19 -> null

# cobaAAAAAAA hapus elemen yang gak ada
ll.delete_node(100)