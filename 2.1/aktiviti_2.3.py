print("Lakukan ujian matematik")
markah = int(input("Masukkan markah anda"))

jumlah = 0
if markah < 85:
    for ulang in range(1, 3+1):
        print("Ulangi ujian matematik")
        markah = int(input("Masukkan markah anda"))
        jumlah = jumlah + markah
        if markah >= 85:
            purata = jumlah / ulang
            break

print(purata)
