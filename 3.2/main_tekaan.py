# Nama yang perlu diteka
nama = "Aminah"
tekaan = input("Mari teka nama rahsia ini. Tekaan anda ialah ")
bil = 0

# Dua syarat bagi gelung tekaan berulang
while tekaan != nama and bil < len(nama):
    print("Tekaan salah! Petunjuk: huruf", bil + 1, "ialah", nama[bil] + ".")
    tekaan = input("\nCuba sekali lagi. ")
    bil = bil + 1

# Dua syarat menghentikan gelung tekaan
if bil == len(nama) and nama != tekaan:
    print("Anda tidak dapat tekaan yang betul. Nama yang betul ialah", nama + ".")
else:
    print("\nTahniah! Anda berjaya pada tekaan ke-" + str(bil+1) + ".")
