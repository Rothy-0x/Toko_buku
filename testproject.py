from prettytable import PrettyTable
tabel = PrettyTable()

akun = {"username": ["alby", "aby ", "admin"],
        "password": ["123", "123", "admin"],
        "ID": [1, 2, 3]
        }

tabel.field_names = ["username", "password", "ID"]


def idata(us, pw, id):  # untuk input data
    akun.get("username").append(us)
    akun.get("password").append(pw)
    akun.get("ID").append(id)


def udata(iubah, pw):  # ubah data
    akun.get("password")[cariin] = pwb


def btable():  # buat data
    tabel.clear_rows()
    for i in range(len(akun.get("username"))):
        tabel.add_row([akun.get("username")[i], akun.get(
            "password")[i], akun.get("ID")[i]])

# def cls(): #yg pake spyder...
# print ("\x1b[2J")


def menu():
    print(f"""
    =================================
    |              Menu             |
    =================================
    |       {"1. Input Data"}           |
    |       {"2. Tampil Data"}          |
    |       {"3. Ubah Data"}            |
    |       {"4. Hapus Data"}           |
    |       {"5. Exit"}                 |
    =================================""")


while True:
    username = input("masukkan username: ")
    password = input("masukkan password: ")
    try:
        cariin = akun.get("username").index(username)
        if username == akun.get("username")[cariin] and password == akun.get("password")[cariin]:
            # cls() ditulis untuk yg spyder
            print("Login Berhasil")
            menu()
            pilih = int(input("pilih: "))
            if pilih == 1:
                us = input("Masukkan Username: ")
                pw = input("Masukkan Password: ")
                id = int(input("Masukkan ID: "))
                idata(us, pw, id)
                btable()
                print(tabel)
            elif pilih == 2:
                print(tabel)

            elif pilih == 3:
                cu = input("Masukkan Username yang mau diubah: ")
                cariin = akun.get("username").index(cu)
                pwb = input("Masukkan Password baru: ")
                udata(cariin, pwb)
                btable()
                print(tabel)

            elif pilih == 4:
                tabel.clear_rows()
                print(tabel)

            break
        else:
            print("Login gagal, Password anda salah")
    except ValueError:
        print("Maaf username tidak tersedia")
