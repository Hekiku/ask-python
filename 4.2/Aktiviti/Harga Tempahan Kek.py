jenis_kek = ["keju", "mentega", "pelangi", "kopi"]
harga_kek = [40, 35, 35, 30]
jumlah = [0, 1, 2, 3]

a = int(input("Masukkan tempahan untuk kek keju: "))
b = int(input("Masukkan tempahan untuk kek mentega: "))
c = int(input("Masukkan tempahan untuk kek pelangi: "))
d = int(input("Masukkan tempahan untuk kek kopi: "))

tempahan = [a, b, c, d]


def jumlah_harga():
    for i in range(4):
        jumlah[i] = harga_kek[i] * tempahan[i]
    return (jumlah)


def cetak():
    print("\n\nTempahan anda ialah:")
    print(a, "kek", jenis_kek[0])
    print(b, "kek", jenis_kek[1])
    print(c, "kek", jenis_kek[2])
    print(d, "kek", jenis_kek[3])
    print("\nJumlah harga untuk tempahan ialah RM", sum(jumlah))


jumlah_harga()
cetak()
