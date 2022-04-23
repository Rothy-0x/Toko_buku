from typing import ValuesView
from prettytable import PrettyTable
from os import system
import sys
import csv


def cls():
    if sys() == "Windows":
        system("cls")
    else:
        system("clear")


users = {
    'username': ['admin', 'admin2'],
    'password': ['admin', 'admin2'],
    'id': ['1', '2']
}

db = {
    "pesanan": []
}
user = PrettyTable()
user.field_names = ["id", "Nama", "No Telp",
                    "Alamat", "Jenis Laundry", "Jumlah Laundry ", "Harga"]


def add():
    print("=" * 52)
    nama = input("Masukkan Nama Pelanggan : ")
    notelp = input("Masukkan No Telp Pelanggan : ")
    alamat = input("Masukkan Alamat Pelanggan : ")
    jenis = input("Masukkan Jenis Laundry : ")
    jumlah = int(input("Masukkan Jumlah Laundry(Kg) : "))
    harga = int(input("Masukkan harga : "))

    db.get('pesanan').append({
        'nama': nama,
        'notelp': notelp,
        'alamat': alamat,
        'jenis': jenis,
        'jumlah': jumlah,
        "harga": harga
    })

    print('Pesanan berhasil ditambah!!')


def show():
    tabel = PrettyTable()
    tabel.field_names = ['No', 'Nama', 'No Telp',
                         'Alamat', 'Jenis', 'Jumlah', 'Harga', 'Subtotal']
    tabel.clear_rows()

    pesanan = db.get('pesanan')
    for i in range(len(pesanan)):
        p = pesanan[i]
        tabel.add_row([
            i + 1,
            p.get('nama'),
            p.get('notelp'),
            p.get('alamat'),
            p.get('jenis'),
            p.get('jumlah'),
            p.get('harga'),
            p.get('jumlah') * p.get('harga')
        ])

    print(tabel)


def delete():
    show()
    i = int(input('Pilih pesanan yang ingin dihapus : '))
    del db['pesanan'][i - 1]
    print()
    print('Pesanan berhasil dihapus')
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
        jenis = input(
            f"Masukkan Jenis Laundry ({pesanan['jenis']}) : ") or pesanan['jenis']
        jumlah = input(
            f"Masukkan Jumlah Laundry ({pesanan['jumlah']}) : ") or pesanan['jumlah']
        harga = input(
            f"Masukkan harga : ({pesanan['harga']}) ") or pesanan['harga']

        pesanan['nama'] = nama
        pesanan['notelp'] = notelp
        pesanan['alamat'] = alamat
        pesanan['jenis'] = jenis
        pesanan['jumlah'] = int(jumlah)
        pesanan["harga"] = int(harga)

        print('Pesanan berhasil diedit')
        show()
    else:
        print('Mohon masukan pesanan yang tersedia')
        return update()


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
            print("Data Telah Berhasil Di Import!!!")


def menua():
    ulang = "ya"
    while (ulang == "ya"):
        print("=" * 42)
        print("1. Tambah Pelanggan")
        print("2. Hapus Pelanggan")
        print("3. Tampilkan Pelanggan")
        print("4. Ubah pelanggan")
        print("5. Import data to csv")
        print("6. Logout")
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
        elif msk == '5':
            laporan()
        elif msk == '6':
            print("=" * 42)
            print("Terima Kasih Telah Menggunakan Aplikasi Kami ")
            return


def login():
    ulang = "ya"
    while (ulang == "ya"):
        print('=' * 42)
        username = input("Masukkan Username Anda : ")
        password = input("Masukkan Password Anda : ")
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


def register():
    ulang = "ya"
    while (ulang == "ya"):
        print('=' * 42)
        add_username = input("Masukkan Username Yang Anda Inginkan : ")
        if add_username in users.get("username"):
            print('=' * 42)
            print("Maaf Username Anda telah tersedia!!\nSilahkan Masukkan Ulang")
            register()
        else:
            add_password = input("Masukkan Password Anda : ")
            users.get("username").append(add_username)
            users.get("password").append(add_password)
            id = len(users.get('id'))
            users.get('id').append(id+1)
            print('=' * 42)
            print("Anda Telah Berhasil Register!!")
            return


system("cls")
ulang = "ya"
while (ulang == "ya"):
    print('='*42)
    print("="*5, "Aplikasi Laundry".center(30), "="*5)
    print("=" * 42)
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    print("=" * 42)
    print()
    msk = input("Silahkan Masukkan Pilihan Anda : ")

    if msk == "1":
        login()
    elif msk == "2":
        register()
    elif msk == "3":
        print("=" * 42)
        print("Terima Kasih Telah Menggunakan Aplikasi Kami ")
        exit()
