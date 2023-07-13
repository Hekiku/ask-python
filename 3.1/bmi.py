nama = input("Sila nyatakan nama anda: ")
umur = input("Sila nyatakan umur anda: ")
jantina = input("Sila nyatakan jantina anda: ")
tinggi = float(input("Sila masukkan tinggi anda dalam meter: "))
berat = int(input("Sila masukkan berat anda dalam kilogram: "))

bmi = berat / tinggi ** 2

print("\nNama:", nama)
print("Umur:", umur, "tahun")
print("Jantina:", jantina)
print("BMI anda ialah", bmi)
