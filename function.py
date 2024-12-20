# variabel globaluntuk menyimpan
buku = []
# fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s"% (indeks, buku[indeks]))

# fungsiuntuk menambah data
def insert_dataa():
    buku_baru = input("judul buku: ")
    buku.append(buku_baru) 

# fungsi untuk edit data
def edit_data():
    show_data()
    indeks = int(input("inputkan ID buku: "))
    if indeks > len(buku):
        print("ID salah")
    else:
        judul_baru = input("jdul baru: ")
        buku[indeks] = judul_baru
def delete_data():
    show_data()
    indeks = int(input("inputkan ID buku: "))
    if indeks > len(buku):
        print("ID salah")
    else:
        buku.remove(buku[indeks])

# fungsi untuk menampilkan menu
def show_menu():
    print("\n")
    print("---------------- MENU ----------------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    menu = input("PILIH MENU> ")
    print("\n")

    if int(menu) == 1:
        show_data()
    elif int(menu) == 2:
        insert_dataa()
    elif int(menu) == 3:
        edit_data()
    elif int(menu) == 4:
        delete_data()
    elif int(menu) == 5:
        exit()
    else:
        print("Salah pilih!")

if __name__ == "__main__":
    while True:
        show_menu()