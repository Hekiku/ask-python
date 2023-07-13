# Fungsi yang mengira kuasa dua
def kuasadua(x):
    y = x**2
    return y


# Bahagian utama atur cara
# Minta pengguna memasukkan satu nombor
nom = int(input("Masukkan satu nombor integer: "))

# Panggilan Fungsi
nom_kuasa = kuasadua(nom)
print("Kuasa dua bagi", nom, "ialah", nom_kuasa)
