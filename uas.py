from prettytable import PrettyTable
from os import system
import pwinput
import sys
from termcolor import cprint
import time

from ProjectAkhir import show


def cls():
    if sys() == "Windows":
        system("cls")
        time.sleep(1)
    else:
        system("clear")
        time.sleep(1)


useracc = {
    "username": ['alby', 'novil', 'rizky'],
    "password": ['123', '123', '123'],
    "age": [10, 20, 30],
    "id": ['1', '2', '3'],
    "sp-coin": [10000, 0, 0],
    "sp-money": [1000000, 0, 0],
    "stat": ['Reguler', 'Reguler', 'Reguler']
}

status = {
    "name": ["VIP", "Reguler"],
    "harga": 2023
}
shop_item = {
    "nama": ['baju', 'sepatu', 'celana', 'kaos kaki', 'sendal'],
    "harga": [125000, 300000, 100000, 50000, 70000],
    "stok": [10, 12, 13, 14, 15]
}

db = {
    "pesanan": []
}
# ---------------------------------------------------------------------------------------------------


def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3:
        return 'Rp. ' + y
    else:
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p

#====================================================================================================#


def topupm():
    jumlah = int(input(">> Masukkan Jumlah : "))
    useracc.get("sp-money").append(jumlah)
    time.sleep(2)
    print("Transaksi Anda Telah Berhasil")


def showmoney(data):
    saldom = useracc.get("sp-money")[data]
    saldoc = useracc.get("sp-coin")[data]
    print(f'Saldo SP-Money Anda = {formatrupiah(saldom)}')
    print()
    print(f'Saldo SP-Coin Anda = {saldoc}', 'Coin')
    return menut()


def buymenu():
    print("=" * 42)
    print("="*5, "Shopedia".center(30), "="*5)
    print("=" * 42)
    print("|", "1. Beli SP-Coin".center(38), "|")
    print("|", "2. Beli SP-Coin".center(38), "|")
    print("3. Exit")
    print("=" * 42)


def showitem():
    table = PrettyTable()
    table.field_names = ["No", "Nama Barang", "Harga Barang", "Jumlah"]
    for i in range(len(shop_item.get("nama"))):
        table.add_row([
            i + 1,
            shop_item.get("nama")[i],
            shop_item.get("harga")[i],
            shop_item.get("stok")[i]
        ])
# -------------------------------------------------------------------------------------------------------


def menu():
    while True:
        print("=" * 42)
        print("="*5, "Shopedia".center(30), "="*5)
        print("=" * 42)
        print(">>", "1. Login".center(30), "<<")
        print("2 Register")
        print("3. Exit")
        print("=" * 42)
        print()
        msk = input("Silahkan Masukkan Pilihan Anda : ")

        if msk == '1':
            login()
        elif msk == '3':
            print("=" * 42)
            cprint("Terima Kasih Telah Menggunakan Aplikasi Kami ", 'cyan')
            exit()
        else:
            cprint("Menu tidak ada, Silahkan Masukkan Ulang!!", 'red')


def menut():
    print("=" * 42)
    print("="*5, "Shopedia".center(30), "="*5)
    print("""
===============================================================
|                    1. Check SP-Money                        |
|                    2. Buy SP-Coin                           |
|                    3. Top-up SP-Money                       |
|                    4. Buy VIP Member                        |
|                    5. Shopping Menu                         |
|                    6. Top-up E-Money                        |
|                    7. Kembali Menu Awal                     |
===============================================================
        """)
    print()
    msk = input("Silahkan Masukkan Pilihan Anda : ")

    return msk


def main(data):
    a = False
    while a == False:
        msk = menut()
        if msk == '1':
            showmoney(data)
        elif msk == '2':
            topupm()
        elif msk == '3':
            print("=" * 42)
            cprint("Terima Kasih Telah Menggunakan Aplikasi Kami ", 'cyan')
            exit()
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
            search = useracc.get("username").index(username)
            if username == useracc.get("username")[search] and password == useracc.get("password")[search] and useracc.get("age")[search] <= 12:
                print('='*42)
                print("="*5, "Selamat Datang Adek".center(30), "="*5)
                print('='*42)
                print('='*42)
                print()
                input("Press Enter to Continue...")
                main(search)
                break
            elif username == useracc.get("username")[search] and password == useracc.get("password")[search] and useracc.get("age")[search] >= 12 or useracc.get("age")[search] >= 25:
                print('='*42)
                print("="*5, "Selamat Datang Kakak".center(30), "="*5)
                print('='*42)
                print('='*42)
                print()
                input("Press Enter to Continue...")
                main(search)
            elif username == useracc.get("username")[search] and password == useracc.get("password")[search] and useracc.get("age")[search] >= 25 or useracc.get("age")[search] >= 40:
                print('='*42)
                print("="*5, "Selamat Datang Bapak/Ibu".center(30), "="*5)
                print('='*42)
                print('='*42)
                print()
                input("Press Enter to Continue...")
                main(search)
            else:
                cprint("Username atau Password Anda Salah!", 'red')
                print("Silahkan Coba Lagi")
        except ValueError:
            cprint("Maaf username tidak tersedia", 'red')


menu()
