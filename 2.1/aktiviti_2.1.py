jumlah_jualan = int(input("Masukkan jumlah jualan bulan ini: "))

if jumlah_jualan < 400:
    komisen = 7 / 100
elif jumlah_jualan < 750:
    komisen = 10 / 100
elif jumlah_jualan < 1000:
    komisen = 12.5 / 100
else:
    komisen = 16 / 100

jumlah_komisen = komisen * jumlah_jualan
print("Jumlah komisen diterima: RM {:.2f}".format(jumlah_komisen))

