from prettytable import PrettyTable
from os import system
import pwinput
import sys
import csv
from termcolor import cprint, colored


def cls():
    if sys() == "Windows":
        system("cls")
    else:
        system("clear")


# =============================================================================================================
pinpass = "051298"

useracc = {
    'username': ['alby', 'nabila', 'firzian'],
    'password': ['alby', 'nabila', 'firzian'],
    'id': ['1', '2', '3']
}

users = {
    'username': ['admin', 'admin2'],
    'password': ['admin', 'admin2'],
    'id': ['1', '2']
}

jenis_pesanan = {
    'nama': ['Cuci Komplit Reguler', 'Cuci Komplit Kilat', 'Cuci Komplit Express', 'Cuci Kering Reguler', 'Cuci Kering Kilat', 'Cuci Kering Express', 'Setrika Reguler', 'Setrika Kilat', 'Setrika Express'],
    'waktu': ['2-3 hari', '1 hari', '9 jam', '2-3 hari', '1 hari', '9 jam', '2-3 hari', '1 hari', '9 jam', ],
    'harga': [7000, 12000, 15000, 6000, 9000, 10000, 6000, 9000, 10000]
}
db = {
    "pesanan": [],
}

jenis = PrettyTable()
jenis.field_names = ['id', 'nama', 'waktu', 'harga']

user = PrettyTable()
user.field_names = ["id", "Nama", "No Telp",
                    "Alamat", "Jenis Laundry", "Jumlah Laundry ", "Harga"]

userakun = PrettyTable()
userakun.field_names = ['id', 'username', 'password']

# =================================Fungsi ADMIN================================================================


def add():
    print("=" * 52)
    nama = input("Masukkan Nama Pelanggan : ")
    while True:
        notelp = input("Masukkan No Telp Pelanggan : ")
        if cek_nomor_hp(notelp):
            break
        else:
            cprint("Silahkan Masukkan Ulang!!", 'red')
    alamat = input("Masukkan Alamat Pelanggan : ")
    while True:
        showjenis()
        try:
            jenis = int(input("Masukkan Jenis Laundry (No) : "))
            if jenis <= len(jenis_pesanan['harga']):
                harga = jenis_pesanan['harga'][jenis - 1]
                break
            else:
                cprint("Jenis tidak tersedia!!!", 'red')
        except ValueError:
            cprint("Silahkan Masukkan Ulang!!!", 'red')
    while True:
        try:
            jumlah = int(input("Masukkan Jumlah Laundry(Kg) : "))
            break
        except ValueError:
            cprint("Silahkan Masukkan Ulang", 'red')

    db.get('pesanan').append({
        'nama': nama,
        'notelp': notelp,
        'alamat': alamat,
        'jenis': jenis,
        'jumlah': jumlah,
        "harga": harga
    })

    cprint('Pesanan berhasil ditambah!!', 'green')


def show():
    tabel = PrettyTable()
    tabel.field_names = ['No', 'Nama', 'No Telp',
                         'Alamat', 'Jenis', 'Jumlah', 'Harga', 'Subtotal']

    pesanan = db.get('pesanan')
    for i in range(len(pesanan)):
        p = pesanan[i]
        tabel.add_row([
            i + 1,
            p.get('nama'),
            p.get('notelp'),
            p.get('alamat'),
            jenis_pesanan['nama'][p.get('jenis') - 1],
            p.get('jumlah'),
            p.get('harga'),
            p.get('jumlah') * p.get('harga')
        ])

    print(tabel)


def delete():
    show()
    i = int(input('Pilih pesanan yang ingin dihapus : '))
    a = input(
        colored("Apakah Anda Yakin Ingin Menghapus Pesanan ini ?(y/n) : ", 'red'))
    if a == 'y' or a == 'Y' or a == 'Ya' or a == 'yA' or a == 'YA' or a == 'ya':
        del db['pesanan'][i - 1]
        print()
        cprint('Pesanan berhasil dihapus', 'yellow')
    elif a == 'n' or a == 'no' or a == 'No' or a == 'nO' or a == 'NO' or a == 'N':
        return delete()
    show()


