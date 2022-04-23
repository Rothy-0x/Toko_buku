akun = {"username": ["bambang", "nana", "admin", ""],
        "password": ["123", "123", "admin"]
        }


# for index,value in enumerate(akun.get("username")):#enumerate ini digunakan untuk mengambil suatu index dan value
#   print(value, "berada di index ke",index)


def menu():
    print("""
    1. input barang
    2. tampil barang
    3. ubah barang
    4. hapus barang
    3. exit

    """)


cekl = 0

while True:
    username = input("masukkan username : ")
    password = input("masukkan password: ")
    if username == akun.get("username")  and password == akun.get("password"):
        print(" CONTOH PROGRAM ".center(30, "="))
        menu()
        break
    else:
        cekl += 1
