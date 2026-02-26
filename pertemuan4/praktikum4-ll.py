#===============================================
# nama  : Cinta Asih Salaamina
# NIM   : J0403251045
#===============================================
#implementasi Dasar : node pada linked list
#===============================================

class Node:
    def __init__(self, data): #konstruktor untuk inisialisasi node
        self.data = data #menyimpan nilai / data
        self.next = None #pointer ke note berikutnya

#1. membuat node satu per satu 
nodeA = Node("A") #membuat node dengan data "A"
nodeB = Node("B") #membuat node dengan data "B"
nodeC = Node("C") #membuat node dengan data "C"

#2. menghubungkan node-node tersebut
nodeA.next = nodeB #nodeA menunjuk ke nodeB
nodeB.next = nodeC #nodeB menunjuk ke nodeC

#3. menentukan node pertama(head)
head = nodeA #nodeA adalah head dari linked list

#4. traversial : menelusuri dari head sampai none
current = head #mulai dari head
while current is not None: #selama current tidak None
    print(current.data) #cetak data pada node saat ini
    current = current.next #pindah ke node berikutnya


#===============================================
#implementasi Dasar : linked list + insert awal
#===============================================

class LinkedList:
    def __init__(self): #konstruktor untuk inisialisasi linked list
        self.head = None #head awalnya None (linked list kosong)

    def insert_awal (self, data): #method untuk insert di awal linked list
        #1. buat node baru 
        nodeBaru = Node(data) #buat node baru dengan data yang diberikan

        #2. node baru menunjuk ke head lama
        nodeBaru.next = self.head #node baru menunjuk ke head saat ini

        #3. head pindah ke node baru
        self.head = nodeBaru #head sekarang menjadi node baru


        def hapus_awal(self): #method untuk menghapus node di awal linked list
            data_terhapus = self.head.data #simpan data yang akan dihapus
            self.head = self.head.next #head pindah ke node berikutnya       

        def tampilkan(self): #method untuk menampilkan isi linked list
            current = self.head #mulai dari head
            while current is not None: #selama current tidak None
                print(current.data) #cetak data pada node saat ini
                current = current.next #pindah ke node berikutnya


ll = LinkedList() #instantiasi objek ke class liked list
ll.insert_awal("X") #insert "X" di awal linked list
ll.tampilkan() #tampilkan isi linked list
ll.hapus_awal() #hapus node di awal linked list
ll.tampilkan() #tampilkan isi linked list setelah penghapusan