def update():
    show()
    i = int(input('Pilih pesanan yang ingin diedit : '))

    if i - 1 < len(db['pesanan']):
        pesanan = db['pesanan'][i - 1]

        nama = input(
            f"Masukkan Nama Pelanggan ({pesanan['nama']}) : ") or pesanan['nama']
        notelp = input(
            f"Masukkan No Telp Pelanggan ({pesanan['notelp']}) : ") or pesanan['notelp']
        alamat = input(
            f"Masukkan Alamat Pelanggan ({pesanan['alamat']}) : ") or pesanan['alamat']
        showjenis()
        jenis = input(
            f"Masukkan Jenis Laundry ({pesanan['jenis']}) : ") or pesanan['jenis']
        jenis = int(jenis)
        if jenis <= len(jenis_pesanan['harga']):
            harga = jenis_pesanan['harga'][jenis - 1]
        else:
            print("Jenis tidak tersedia")
            return update()

        jumlah = input(
            f"Masukkan Jumlah Laundry ({pesanan['jumlah']}) : ") or pesanan['jumlah']

        pesanan['nama'] = nama
        pesanan['notelp'] = notelp
        pesanan['alamat'] = alamat
        pesanan['jenis'] = jenis
        pesanan['jumlah'] = int(jumlah)
        pesanan["harga"] = int(harga)

        print()
        cprint('Pesanan berhasil diedit!!!', 'yellow')
        show()
    else:
        print('Mohon masukan pesanan yang tersedia')
        return update()


def cek_nomor_hp(notelp):
    for i in notelp:
        if i.isalpha():
            return False
    return True


def laporan():
    with open('output.csv', 'w', newline='') as csv_1:
        csv_out = csv.writer(csv_1)
        pesanan = db.get('pesanan')
        for a in range(0, len(pesanan)):
            csv_out.writerow([
                a + 1,
                pesanan[a]['nama'],
                pesanan[a]['notelp'],
                pesanan[a]['alamat'],
                pesanan[a]['jenis'],
                pesanan[a]['jumlah'],
                pesanan[a]['harga'],
                pesanan[a]['jumlah'] * pesanan[a]['harga']
            ])
            print()
            cprint("Data Telah Berhasil Di Import!!!", 'green')


def showjenis():
    jenis = PrettyTable()
    jenis.field_names = ["No", "Jenis Laundry", "Lama Pengerjaan", "Harga"]
    jenis.clear_rows()
    for i in range(len(jenis_pesanan.get("nama"))):
        jenis.add_row([i + 1, jenis_pesanan.get("nama")[i],
                      jenis_pesanan.get("waktu")[i], jenis_pesanan.get("harga")[i]])
    print(jenis)


def menua():
    ulang = "ya"
    while (ulang == "ya"):
        print("=" * 42)
        print("="*5, "Aplikasi Laundry".center(30), "="*5)
        print("="*5, "Admin".center(30), "="*5)
        print("=" * 42)
        print("1. Tambah Pelanggan")
        print("2. Hapus Pelanggan")
        print("3. Tampilkan Pelanggan")
        print("4. Ubah pelanggan")
        print("5. Tampilkan Kasir")
        print("6. Cetak Struk ")
        print("7. Jenis Laundry")
        print("8. Import data to csv")
        print("9. Logout")
        print("10. Exit")
        print("=" * 42)
        print()
        msk = input("Silahkan Masukkan Pilihan Anda : ")

        if msk == '1':
            add()
        elif msk == '2':
            delete()
        elif msk == '3':
            show()
        elif msk == "4":
            update()
        elif msk == "5":
            showuser()
        elif msk == "6":
            struk()
        elif msk == "7":
            showjenis()
        elif msk == '8':
            laporan()
        elif msk == '9':
            print("=" * 42)
            cprint("Terima Kasih Telah Menggunakan Aplikasi Kami ", 'cyan')
            return menuawal()
        elif msk == '10':
            print("=" * 42)
            cprint("Terima Kasih Telah Menggunakan Aplikasi Kami ", 'cyan')
            exit()
        else:
            cprint("Menu tidak ada, Silahkan Masukkan Ulang!!", 'red')


