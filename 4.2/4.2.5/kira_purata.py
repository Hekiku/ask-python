# Function mengira purata
def kira_purata(x, y):
    purata = jumlah / bilangan
    return(purata)


# Atur cara utama
senaraiNo = []
cont = True
while cont:
    try:
        nom = float(input("Masukkan nombor [X utk berhenti]: "))
        senaraiNo.append(nom)
    except ValueError:
        cont = False

bilangan = len(senaraiNo)
jumlah = sum(senaraiNo)
print("Purata =", str(kira_purata(jumlah, bilangan)))
print("Tamat")
