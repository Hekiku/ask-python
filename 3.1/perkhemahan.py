float(peribadi=13.50)
float(pakaian=105.90)
float(khemah=12.00)

kos_tetap = peribadi + pakaian + khemah
kos_masak = float(input("\nMasukkan kos untuk barangan memasak: RM"))
jumlah_kos = kos_tetap + kos_masak

print("\n***Pengiraan Kos Perkhemahan Unit Berunifor***")
print("\nJumlah bagi Kos Tetap: RM", kos_tetap)
print("Jumlah bagi Kos Berubah: RM", kos_masak)
print("Jumlah Kos: RM", round(jumlah_kos, 2))
