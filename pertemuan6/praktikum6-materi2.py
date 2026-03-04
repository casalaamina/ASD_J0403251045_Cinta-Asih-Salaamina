#==
# Nama : Cinta Asih Salaamina
# NIM : J0403251045
# Kelas : B2
#==

#== 
# insertion sort (Ascending)
#==

def insertion_sort(data):

     #melihat data awal
    print("data awal: ", data)
    print("-"*50)
        
    #loop mulai dari data ke 2 (index arrary ke 1)
    for i in range(1, len(data)):

        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri

        print("Iterasi Ke-", i)
        print("Nilai key = ", key)
        print("Bagian Kiri (terurut): ", data[:i])
        print("Bagian Kanan (belum terurut): ", data[i:])
        print("-"*50)


        #geser
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        #sisipkan key pada posisi yang benar
        data[j + 1] = key

        print("Setelah disisipkan: ", data)
        print("-"*50)

    return data

angka = [7,8,5,2,4,6]
print("Hasil Sorting: ", insertion_sort(angka)) # Output: [2, 4, 5, 6, 7, 8]