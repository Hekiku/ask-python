# User-defined function untuk menentukan baki
def jumlBaki(jumlah, amaun):
    baki = amaun - jumlah
    return baki


# User-define function untuk menentukan pulangan duit kertas
def pulanganK(baki, duit):
    jumlduit = baki // duit
    if jumlduit != 0:
        print("RM", duit, ":", int(jumlduit))
        baki = baki - duit*jumlduit
    return baki


# User-define function untuk menentukan pulangan duit syiling
def pulanganS(baki, duit):
    jumlduit = baki // duit
    if jumlduit != 0:
        print(duit, "sen :", int(jumlduit))
        baki = baki - duit*jumlduit
    return baki


# Atur cara utama
print(" " * 10 + "Kedai Runcit Pak Cik Sairin" + " " * 10)
terus = 0
jumlah = 0
while terus != "T":
    print("Teruskan atau Masukkan T untuk mendapatkan JUMLAH:")
    harga = input("Masukkan amaun: ")
    if harga == "T" or harga == "t":
        terus = "T"
    else:
        jumlah = jumlah + float(harga)

print("\nJumlah belian: RM", "%.2f" % jumlah)
amaun = float(input("Masukkan amaun diterima: "))
baki = jumlBaki(jumlah, amaun)

print("*" * 35)

print("Terima (RM):", "%.2f" % amaun)
print("Jumlah belian (RM):", "%.2f" % jumlah)
print("Baki (RM):", "%.2f" % baki)

print("\nPulangkan......")
print("*" * 35)

# Mengira bilangan wang kertas untuk setiap nilai
for duit in [50, 20, 10, 5, 1]:
    baki = pulanganK(baki, duit)

baki = baki * 100  # Menukarkan baki kepada sen sahaja

# Membundarkan nilai sen kepada 5 sen terdekat
if baki % 10 < 3:
    baki = baki // 10 * 10
elif baki % 10 > 7:
    baki = (baki // 10 + 1) * 10
else:
    baki = baki // 10 * 10 + 5

# Mengira bilangan wang syiling untuk setiap nilai
for duit in [50, 20, 10, 5]:
    baki = pulanganS(baki, duit)

print("*" * 35)
