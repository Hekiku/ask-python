print("*** ATUR CARA INI AKAN MENJAN JADUAL SIFIR DARAB ***")
sifir = int(input("Masukkan nombor Jadual Sifir Darab anda: "))
print("Jadual Sifir Darab", sifir, "ialah:")

for i in range(1, 13):
    hasil = i * sifir
    print(i, "x", sifir, "=", hasil)
