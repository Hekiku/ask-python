import string

L = list(string.ascii_uppercase)
n = 26
i = 0
j = n - 1
b = input("Masukkan nilai carian: ")

while i <= j:
    m = (i + j) // 2
    if b == L[m]:
        print("Item ada dalam senarai")
        break
    else:
        if b < L[m]:
            j = m - 1
        else:
            i = m + 1
