pertama = float(input("Masukkan ketinggian ahli pertama: "))
kedua = float(input("Masukkan ketinggian ahli kedua: "))
ketiga = float(input("Masukkan ketinggian ahli ketiga: "))
keempat = float(input("Masukkan ketinggian ahli keempat: "))
kelima = float(input("Masukkan ketinggian ahli kelima: "))

jumlah = pertama + kedua + ketiga + keempat + kelima
purata = jumlah / 5

print("\nUkuran ketinggian yang dimasukkan:")
print("Ahli Pertama:", pertama, "m")
print("Ahli Kedua:", kedua, "m")
print("Ahli Ketiga:", ketiga, "m")
print("Ahli Keempat:", keempat, "m")
print("Ahli Kelima:", kelima, "m")
print("\nPurata Ketinggian:" round(purata, 2), "m")
