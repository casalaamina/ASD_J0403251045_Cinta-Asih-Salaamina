#hehehhehehehehehhehhehe
#praktikkum 1, Konsep ADT dan file handling

#membuka file dan membaca seluruh isi file
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    data = file.read()
print(data)
print("=========================================")
print("type data : ", type(data))
print("jumlah karakter : ", len(data))
print("jumlah baris : ", data.count("\n") + 1)
print("jumlah kata : ", len(data.split()))
print("=========================================")

#membuka file per barisssssss
print("=========================================")
print("membaca file per baris")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris += 1
        baris = baris.strip()
        print("baris ke : ", jumlah_baris)
        print("Isinya : ", baris) 
print("=========================================")

#parsing data berdasarkan karakter pemisah koma
print("=========================================")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nama, nim, nilai = baris.split(",")
        print("NIM : ", nim, "| Nama : ", nama, "| Nilai : ", nilai, "|")

#membaca file dan menyimpan ke list
print("=========================================")
daftar_mahasiswa = []
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        
        #simpan sebagai list " [nim, nama, nilai] "
        daftar_mahasiswa.append([nim,nama,int(nilai)])
print("===== data mahasiswa dalam list =====")
print(daftar_mahasiswa)

print("=== jumlah record dalam list")
print("jumlah record : ", len(daftar_mahasiswa))

print("=== menampilkan data record tertentu ===")
print("contoh menampilkan record ke 0", daftar_mahasiswa[0])


print("=========================================")

data_dict = {}
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file: 
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        #simpan data mahasiswa ke dictionary dengan nim sebagai key
        data_dict[nim] = {                  #key
            "nama": nama,                   #value
            "nilai": int(nilai)             #value
            }
print("===== data mahasiswa dalam dictionary =====")
print(data_dict)

#menghitung nilai tertinggi, terendah, dan rata-rata NYOBAAAAAAA
print("=========================================")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    daftar_nilai = []
    for baris in file:
        baris = baris.strip()
        nama, nim, nilai = baris.split(",")
        daftar_nilai.append(int(nilai))
    print("Daftar Nilai : ", daftar_nilai)
    print("Nilai Tertinggi : ", max(daftar_nilai))
    print("Nilai Terendah : ", min(daftar_nilai))
    print("Rata-rata Nilai : ", sum(daftar_nilai) / len(daftar_nilai))
print("=========================================")
