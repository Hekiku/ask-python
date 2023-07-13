def banding(x, y):
    if x > y:
        besar = x
    else:
        kecil = x
    return(besar, kecil)


# Atur cara utama
[besar, kecil] = banding(6, 9)
print("Nombor", besar, "lebih besar daripada", kecil)
