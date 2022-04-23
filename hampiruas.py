import os
import pwinput
from termcolor import cprint
import time
from datetime import datetime as dt
from prettytable import PrettyTable

useracc = {
    "username": ['alby', 'novil', 'rizky'],
    "password": ['123', '123', '123'],
    "age": [10, 20, 40],
    "id": ['1', '2', '3'],
    "sp-coin": [10000, 0, 0],
    "sp-money": [10000000, 0, 0],
    "stat": ['Reguler', 'Reguler', 'Reguler']
}

role = {
    "id" : [],
    "username" : [],
    "waktu" : [],
    'status' : []
}
shop_item = {
    "nama": ['baju', 'sepatu', 'celana', 'kaos kaki', 'sendal'],
    "harga": [200, 400, 150, 100, 250],
    "stok": [10, 12, 13, 14, 15]
}

db = {
    "nama": [],
    "harga": [],
    "jumlah": []
}
# ---------------------------------------------------------------------------------------------------


def cls():
    os.system('cls')
    time.sleep(1)

def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3:
        return 'Rp. ' + y
    else:
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p

#====================================================================================================#


def shoppingmenu():
    while True:
        showitem()
        print("=" * 42)
        while True:
            try:
                nomor = int(input("Masukkan Nomor Barang Anda : "))
                if nomor <= 0:
                    print("Barang Tidak Ada")
                    time.sleep(1)
                    return shoppingmenu()
                nama = shop_item.get('nama')[nomor - 1]
                if nomor <= len(shop_item['harga']):
                    harga = shop_item['harga'][nomor - 1]
            except ValueError:
                print("Silahkan Masukkan Ulang")
            break
        jumlah1 = shop_item.get("stok")[nomor - 1]
        try:
            while True:
                jumlah = int(input("Masukkan Berapa Jumlah Yang Anda Beli : "))
                if jumlah > jumlah1:
                    print("Stok barang tidak mencukupi!")
                    continue
                jumlah1 = jumlah1 - jumlah
                shop_item["stok"][nomor - 1] = jumlah1
                break
        except ValueError:
            print("Silahkan Masukkan Ulang")
        db.get("nama").append(nama)
        db.get("harga").append(harga)
        db.get("jumlah").append(jumlah)
        more = input("Apakah Anda Ingin Memesan Lagi ? ")
        if more == 'ya':
            return shoppingmenu()
        elif more == 'tidak':
            pembayaran()
        else:
            print("Silahkan Masukkan Ulang")
            return more()

def pembayaran():
    p = input("Apakah anda ingin membayar?: ")
    if p == 'ya':
        if search < len(role['status']) :
            if role['status'][search] == 'VIP' :
                bayarvip()
            else :
                bayar()
        else:
            bayar()
    elif p == "t" or p == 'tidak' or p == 'TIDAK' or p == 'Tidak':
        return menut()
    else:
        print("Silahkan Masukkan Ulang")

def tampilpesanan():
    table = PrettyTable()
    table.field_names = ['Nomor Pesanan','Nama Barang', 'Harga Barang', 'Jumlah Barang']
    table.clear_rows
    for i in range(len(db.get("nama"))):
        table.add_row([
            'A' + str(i + 1),
            db.get("nama")[i],
            str(db.get('harga')[i]) + " Coin",
            db.get('jumlah')[i]
        ])
    print(table)


def bayar():
    tampilpesanan()
    print(">> Berikut Adalah Pesanan Anda")
    a = input(">> Apakah Anda Yakin Ingin Membayar? :  ")
    total = []
    if a == 'ya':
        for i in range(len(db.get("nama"))):
            total.append(db["harga"][i]*db["jumlah"][i])
        x = sum(total)
        print(">> Total Harganya adalah", x, "Coin")
        if useracc["sp-coin"][search] < x :
            print(">> Saldo Anda Tidak Cukup Untuk Melakukan Pembayaran \n>> Silahkan Top-Up Terlebih Dahulu")
            cls()
            return menut()
        else :
            saldoc = useracc.get("sp-coin")[search] - x
            useracc["sp-coin"][search] = saldoc
            time.sleep(1)
            print(">> Pembayaran telah berhasil")
            print(">> Sisa Saldo Coin Anda adalah", useracc["sp-coin"][search], 'Coin')
            print(">"*5, "Terima Kasih Telah Berbelanja Di Toko Kami".center(30), "<"*5)
            return menut()
    else :
        return menut()
