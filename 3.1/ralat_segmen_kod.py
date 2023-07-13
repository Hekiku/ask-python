# Harga seunit pensel, pen, gunting, pemadam dan pembaris
pensel = 1
pen = 2
gunting = 3
pemadam = 1.5
pembaris = 1.2

# Bilangan pensel, pen, gunting, pemadam dan pembaris dimasukkan oleh pengguna
bil_pensel = int(input("Masukkan bilangan pensel yang diperlukan: "))
bil_pen = int(input("Masukkan bilangan pen yang diperlukan: "))
bil_gunting = int(input("Masukkan bilangan gunting yang diperlukan: "))
bil_pemadam = int(input("Masukkan bilangan pemadam yang diperlukan: "))
bil_pembaris = int(input("Masukkan bilangan pembaris yang diperlukan: ")

# Atur cara mengira harga
jum_pensel = pensel * bil_pensel
jum_pen = pen * bil_pen
jum_gunting = gunting * bil_gunting
jum_pemadam = pemadam * bil_pemadam
jum_pembaris = pembaris * bi_pembaris

# Atur cara mengira jumlah kos
jum_kos = jum_pensel + jum_pen + jum_gunting + jum_pemadam * jum_pembaris

# Atur cara paparkan jumlah kos
print("\nJumlah kos untuk alat tulis: RM"+ jum_kos)
