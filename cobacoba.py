print("""
============== PROGRAM SEARCH & SORTING DESCENDING ==============
=================================================================
              Ariantika Putri Maharani (2109116110)
                    Sistem Informasi C'21
                 UTS ALGORTMA & STRUKTUR DATA
=================================================================
""")

#import modul
import os
import time
import pwinput

#dictionary
datauser = {"username" : ["ariantika", "arin", "putut"],
            "pass"     : ["123", "123", "123"]
}

#array
dataAngka = [32, 18, 22, 39, 80, 21, 46, 3, 50, 48]

#function untuk menunda waktu eksekusi pada output
def clear():
    os.system('cls')
    time.sleep(1)

#function untuk melihat data
def cdangka():
    datasort = merge_sort(dataAngka)
    print("\nData Angka:", datasort)
    print("Panjang Data Angka Sekarang:", len(dataAngka))

#function untuk menambahkan data
def tdangka():
    dataAngka.append(int(input("\nMasukkan Angka yang ingin ditambahkan: ")))
    clear()
    print("Data Angka berhasil ditambahkan.")
    time.sleep(2)
    clear()
    cdangka()

#function untuk menghapus data
def hdangka():
    dataAngka.pop(int(input("\nMasukkan index Angka ke berapa yang ingin dihapus: ")))
    clear()
    print("Data Angka berhasil dihapus.")
    time.sleep(1)
    clear()
    cdangka()

#function searching menggunakan fibonacci search
def cari(x):
    datasort = merge_sort(dataAngka)
    for i in range(len(datasort)):
        if datasort[i] == x:
            return i
        
    return -1    
    

#function untuk searching data (2)
def sdangka():
    datasort = merge_sort(dataAngka)
    x = int(input("\nMasukkan Angka yang ingin dicari: "))
    indeks = cari(x)
    if indeks >= 0:
        clear()
        print("Sedang mencari...")
        time.sleep(3)
        clear()
        print("Angka", x, "berhasil ditemukan!")
        time.sleep(2)
        clear()
        print("\nData Angka:", datasort)
        print("Panjang Data Angka Sekarang:", len(datasort))
        print("Angka", x, "berada di index ke:", indeks)
    else:
        clear()
        print("Sedang mencari...")
        time.sleep(3)
        clear()
        print("Maaf Angka", x, "tidak ada")
        time.sleep(2)
        clear()
        menu()

#function untuk mengurutkan data dari yang terbesar-terkecil
def merge_sort(dataAngka):
    if len(dataAngka) <= 1:
        return dataAngka
    tengah = len(dataAngka) // 2
    kiri = merge_sort(dataAngka[:tengah])
    kanan = merge_sort(dataAngka[tengah:])
    return merge(kiri, kanan)

#function untuk menggabungkan 2 array sebelumnya
def merge(kiri, kanan):
    hasil = []
    i, j = 0, 0

    while i < len(kiri) and j < len(kanan):
        if kiri[i] > kanan[j]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1

    hasil += kiri[i:]
    hasil += kanan[j:]
    return hasil

#function login
def login():
    print("""
    ==== MENU LOGIN ====
    |     1. Login     |
    |     2. Exit      |
    ====================
    """)

    pilihan = (input("Masukkan pilihan kamu: "))
    if pilihan == "1":
        print("\nHalo! Silahkan input data kamu, jangan sampai salah ya!\n")
        while True:
            try:
                us = input("Masukkan Username kamu: ")
                pw = pwinput.pwinput("Masukkan Password kamu: ")
                indeks = datauser.get("username").index(us)
                if us == datauser.get("username")[indeks] and pw == datauser.get("pass")[indeks]:
                    clear()
                    print("Login berhasil!")
                    time.sleep(1)
                    clear()
                    print("Selamat Datang,",datauser["username"][indeks])
                    menu()

                else:
                    clear()
                    print("Maaf data Anda tidak terdaftar, silahkan login ulang!")
                    time.sleep(1)
                    clear()
                    login()

            except ValueError:
                clear()
                print("Maaf input Anda tidak sesuai!")
                time.sleep(2)
                clear()
                login()

    elif pilihan == "2":
        print("\nArigatou! Semoga harimu menyenangkan! ^o^\n")
        raise SystemExit
    
    else:
        clear()
        print("Maaf pilihan tidak ada!")
        time.sleep(1)
        clear()
        login()

#function menu
def menu():
    
    print("""
    \nSELAMAT DATANG DI PROGRAM DESCENDING NUMBER\n
        ===== MENU UTAMA ====
        |1. Cek Data        |
        |2. Tambah Data     |
        |3. Hapus Data      |
        |4. Search Data     |
        |5. Descending Data |
        |6. Logout          |
        =====================
    """)

    while True:
        try:
            pilih = input("Masukkan pilihan kamu: ")

        except ValueError:
            print("Maaf pilihan tidak ada!")

        if pilih == "1":
            print(f"""{" Cek Data "}""".center(50,"="))
            cdangka()
            menu()

        elif pilih == "2":
            print(f"""{" Tambah Data "}""".center(50,"="))
            tdangka()
            menu()

        elif pilih == "3":
            print(f"""{" Menghapus Data "}""".center(50,"="))
            hdangka()
            menu()

        elif pilih == "4":
            print(f"""{" Search Data "}""".center(50,"="))
            sdangka()
            menu()

        elif pilih == "5":
            print(f"""{" Descending Data "}""".center(50,"="))
            print("\nData normal:", dataAngka)
            print("Data setelah di Descending:", merge_sort(dataAngka))
            menu()

        elif pilih == "6":
            clear()
            print("Anda kembali ke menu login...")
            time.sleep(2)
            clear()
            login()

        else:
            clear()
            print("Maaf pilihan tidak ada, silahkan coba lagi!")
            time.sleep(2)
            clear()
            menu()

login()