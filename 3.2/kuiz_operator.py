print("Jawab soalan-soalan berikut.")
print("a = 12, b = 5, c = 2")

print("\n1. a > b")
print("2. a % b = 0")
print("3. 12 // 5 = c")
print("4. a > 6 > b")
print("5. b < 2 < a")

jaw1 = input("Jawapan soalan 1: ")
jaw2 = input("Jawapan soalan 2: ")
jaw3 = input("Jawapan soalan 3: ")
jaw4 = input("Jawapan soalan 4: ")
jaw5 = input("Jawapan soalan 5: ")

betul = 0
if jaw1 == "True":
    betul = betul + 1
if jaw2 == "False":
    betul = betul + 1
if jaw1 == "True":
    betul = betul + 1
if jaw2 == "True":
    betul = betul + 1
if jaw5 == "False":
    betul = betul + 1

if betul == 5:
    print("Tahniah, anda telah menjawab semua soalan dengan betul.")
else:
    print("Anda telah menjawab", betul, "soalan dengan betul dan", (5-betul), "dengan salah.\nSila buat ulang kaji."
