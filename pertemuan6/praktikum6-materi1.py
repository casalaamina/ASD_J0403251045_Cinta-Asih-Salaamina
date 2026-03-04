#==
# Nama : Cinta Asih Salaamina
# NIM : J0403251045
# Kelas : B2
#==

#== 
# insertion sort (Ascending)
#==

def insertion_sort(data):
    #loop mulai dari data ke 2 (index arrary ke 1)
    for i in range(1, len(data)):
        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri
        
        #geser
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        #sisipkan key pada posisi yang benar
        data[j + 1] = key
    return data

angka = [7,8,5,2,4,6]
print("Hasil Sorting: ", insertion_sort(angka)) # Output: [2, 4, 5, 6, 7, 8]