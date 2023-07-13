# User-defined function untuk menentukan jenis bacaan paling disukai
def jenisBuku(jumlBuku):
    jenis = ["Buku cerita", "Buku latihan", "Buku rujukan"]
    jumlTertinggi = max(jumlBuku)
    indeksTertinggi = jumlBuku.index(jumlTertinggi)
    return jenis[indeksTertinggi]


# Menyimpan nama pelajar
nama = ["Aimi", "Aru", "Lee"]

# Menyimpan jumlah perbelanjaan
murid1 = [12, 15, 33]
murid2 = [10, 12, 15]
murid3 = [15, 18, 0]

# Mengira jumlah perbelanjaan keseluruhan
jumlKeseluruhan = sum(murid1) + sum(murid2) + sum(murid3)

# Mengira jumlah perbelanjaan mengikut jenis buku
jumlBuku1 = murid1[0] + murid2[0] + murid3[0]
jumlBuku2 = murid1[1] + murid2[1] + murid3[1]
jumlBuku3 = murid1[2] + murid2[2] + murid3[2]

jumlBuku = [jumlBuku1, jumlBuku2, jumlBuku3]

# Memaparkan hasil dapatan
print("Murid membelanjakan RM", jumlKeseluruhan, "utk semua jenis buku")

print("Murid membelanjakan RM", jumlBuku1, "utk Buku cerita")
print("Murid membelanjakan RM", jumlBuku2, "utk Buku latihan")
print("Murid membelanjakan RM", jumlBuku3, "utk Buku rujukan")

print("Buku yang paling disukai oleh murid sekolah ialah", jenisBuku(jumlBuku))