def bayarvip():
    tampilpesanan()
    print(">> Berikut Adalah Pesanan Anda")
    a = input(">> Apakah Anda Yakin Ingin Membayar? :  ")
    total = []
    if a == 'ya':
        for i in range(len(db.get("nama"))):
            total.append(db["harga"][i]*db["jumlah"][i])
        x = sum(total)
        a = x * (30/100)
        y = x - a
        print("Karna Anda adalah VIP anda mendapatkan diskon sebesar 30% ")
        print(">> Total Harganya adalah", y, "Coin")
        if useracc["sp-coin"][search] < y :
            print(">> Saldo Anda Tidak Cukup Untuk Melakukan Pembayaran \n>> Silahkan Top-Up Terlebih Dahulu")
            cls()
            return menut()
        else :
            saldoc = useracc.get("sp-coin")[search] - a
            useracc["sp-coin"][search] = saldoc
            time.sleep(1)
            print(">> Pembayaran telah berhasil")
            print(">> Sisa Saldo Coin Anda adalah",useracc["sp-coin"][search], 'Coin')
            print(">"*5, "Terima Kasih Telah Berbelanja Di Toko Kami".center(30), "<"*5)
            return menut()
    else :
        return menut()


def topupm():
    jumlah = int(input(">> Masukkan Jumlah : "))
    if jumlah < 50000 :
        print("Maaf, Minimal Pengisian Saldo adalah Rp. 50.000")
        return topupm
    else:
        buy = useracc.get("sp-money")[search] + jumlah
        useracc['sp-money'][search] = buy
        time.sleep(2)
        print("Transaksi Anda Telah Berhasil")


def c245():
    harga = 100000
    if useracc['sp-money'][search] < harga:
        print("Maaf, Saldo Anda Tidak Mencukupi\nSilahkan Top-Up Terlebih Dahulu")
        return menut()
    else:
        buy = useracc.get("sp-money")[search] - harga
        useracc["sp-money"][search] = buy
        coin1 = useracc.get("sp-coin")[search] + 245
        useracc['sp-coin'][search] = coin1
        cls()
        print("Pembelian Anda Sedang Diproses")
        time.sleep(2)
        cls()
        time.sleep(0.7)
        print("Pembelian Berhasil!")
        time.sleep(1)
        cls()
        return menut()


def c540():
    harga = 200000
    if useracc['sp-money'][search] < harga:
        print("Saldo Anda Tidak Mencukupi\nSilahkan Top-Up Terlebih Dahulu")
        return menut()
    else:
        buy = useracc.get("sp-money")[search] - harga
        useracc["sp-money"][search] = buy
        coin1 = useracc.get("sp-coin")[search] + 540
        useracc['sp-coin'][search] = coin1
        cls()
        print("Pembelian Anda Sedang Diproses")
        time.sleep(2)
        cls()
        time.sleep(0.7)
        print("Pembelian Berhasil!")
        time.sleep(1)
        cls()
        return menut()


def c825():
    harga = 270000
    if useracc['sp-money'][search] < harga:
        print("Saldo Anda Tidak Mencukupi\nSilahkan Top-Up Terlebih Dahulu")
        return menut()
    else:
        buy = useracc.get("sp-money")[search] - harga
        useracc["sp-money"][search] = buy
        coin1 = useracc.get("sp-coin")[search] + 825
        useracc['sp-coin'][search] = coin1
        cls()
        print("Pembelian Anda Sedang Diproses")
        time.sleep(2)
        cls()
        time.sleep(0.7)
        print("Pembelian Berhasil!")
        time.sleep(1)
        cls()
        return menut()

