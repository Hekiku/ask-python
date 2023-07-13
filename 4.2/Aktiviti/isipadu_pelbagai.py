# Procedure menu
def menu():
    print("*" * 35)
    print(" " * 7, "Menu Mengira Isipadu", " " * 7)
    print("*" * 35)
    print("1.  Kuboid")
    print("2.  Silinder")
    print("3.  Kon")
    print("4.  Sfera")
    print("5.  Tamat")
    print("*" * 35)


# User-defined function utk isipadu kuboid
def kuboid(pjg, lebar, tinggi):
    return(pjg * lebar * tinggi)


# User-defined function utk isipadu silinder
def silinder(jejari, tinggi):
    pi = 3.142
    luas = pi * jejari ** 2
    return(luas * tinggi)


# User-defined function utk isipadu kon
def kon(jejari, tinggi):
    pi = 3.142
    luas = pi * jejari ** 2
    return((1 / 3) * luas * tinggi)


# User-defined function utk isipadu sfera
def sfera(jejari):
    pi = 3.142
    return((4 / 3) * pi * jejari ** 3)


# Atur cara utama
run = True
while run:
    menu()
    pilihan = int(input("Masukkan pilihan anda: [1-5] : "))

    if pilihan == 1:
        pjg = int(input("Masukkan panjang : "))
        lebar = int(input("Masukkan lebar : "))
        tinggi = int(input("Masukkan tinggi : "))
        isipadu = kuboid(pjg, lebar, tinggi)
    elif pilihan == 2:
        jejari = int(input("Masukkan jejari : "))
        tinggi = int(input("masukkan tinggi : "))
        isipadu = silinder(jejari, tinggi)
    elif pilihan == 3:
        jejari = int(input("Masukkan jejari : "))
        tinggi = int(input("masukkan tinggi : "))
        isipadu = kon(jejari, tinggi)
    elif pilihan == 4:
        jejari = int(input("Masukkan jejari : "))
        isipadu = sfera(jejari)
    else:
        break

    print("\nIsipadu ialah", round(isipadu, 2), "\n")

print("\nTerima kasih kerana menggunakan saya")
