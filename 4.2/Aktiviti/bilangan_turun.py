def bilanganturun(simbol):
    bil_baris = 1
    while bil_baris < 10:
        print(simbol*bil_baris)
        bil_baris = bil_baris + 1


# Atur cara utama
aksara = input("Masukkan simbol: ")
bilanganturun("aksara")