def logina():
    ulang = "ya"
    while (ulang == "ya"):
        print('=' * 42)
        username = input("Masukkan Username Anda : ")
        password = pwinput.pwinput("Masukkan Password Anda : ")
        print('=' * 42)
        try:
            search = users.get("username").index(username)
            if username == users.get("username")[search] and password == users.get("password")[search]:
                print('='*42)
                print("="*5, "Anda Berhasil Login".center(30), "="*5)
                print('='*42)
                print('='*42)
                print()
                input("Press Enter to Continue...")
                menua()
                ulang = "tidak"
            else:
                print("Username atau Password Anda Salah!")
                print("Silahkan Coba Lagi")
        except ValueError:
            print("Maaf username tidak tersedia")


def registera():
    ulang = "ya"
    while (ulang == "ya"):
        print('=' * 42)
        add_username = input("Masukkan Username Yang Anda Inginkan : ")
        if add_username in users.get("username"):
            print('=' * 42)
            print("Maaf Username Anda telah tersedia!!\nSilahkan Masukkan Ulang")
            registera()
        else:
            add_password = input("Masukkan Password Anda : ")
            users.get("username").append(add_username)
            users.get("password").append(add_password)
            id = len(users.get('id'))
            users.get('id').append(id+1)
            print('=' * 42)
            print("Anda Telah Berhasil Register!!")
            return


def menuadmin():
    ulang = "ya"
    while (ulang == "ya"):
        print('='*42)
        print("="*5, "Aplikasi Laundry".center(30), "="*5)
        print("="*5, "Admin".center(30), "="*5)
        print("=" * 42)
        print("1. Login")
        print("2. Register")
        print("3. Back")
        print("4. Exit")
        print("=" * 42)
        print()
        msk = input("Silahkan Masukkan Pilihan Anda : ")

        if msk == "1":
            logina()
        elif msk == "2":
            registera()
        elif msk == "3":
            return menuawal()
        elif msk == "4":
            print("=" * 42)
            cprint("Terima Kasih Telah Menggunakan Aplikasi Kami ", 'cyan')
            exit()
        else:
            cprint("Menu tidak ada, Silahkan Masukkan Ulang!!", 'red')


# =================================Fungsi USER================================================================

def struk():
    show()
    p = int(input("Silahkan Masukkan Pesanan Nomor Berapa? : "))
    if p - 1 < len(db['pesanan']):
        pesanan = db['pesanan'][p - 1]
        print('=' * 42)
        print("="*5, "Struk Pesanan".center(30), "="*5)
        print("=" * 42)
        print(f"Nama  = {pesanan['nama']} ")
        print(f"Jenis = {jenis_pesanan['nama'][pesanan.get('jenis') - 1]}")
        print(
            f"Waktu Pengerjaan = {jenis_pesanan['waktu'][pesanan.get('jenis') - 1]}")
        print(f"Harga Jenis = Rp. {pesanan['harga']} ")
        print(f"Jumlah =  {pesanan['jumlah']} Kg")
        print('=' * 42)
        subtotal = pesanan['jumlah'] * pesanan['harga']
        print(f"Subtotal = Rp. {subtotal} ")
        print('=' * 42)
        print("="*5, "Terima Kasih".center(30), "="*5)
        print("="*5, "Telah Menggunakan Jasa Kami".center(30), "="*5)
        print("=" * 42)


def showuser():
    tableuser = PrettyTable()
    tableuser.field_names = ['id', 'username']
    tableuser.clear_rows()
    for i in range(len(useracc.get('username'))):
        tableuser.add_row([
            i+1, useracc.get('username')[i],
        ])

    print(tableuser)


def menuu():
    ulang = "ya"
    while (ulang == "ya"):
        print("=" * 42)
        print("1. Tambah Pesanan")
        print("2. Tampilkan Pesanan")
        print("3. Cetak Struk")
        print("4. Logout")
        print("5. Exit")
        print("=" * 42)
        print()
        msk = input("Silahkan Masukkan Pilihan Anda : ")

        if msk == '1':
            add()
        elif msk == '2':
            show()
        elif msk == '3':
            struk()
        elif msk == '4':
            print("=" * 42)
            cprint("Terima Kasih Telah Menggunakan Aplikasi Kami ", 'cyan')
            return menuawal()
        elif msk == "5":
            print("=" * 42)
            cprint("Terima Kasih Telah Menggunakan Aplikasi Kami ", 'cyan')
            exit()
        else:
            cprint("Menu tidak ada, Silahkan Masukkan Ulang!!", 'red')


