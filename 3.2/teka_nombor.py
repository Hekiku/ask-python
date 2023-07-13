print("************* PERMAINAN MENEKA NOMBOR *************")

rahsia = 49
teka = True

while teka:
    nombor = int(input("Masukkan nombor tekaan anda: "))
    if rahsia == nombor:
        for i in range(5):
            print("Syabas!")
        teka = False
    elif rahsia < nombor:
        print("Nombor tekaan lebih besar daripada nombor rahsia.")
    else:
        print("Nombor tekaan lebih kecil daripada nombor rahsia.")
else:
    print("Terima kasih kerana menyelesaikan permainan meneka nombor ini.")
