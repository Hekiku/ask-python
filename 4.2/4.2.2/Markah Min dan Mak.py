# Menyimpan markah setiap murid dalam senarai
murid_1 = [87, 70, 80, 78]
murid_2 = [95, 80, 65, 75]
murid_3 = [74, 85, 90, 85]
murid_4 = [55, 85, 71, 68]
murid_5 = [65, 78, 68, 65]

# Menyimpan nama setiap murid dalam urutan senarai nama
nama = ["Ali bin Azmi", "Aminah binti Yusof", "Chong Yee Ling", "Dayana Minsu",
        "Denish A/L Kathigasu"]

# Menjumlahkan markah setiap murid
jumlah_1 = sum(murid_1)
jumlah_2 = sum(murid_2)
jumlah_3 = sum(murid_3)
jumlah_4 = sum(murid_4)
jumlah_5 = sum(murid_5)

# Menyimpan jumlah markah setiap murid dalam senarai jumlah
jumlah = [jumlah_1, jumlah_2, jumlah_3, jumlah_4, jumlah_5]

# Mencari markah tertinggi dan terendah dalam senarai jumlah
tertinggi = max(jumlah)
terendah = min(jumlah)

# Menggunakan sub-function untuk mencari indeks
indeks_tertinggi = jumlah.index(tertinggi)
indeks_terendah = jumlah.index(terendah)

# Menggunakan sub-function untuk mencari nama murid
murid_tertinggi = nama[indeks_tertinggi]
murid_terendah = nama[indeks_terendah]

# Mencetak nama beserta markah tertinggi dan terendah
print(murid_tertinggi, "memperoleh jumlah markah tertinggi, iaitu", tertinggi)
print(murid_terendah, "memperoleh jumlah markah terendah, iaitu", terendah)
