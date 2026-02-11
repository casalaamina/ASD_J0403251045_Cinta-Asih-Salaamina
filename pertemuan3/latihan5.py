class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self, prefix="Linked List"):
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print(f"{prefix}: {'->'.join(elements)}->null")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        
        while current is not None:
            next_node = current.next 
            
            current.next = prev
            
            prev = current
            current = next_node
            
        self.head = prev

#contoh tampilan ke latihan 5
print("\n--- Latihan 5: Membalik Single Linked List ---")

#contoh 1-------
ll1 = LinkedList()
data_list_1 = [1, 2, 3, 4, 5]
for d in data_list_1:
    ll1.insert_at_end(d)
    
ll1.display("Linked List sebelum dibalik")
ll1.reverse()
ll1.display("Linked List setelah dibalik")

print("-" * 20)

#contoh ke 2
ll2 = LinkedList()
data_list_2 = [10, 20, 30, 40]
for d in data_list_2:
    ll2.insert_at_end(d)

ll2.display("Linked List sebelum dibalik")
ll2.reverse()
ll2.display("Linked List setelah dibalik")

print("-" * 20)

#cnth ke 3 
ll3 = LinkedList()
ll3.insert_at_end(7)

ll3.display("Linked List sebelum dibalik")
ll3.reverse()
ll3.display("Linked List setelah dibalik")