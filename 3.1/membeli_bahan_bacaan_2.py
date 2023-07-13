buku_cerita = float(39)
majalah = float(16)

jum1 = (2 * buku_cerita) + majalah
bayaran = 200
baki1 = 66

jum_buku = bayaran - baki1
buku_motivasi = jum_buku - jum1 / 2  # Pengiraan sebuah buku buku_motivasi

# Semakan pengiraan
jum3 = jum1 + (2 * buku_motivasi)
baki2 = 200 - jum3

print("Bayaran yang dibuat: RM200")
print("\nBuku cerita, RM", 2 * buku_cerita)
print("Majalah, RM", majalah)
print("Buku motivasi, RM", buku_motivasi)
print("\nBaki wang anda, RM", baki2, baki2 == baki1)  # True bermaksud semakan benar
