#==
# Nama : Cinta Asih Salaamina
# NIM : J0403251045
# Kelas : B2
#==

#===================================================================================
#Merge Sort (ascending)
#===================================================================================

def merge_sort(data, depth=0):

    indent=" " * depth
    print(f"{indent}merge_sort({data})")

    if len(data) <= 1: 
        return data
    
    #Divide : memabgi data menjadi 2 bagian
    mid = len(data)//2 #membagi data menjadi 2 bagian
    left = data[:mid] #slicing bagian kiri
    right = data[mid:] #slicing bagian kanan

    print(f"{indent}divide: {data} => {left} | {right}")

    #recursive call 
    left_sorted = merge_sort(left, depth + 1)
    right_sorted = merge_sort(right, depth + 1)

    merged = merge(left_sorted, right_sorted)
    print(f"{indent}merge({left_sorted}, {right_sorted}) => {merged}")

    return merge(left_sorted, right_sorted)

def merge(left,right):

    result = []
    i= 0
    j= 0

    #membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Menambahkan elemen yang tersisa
    result.extend(left[i:])
    result.extend(right[j:])

    return result

angka = [13,7,28,5,19,36,4]
print("Hasil Sorting: ", merge_sort(angka))

