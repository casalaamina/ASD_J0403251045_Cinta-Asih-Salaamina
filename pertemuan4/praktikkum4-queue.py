#===============================================
# nama  : Cinta Asih Salaamina
# NIM   : J0403251045
#===============================================
#implementasi Dasar : queue
#===============================================

class node:
    def __init__(self, data): #konstruktor untuk inisialisasi node
        self.data = data #menyimpan nilai / data
        self.next = None #pointer ke note berikutnya

#queue dengan 2 pointerfront and rear

    class QueueLL:
        def __init__(self):
            self.front = none
            self.rear = none


            if sel.front = 

            def enqueue(self,data):
                #menambah data di belakang (rear)
                nodeBaru = node(data)

                if self.is_empty():
                    self.front = nodeBaru
                    self.rear = nodeBaru
                    return
                    
                self.rear.next= nodeBaru
                self.rear = nodeBaru

                def tampilkan(self):
                    current = self.front
                    print("Front -> ", end="")
                    while current is not None:
                        print(current.data, end=" -> ")
                        current = current.next
                    print("None")


#instantiasi objek class queueLL
q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()