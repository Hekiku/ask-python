L = [10, 82, 5, 18, 27, 15, 44, 100, 42, 99]
n = 10
i = 0
T = int(input("Masukkan nilai carian: "))

for i in range(n):
    if L[i] == T:
        print("Item ada dalam senarai")
        break
    else:
        i = i + 1
if i >= n:
    print("Item tiada dalam senarai")
