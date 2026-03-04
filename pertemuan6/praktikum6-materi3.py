#==
# Nama : Cinta Asih Salaamina
# NIM : J0403251045
# Kelas : B2
#==

#== 
# Merge sort (Ascending)
#==

def merge_sort(data):
    # base case
    if len(data) <= 1:
        return data

    # divide
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    # recursive call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    i = 0
    j = 0

    # membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # menambahkan sisa
    result.extend(left[i:])
    result.extend(right[j:])

    return result


angka = [13, 7, 28, 5, 19, 36, 4]
print("Hasil Sorting:", merge_sort(angka))