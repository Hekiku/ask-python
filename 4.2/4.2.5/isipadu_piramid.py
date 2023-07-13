# Mengira isipadu piramid bertapak segi empat sama
def kira_Isipadu_piramid(a, b):
    isipadu_piramid = (1/3) * (sisi * sisi) * tinggi
    return(isipadu_piramid)


# Atur cara utama
print("Kira Isipadu Piramid")
sisi = int(input("Masukkan ukuran sisi tapak piramid: "))
tinggi = int(input("Masukkan tinggi piramid: "))

# Pemanggilan function dan pemulangan nilai
print("Isi Padu Piramid =", kira_Isipadu_piramid(a, b))
