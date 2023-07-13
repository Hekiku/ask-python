tahun = int(input("Masukkan tahun untuk semakan: "))

if tahun % 4 == 0 and tahun % 100 != 0 or tahun % 400 == 0:
    print(str(tahun), "ialah tahun lompat")
else:
    print(str(tahun), "bukan tahun lompat")
