cerita = [12, 10, 15]
latihan = [15, 12, 18]
rujukan = [33, 15, 0]


def jum_buku(my_list):
    jum = 0
    for x in my_list:
        jum = jum + x
    return jum


jum_cerita = jum_buku(cerita)
jum_latihan = jum_buku(latihan)
jum_rujukan = jum_buku(rujukan)
jum_buku = jum_cerita + jum_latihan + jum_rujukan
paling_banyak = max(jum_cerita, jum_latihan, jum_rujukan)

print(f"Jumlah Semua Buku ialah, {jum_buku} buah\n")
print("Jumlah Buku Mengikut Jenis:")
print(f"Jenis Buku Cerita, {jum_cerita} buah")
print(f"Jenis Buku Latihan, {jum_latihan} buah")
print(f"Jenis Buku Rujukan, {jum_rujukan} buah\n")

if paling_banyak == jum_cerita:
    print("Buku Yang Paling Disukai Pelajar Sekolah Ini ialah Buku Cerita.")
elif paling_banyak == jum_latihan:
    print("Buku Yang Paling Disukai Pelajar Sekolah Ini ialah Buku Latihan.")
else:
    print("Buku Yang Paling Disukai Pelajar Sekolah Ini ialah Buku Rujukan.")
