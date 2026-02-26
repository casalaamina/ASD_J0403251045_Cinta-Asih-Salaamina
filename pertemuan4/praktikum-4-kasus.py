#===================================================================================
#Nama : Cinta Asih S
#NIM : J0403251045
#Kelas : 
#===================================================================================

#===================================================================================
#Studi Kasus : Sistem Antrian Layanan Akademik
#Implementasi Queue =>
# Enqueue (tambah data ke antrian) : Memindahkan pointer rear
# Dequeue (hapus data dari antrian) : memindahkan pointer front
# Stack ==> Front -> B -> A -> None
# Front-> A > B >  C  ->Rear

#===================================================================================

#1. Mendefinisikan node (unit dasar linked list)
class node:
    def __init__(self,nim,nama):
        self.nim = nim    #Menyimpan NIM mahasiswa
        self.nama = nama  #menyimpan nama mahasiswa
        self.next = None   #pointer ke node berukutnya

#2. mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None  #pointer ke node paling depan
        self.rear = None   #pointer ke node paling belakang

    def is_empty(self):
        #ketika queue kosong maka front = rear = None
        return self.front is None  #mengembalikan True jika antrian kosong
    
    #menambahkan data baru ke bagian belakang (rear)
    def enqueue(self,nim,nama):
        #membuat node baru dengan data nim dan nama
            new_node = node(nim, nama)
            if self.is_empty():
                #jika antrian kosong, maka front dan rear menunjuk ke node baru
                self.front = new_node
                self.rear = new_node
                return

            self.rear.next = new_node
            self.rear = new_node

    #menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):

        if self.is_empty():
            print("Antrian kosong, tidak ada data untuk dihapus.")
            return None

        #lihat data bagian front, simpan di variable data
        node_dilayani = self.front

        #geser pointer front ke next front 
        self.front = self.front.next

        #jika front menjadi none (data antrian terakhir yang dilayani)
        if self.front is None:
            self.rear = None  #set rear juga ke None karena antrian kosong

        return node_dilayani

    def tampilkan(self):
        print("Daftar Antrian Mahasiswa (front -> rear) :")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. NIM: {current.nim}, Nama: {current.nama}")
            current = current.next
            no += 1

#===================================================================================
#Program utama
def main():
    #instantiasi queue akademik
    q = queueAkademik()

    while True:
        print("\nMenu Layanan Akademik:")
        print("1. Tambah Antrian")
        print("2. Layani Antrian")
        print("3. Tampilkan Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            nim = input("Masukkan NIM mahasiswa: ")
            nama = input("Masukkan nama mahasiswa: ")
            q.enqueue(nim, nama)
            print(f"Antrian untuk {nama} (NIM: {nim}) telah ditambahkan.")
        
        elif pilihan == '2':
            mahasiswa_dilayani = q.dequeue()
            if mahasiswa_dilayani:
                print(f"Memberikan layanan kepada {mahasiswa_dilayani.nama} (NIM: {mahasiswa_dilayani.nim}).")
        
        elif pilihan == '3':
            q.tampilkan()
        
        elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem antrian layanan akademik.")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()