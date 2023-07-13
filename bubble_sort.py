L = [28.2, 26, 26.5, 27.2, 30.4, 27, 31.4, 29.1, 27.4, 27.8]
n = 10
i = 0
temp = 0

for i in range(n - 1):
    j = 0
    for j in range(n - i - 1):
        if L[j] > L[j + 1]:
            temp = L[j]
            L[j] = L[j + 1]
            L[j + 1] = temp
        j = j + 1
    i = i + 1

print(L)
