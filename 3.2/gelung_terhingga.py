# Nilai kawalan diisytiharkan
teruskan = "y"

# Operator perbandingan digunakan sebagai syarat
while teruskan == "y":
    jualan = float(input("Masukkan jumlah jualan anda: RM"))
    peratus_komisen = float(input("Masukkan peratusan komisen"))
    komisen = jualan * peratus_komisen
    print("Komisen anda adalah RM", komisen)

# Pengujian syarat
    teruskan = input("Adakah anda masih mahu meneruskan? (jawab y untuk ya): ")
