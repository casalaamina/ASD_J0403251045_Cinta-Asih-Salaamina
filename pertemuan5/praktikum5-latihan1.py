#===================================================================================
#Nama : Cinta Asih S
#NIM : J0403251045
#Kelas : B2
#===================================================================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================
def pangkat(a, n):
    # Fungsi rekursif untuk menghitung a pangkat n (a^n)
    # a: bilangan pokok
    # n: pangkat (eksponen)

    # Base case: jika n == 0, maka hasilnya 1 (karena a^0 = 1)
    if n == 0:
        return 1  # Mengembalikan 1 jika sudah mencapai pangkat 0

    # Recursive call: kalikan a dengan hasil pangkat(a, n-1)
    # Setiap pemanggilan rekursif akan mengurangi n hingga mencapai base case
    return a * pangkat(a, n - 1)

# Contoh pemanggilan fungsi pangkat
# Akan menghitung 2^4 = 2*2*2*2 = 16
print(pangkat(2, 4)) # Output: 16

# Penjelasan alur program:
# 1. Fungsi pangkat dipanggil dengan a=2, n=4.
# 2. Karena n != 0, maka dilakukan rekursi: 2 * pangkat(2, 3)
# 3. pangkat(2, 3) memanggil 2 * pangkat(2, 2)
# 4. pangkat(2, 2) memanggil 2 * pangkat(2, 1)
# 5. pangkat(2, 1) memanggil 2 * pangkat(2, 0)
# 6. pangkat(2, 0) mencapai base case, mengembalikan 1
# 7. Hasil rekursi: 2*2*2*2*1 = 16
