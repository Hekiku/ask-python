print("***Pengiraan Komisen Bagi Program Jualan Amal***")

buah = input(float("Masukkan jualan buah-buahan: RM "))
minuman = input(float("Masukkan jualan minuman: RM "))
biskut = input(float("Masukkan jualan biskut: RM "))

jum_jualan = buah + minuman + biskut
print("\nJumlah jualan: RM", round(jumjualan, 2))

if jum_jualan > 800:
    print("Komisen ialah 8%")
    komisen = 0.08
elif jum_jualan > 500:
    print("Komisen ialah 5%")
    komisen = 0.05
else
    print("Komisen ialah 0%")
    komisen = 0

jum_komisen = jum_jualan * komisen
ind_komisen = jum_komisen / 6

print("Jumlah komisen: RM", round(jum_komisen, 2))
print("Komisen untuk setiap ahli: RM", round(ind_komisen,2)
