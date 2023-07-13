def corak(aksara, bilangan):
    print(aksara*bilangan)


def menu():
    print("1. Penyulitan (Encryption)")
    print("2. Nyahsulit (Decryption)")


def mesej():
    teks = input("Masukkan nama anda: ")
    return teks


def songsang(ayat):
    str = " "
    for i in ayat:
        str = i + str
    print("")
    corak("#", len(str))
    print(str)
    corak("#", len(str))


corak("*", 32)
print("Penyulitan / Penyahsulitan Mesej")
print(corak("*", 32))
menu()
print("")
pilihan = (input("Masukkan pilihan anda: "))

if pilihan == 1:
    mesej_asal = input("Masukkan mesej anda: ")
else:
    mesej_sulit = input("Masukkan mesej sulit anda: ")
    songsang(mesej_sulit)
