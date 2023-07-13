import random


# User-defined function untuk simulasi menimbang batu
def bilangan_batu(x):
    hasil = (random.randint(0, x))
    return hasil


# Membuat panggilan function
# Hantar nilai bilangan batu yang digunakan ke dalam bilangan_batu()
terus = "Y"
while terus == "Y":
    hasil_timbang = bilangan_batu(5)
    print("Hasil timbangan anda ialah " + str(hasil_timbang) + "batu.")

# Menangkap batu. Membuat panggilan fungsi
# Hantar hasil timbangan ke dalam bilangan_batu()
    if hasil_timbang > 0:
        tangkap = bilangan_batu(hasil_timbang)
        print("Hasil tangkapan anda ialah " + str(tangkap))
    terus = input("\nTeruskan [Y] atau Berhenti [T]? Tekan [Y|T] ")
    print()
