class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node

    def display_forward(self):
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        return ", ".join(elements)


    def search(self, key):
        temp = self.head
        is_found = False
        
        while temp:
            if temp.data == key:
                is_found = True
                break
            temp = temp.next
            
        if is_found:
            print(f"Elemen {key} ditemukan dalam Doubly Linked List.")
            return True
        else:
            print(f"Elemen {key} tidak ditemukan dalam Doubly Linked List.")
            return False

print("\n--- Latihan 3: Pencarian pada Doubly Linked List ---")
dll = DoublyLinkedList()

data_list_1 = [2, 6, 9, 14, 20]
for d in data_list_1:
    dll.insert_at_end(d)
    
print(f"Masukkan elemen ke dalam Doubly Linked List: {dll.display_forward()}")
print("Masukkan elemen yang ingin dicari: 9")
dll.search(9)

print("\nMasukkan elemen yang ingin dicari: 50")
dll.search(50)

dll_empty = DoublyLinkedList()
print("\nMasukkan elemen ke dalam Doubly Linked List: (Tidak ada elemen)")
print("Masukkan elemen yang ingin dicari: 10")
if not dll_empty.head:
    print("Doubly Linked List kosong. Tidak ada elemen yang bisa dicari.")

#harusnya udh bener sih.........