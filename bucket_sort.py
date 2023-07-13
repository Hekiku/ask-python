def bubble(L):
    n = len(L)
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

    return(L)


def bucket(L):
    buckets = [[] for x in range(10)]
    for val in L:
        buckets[int(val*len(buckets))].append(val)
    out = []
    for buck in buckets:
        out = out + bubble(buck)
    return out


L = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
L_sort = bucket(L)
print(L_sort)