def registeruser():
    ulang = "ya"
    while (ulang == "ya"):
        print('=' * 42)
        add_username = input("Masukkan Username Yang Anda Inginkan : ")
        if add_username in useracc.get("username"):
            print('=' * 42)
            cprint(
                "Maaf Username Anda telah tersedia!!\nSilahkan Masukkan Ulang", 'red')
            registeruser()
        else:
            add_password = input("Masukkan Password Anda : ")
            useracc.get("username").append(add_username)
            useracc.get("password").append(add_password)
            id = len(useracc.get('id'))
            useracc.get('id').append(id+1)
            print('=' * 42)
            cprint("Anda Telah Berhasil Register!!", 'green')
            return menukasir()


def masukan_pin():
    pin = pwinput.pwinput("Masukkan Pin untuk Registrasi Akun : ")
    if pin == pinpass:
        return registeruser()
    else:
        cprint("Pin Anda Salah !!!, Silahkan Masukkan Ulang", 'red')

        okt = input("Apakah Anda Ingin Masukkan Ulang?(y/n) : ")
        if okt == "y" or okt == 'Y' or okt == 'Ya' or okt == 'yA' or okt == 'YA' or okt == 'ya':
            return masukan_pin()
        elif okt == "n" or okt == 'no' or okt == 'No' or okt == 'nO' or okt == 'NO' or okt == 'N':
            return menuawal()


def menukasir():
    while True:
        print('='*42)
        print("="*5, "Aplikasi Laundry".center(30), "="*5)
        print("="*5, "Kasir".center(30), "="*5)
        print("=" * 42)
        print("1. Login")
        print("2. Register")
        print("3. Back")
        print("4. Exit")
        print("=" * 42)
        print()

        msk = input("Silahkan Masukkan Pilihan Anda : ")

        if msk == "1":
            loginuser()
        elif msk == "2":
            return masukan_pin()
        elif msk == "3":
            return menuawal()
        elif msk == "4":
            print("=" * 42)
            cprint("Terima Kasih Telah Menggunakan Aplikasi Kami ", 'cyan')
            exit()
        else:
            cprint("Menu tidak ada, Silahkan Masukkan Ulang!!", 'red')


def loginuser():
    ulang = "ya"
    while (ulang == "ya"):
        print('=' * 42)
        username = input("Masukkan Username Anda : ")
        password = pwinput.pwinput("Masukkan Password Anda : ")
        print('=' * 42)
        try:
            search = useracc.get("username").index(username)
            if username == useracc.get("username")[search] and password == useracc.get("password")[search]:
                print('='*42)
                print("="*5, "Anda Berhasil Login".center(30), "="*5)
                print('='*42)
                print('='*42)
                print()
                input("Press Enter to Continue...")
                menuu()
                ulang = "tidak"
            else:
                cprint("Username atau Password Anda Salah!", 'red')
                print("Silahkan Coba Lagi")
        except ValueError:
            cprint("Maaf username tidak tersedia", 'red')


# =================================Menu Awal===============================================================
def menuawal():
    while True:
        print('='*42)
        print("="*5, "Aplikasi Laundry".center(30), "="*5)
        print("=" * 42)
        print("1. Login Admin")
        print("2. login Kasir")
        print("3. Exit")
        print("=" * 42)
        print()
        msk = input("Silahkan Masukkan Pilihan Anda : ")

        if msk == "1":
            menuadmin()
        elif msk == "2":
            menukasir()
        elif msk == '3':
            print('='*42)
            cprint("Terima Kasih Telah Menggunakan Aplikasi Kami ", 'cyan')
            exit()
        else:
            cprint("Menu tidak ada, Silahkan Masukkan Ulang!!", 'red')


menuawal()