def c1():
    harga = 500
    print()
    jumlah = int(input("Masukkan Jumlah Yang Anda Inginkan : "))
    harga1 = jumlah * harga
    if useracc['sp-money'][search] < harga1:
        print("Saldo Anda Tidak Mencukupi\nSilahkan Top-Up Terlebih Dahulu")
        return menut()
    else:
        buy = useracc.get("sp-money")[search] - harga1
        useracc["sp-money"][search] = buy
        coin1 = useracc.get("sp-coin")[search] + jumlah
        useracc['sp-coin'][search] = coin1
        cls()
        print("Pembelian Anda Sedang Diproses")
        time.sleep(2)
        cls()
        time.sleep(0.7)
        print("Pembelian Berhasil!")
        time.sleep(1)
        cls()
        return menut()

    

def showmoney():
    saldom = useracc.get("sp-money")[search]
    saldoc = useracc.get("sp-coin")[search]
    print(f'Saldo SP-Money Anda = {formatrupiah(saldom)}')
    print()
    print(f'Saldo SP-Coin Anda = {saldoc}', 'Coin')
    input("Press Enter to Continue...")
    time.sleep(1)
    cls()
    return menut()


def showitem():
    show = PrettyTable()
    show.field_names = ["No", "Nama Barang", "Harga Barang", "Jumlah"]
    show.clear_rows()
    for i in range(len(shop_item.get("nama"))):
        show.add_row([
            i + 1,
            shop_item.get("nama")[i],
            str(shop_item.get("harga")[i]) + ' coin',
            shop_item.get("stok")[i]
        ])
        show.align["Harga Barang"] = 'l'
        show.align["Nama Barang"] = 'l'
    print(show)


def showuser():
    tableuser = PrettyTable()
    tableuser.field_names = ['id', 'username', 'age']
    tableuser.clear_rows()
    for i in range(len(useracc.get('username'))):
        tableuser.add_row([
            i+1, 
            useracc.get('username')[i], 
            useracc.get('age')[i]
        ])
    print(tableuser) 

def vip():
    print(">"*5, "Harga Member VIP = 5000 Coin".center(30), "<"*5)
    x = input(">>Apakah anda yakin ingin membeli VIP? : ")
    if x == "y" or x == 'Y' or x == 'Ya' or x == 'yA' or x == 'YA' or x == 'IYA'or x == 'ya' or x == 'Iya'or x == 'iya'or x == 'IYa' :
        if useracc['sp-coin'][search] < 5000:
            print("Saldo Anda Tidak Mencukupi\nSilahkan Top-Up Terlebih Dahulu")
            return menut()
        elif useracc['sp-coin'][search] >= 5000:
            a = useracc.get("username")[search]
            role.get('id').append(search)
            role.get('username').append(a)
            role.get('status').append("VIP")
            harga = 5000
            saldoc = useracc.get('sp-coin')[search] - harga
            useracc.get('sp-coin')[search] = saldoc
            waktu_expired = '17-1-2022'
            str_waktu_expired = dt.strptime(waktu_expired, '%d-%m-%Y')
            role.get("waktu").append(waktu_expired)
            print("Pembelian Vip Anda Telah Berhasil ")
            print("Sekarang ", role.get("username")[0], "Anda Telah Berlangganan VIP,\nWaktu expired anda adalah", role.get("waktu")[0])
            print("Saldo Anda sekarang adalah", saldoc,'Coin')
            return menut()
    else :
        return menut()
# -------------------------------------------------------------------------------------------------------


