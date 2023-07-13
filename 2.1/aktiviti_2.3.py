print("Lakukan ujian matematik")
markah = int(input("Masukkan markah anda: "))

jumlah = markah
bil_ujian = 1
if markah < 85:
    for ulang in range(3):
        print("Ulangi ujian matematik")
        markah = int(input("Masukkan markah anda: "))
        jumlah = jumlah + markah
        bil_ujian += 1
        if markah >= 85:
            break

purata = jumlah / (bil_ujian)
print("\nMarkah anda untuk ujian:", purata)

