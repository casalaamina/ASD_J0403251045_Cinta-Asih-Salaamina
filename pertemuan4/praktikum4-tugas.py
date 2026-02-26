# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================

# Kelas Node untuk menyimpan data pelanggan dan pointer ke node berikutnya
class Node:
	def __init__(self, no, nama, servis):
		# Inisialisasi node dengan data pelanggan
		self.no = no
		self.nama = nama
		self.servis = servis
		self.next = None

# Kelas QueueBengkel untuk mengelola antrian menggunakan linked list
class QueueBengkel:
	def __init__(self):
		# Inisialisasi queue dengan front dan rear kosong
		self.front = None
		self.rear = None

	def enqueue(self, no, nama, servis):
		# Tambahkan pelanggan ke antrian (di belakang/rear)
		new_node = Node(no, nama, servis)
		if self.rear is None:
			# Jika antrian kosong, front dan rear menunjuk ke node baru
			self.front = self.rear = new_node
		else:
			# Jika tidak kosong, tambahkan node baru di belakang
			self.rear.next = new_node
			self.rear = new_node
		print(f"Pelanggan dengan No Antrian {no} berhasil ditambahkan.")

	def dequeue(self):
		# Layani pelanggan terdepan (FIFO)
		if self.front is None:
			print("Antrian kosong, tidak ada pelanggan yang dilayani.")
			return
		# Ambil data pelanggan terdepan
		served = self.front
		print(f"Melayani pelanggan: No Antrian: {served.no}, Nama: {served.nama}, Servis: {served.servis}")
		# Geser front ke node berikutnya
		self.front = self.front.next
		# Jika setelah dequeue antrian kosong, rear juga harus None
		if self.front is None:
			self.rear = None

	def tampilkan(self):
		# Tampilkan seluruh data antrian
		if self.front is None:
			print("Antrian kosong.")
			return
		print("\nDaftar Antrian Pelanggan:")
		print("No Antrian | Nama           | Jenis Servis")
		print("------------------------------------------")
		current = self.front
		while current:
			print(f"{current.no:<10} | {current.nama:<14} | {current.servis}")
			current = current.next

# Fungsi utama untuk menjalankan menu interaktif
def main():
	q = QueueBengkel()
	while True:
		print("\n=== Sistem Antrian Bengkel ===")
		print("1. Tambah Pelanggan")
		print("2. Layani Pelanggan")
		print("3. Lihat Antrian")
		print("4. Keluar")
		pilih = input("Pilih menu: ")
		if pilih == "1":
			no = input("No Antrian : ")
			nama = input("Nama : ")
			servis = input("Servis : ")
			q.enqueue(no, nama, servis)
		elif pilih == "2":
			q.dequeue()
		elif pilih == "3":
			q.tampilkan()
		elif pilih == "4":
			print("Terima kasih telah menggunakan sistem antrian bengkel.")
			break
		else:
			print("Pilihan tidak valid")

# Program utama dijalankan di sini
if __name__ == "__main__":
	main()
