""" User-defined function yang memeulangkan nombor besar di kiri
dan nombor kecil di kanan """


def besar_kecil(x, y):
    if x > y:
        return x, y
    else:
        return y, x


# Bahagian utama atur cara
# Minta pengguna memasukkan dua nombor
a = int(input("Masukkan nombor integer yang pertama: "))
b = int(input("Masukkan nombor integer yang kedua: "))

# Panggilan user-defined function
[besar, kecil] = besar_kecil(a, b)
print("Nombor", besar, "lebih besar daripada", kecil)