def menucoin():
    while True:
        time.sleep(1)
        print("""
===============================================================
======                   Shopedia                        ======
===============================================================
|                    1. 245 Coin = RP. 100.000                |
|                    2. 540 Coin = Rp. 200.000                |
|                    3. 825 Coin = Rp. 270.000                |
|                    4. 1 Coin   = Rp. 500                    |
===============================================================
            """)

        try:
            msk = int(input(">> Silahkan Masukkan Pilihan Anda : "))
            if msk == 1:
                c245()
            elif msk == 2:
                c540()
            elif msk == 3:
                c825()
            elif msk == 4:
                c1()    
            else:
                print("Menu tidak tersedia!!\n Silahkan Masukkan Ulang")
                return menucoin()
        except ValueError:
            cprint("Silahkan Masukkan Dengan Benar!!!", 'red')
            return menucoin()


def menu():
    while True:
        print("=" * 42)
        print("="*5, "Shopedia".center(30), "="*5)
        print("=" * 42)
        print(">>", "1. Login".center(36), "<<")
        print(">>", "2. Exit".center(36), "<<")
        print("=" * 42)
        print()
        msk = input("Silahkan Masukkan Pilihan Anda : ")

        if msk == '1':
            login()
        elif msk == '3':
            showitem()
        elif msk == '2':
            print("=" * 42)
            cprint("Terima Kasih Telah Menggunakan Aplikasi Kami ", 'cyan')
            raise SystemExit
        else:
            cprint("Menu tidak ada, Silahkan Masukkan Ulang!!", 'red')


def menut():
    while True:
        print("""
===============================================================
======                   Shopedia                        ======
===============================================================
|                    1. Check SP-Money                        |
|                    2. Buy SP-Coin                           |
|                    3. Top-up SP-Money                       |
|                    4. Buy VIP Member                        |
|                    5. Shopping Menu                         |
|                    6. Exit                                  |
===============================================================
            """)
        print()
        msk = input("Silahkan Masukkan Pilihan Anda : ")

        if msk == '1':
            showmoney()
        elif msk == '2':
            menucoin()
        elif msk == '3':
            topupm()
        elif msk == '4':
            vip()
        elif msk == '5':
            shoppingmenu()
        elif msk == '6':
            print("=" * 42)
            cprint("Terima Kasih Telah Menggunakan Aplikasi Kami ", 'cyan')
            raise SystemExit
        else:
            cprint("Menu tidak ada, Silahkan Masukkan Ulang!!", 'red')


def login():
    ulang = "ya"
    while (ulang == "ya"):
        print('=' * 42)
        username = input("Masukkan Username Anda : ")
        password = pwinput.pwinput("Masukkan Password Anda : ")
        print('=' * 42)
        try:
            global search
            search = useracc.get("username").index(username)
            if username == useracc.get("username")[search] and password == useracc.get("password")[search] and useracc.get("age")[search] <= 12:
                print('='*42)
                print(
                    "="*5, f"Selamat Datang Adek {username}".center(30), "="*5)
                print('='*42)
                print('='*42)
                print()
                input("Press Enter to Continue...")
                cls()
                menut()
            elif username == useracc.get("username")[search] and password == useracc.get("password")[search] and useracc.get("age")[search] == 12 or useracc.get("age")[search] <= 25:
                print('='*42)
                print(
                    "="*5, f"Selamat Datang Kakak {username}".center(30), "="*5)
                print('='*42)
                print('='*42)
                print()
                input("Press Enter to Continue...")
                cls()
                menut()
            elif username == useracc.get("username")[search] and password == useracc.get("password")[search] and useracc.get("age")[search] == 26 or useracc.get("age")[search] <= 40:
                print('='*42)
                print(
                    "="*5, f"Selamat Datang Bapak {username}".center(30), "="*5)
                print('='*42)
                print('='*42)
                print()
                input("Press Enter to Continue...")
                cls()
                menut()
            else:
                cprint("Username atau Password Anda Salah!", 'red')
                print("Silahkan Coba Lagi")
        except ValueError:
            cprint("Maaf username tidak tersedia", 'red')


menu()
