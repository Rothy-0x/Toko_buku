""""
  ARIANTIKA PUTRI MAHARANI
        2109116110
  SISTEM INFORMASI C 2021
UAS DASAR-DASAR PEMROGRAMAN
"""

# import library
import os
import time
import pwinput
from prettytable import PrettyTable

tabel_snack = PrettyTable()

# dictionary
dataUser = {"username"  : ["tika", "ariantika", "putri", "rian"],
            "password"  : ["123", "123", "123", "123", "123"],
            "umur"      : [16, 17, 18, 18],
            "e-money"   : 4000000,
            "gold"      : 0,
            "status"    : "Bronze"
}

dataSnack = {"no"      : [1, 2, 3],
             "paket 1" : ["Tteokbokki + Mozarella (1pcs)", "Seblak Seuhah (1pcs)", "Baso Aci Level 5 (1pcs)"],
             "paket 2" : ["Cimol Pidis Jiwi (1pcs)", "Cireng Isi Ayam (1pcs)", "Cilok (1pcs)"],
             "paket 3" : ["Makaroni Original (1pcs)", "Makaroni Jagung Bakar (1pcs)", "Makaroni Pedas (1pcs)"]
}

dataHarga = {"paket1" : 600,
             "paket2" : 550,
             "paket3" : 500
}

# function
def clear():
    os.system('cls')
    time.sleep(1)

# untuk cek e-money, gold, dan status member
def cmgs():
    print("\nE-Money Anda Rp", dataUser["e-money"])
    print("Gold Anda G", dataUser["gold"])
    print("Status Member Anda", dataUser["status"])

# untuk cek stok snack
def csnack():
    tabel_snack.title = "Stok Snack Enthusiast Store"
    tabel_snack.field_names = ["No", "Paket 1", "Paket 2", "Paket 3"]
    tabel_snack.clear_rows()
    for i in range (len(dataSnack.get("paket 1"))):
        tabel_snack.add_row([i + 1, dataSnack.get("paket 1")[i], dataSnack.get("paket 2")[i], dataSnack.get("paket 3")[i]])

# untuk beli 75 gold
def bgold75():
    beli1 = dataUser["e-money"] - 15000
    dataUser["e-money"] = beli1
    gold75 = dataUser["gold"] + 75
    dataUser["gold"] = gold75
    clear()
    print("Pembelian Berhasil!")
    time.sleep(1)
    clear()
    print("Gold Anda G", dataUser["gold"])
    print("Sisa E-Money Anda Rp.", dataUser["e-money"])

# untuk beli 150 gold
def bgold150():
    beli2 = dataUser["e-money"] - 30000
    dataUser["e-money"] = beli2
    gold150 = dataUser["gold"] + 150
    dataUser["gold"] = gold150
    clear()
    print("Pembelian Berhasil!")
    time.sleep(1)
    clear()
    print("Gold Anda G", dataUser["gold"])
    print("Sisa E-Money Anda Rp.", dataUser["e-money"])

# untuk beli 350 gold
def bgold350():
    beli3 = dataUser["e-money"] - 75000
    dataUser["e-money"] = beli3
    gold350 = dataUser["gold"] + 350
    dataUser["gold"] = gold350
    clear()
    print("Pembelian Berhasil!")
    time.sleep(1)
    clear()
    print("Gold Anda G", dataUser["gold"])
    print("Sisa E-Money Anda Rp.", dataUser["e-money"])

# untuk beli 815 gold
def bgold815():
    beli4 = dataUser["e-money"] - 250000
    dataUser["e-money"] = beli4
    gold815 = dataUser["gold"] + 815
    dataUser["gold"] = gold815
    clear()
    print("Pembelian Berhasil!")
    time.sleep(1)
    clear()
    print("Gold Anda G", dataUser["gold"])
    print("Sisa E-Money Anda Rp.", dataUser["e-money"])

# untuk beli snack
def bpaket1():
    paket1 = dataUser["gold"] - dataHarga["paket1"]
    dataUser["gold"] = paket1
    clear()
    print("Pembelian Berhasil!")
    time.sleep(1)
    clear()
    print("Anda telah membeli Paket 1 :", dataSnack["paket 1"])
    print("Sisa Gold Anda G", dataUser["gold"])

def bpaket2():
    paket2 = dataUser["gold"] - dataHarga["paket2"]
    dataUser["gold"] = paket2
    clear()
    print("Pembelian Berhasil!")
    time.sleep(1)
    clear()
    print("Anda telah membeli Paket 2 :", dataSnack["paket 2"])
    print("Sisa Gold Anda G", dataUser["gold"])

def bpaket3(paket3):
    paket3 = dataUser["gold"] - dataHarga["paket3"]
    dataUser["gold"] = paket3
    clear()
    print("Pembelian Berhasil!")
    time.sleep(1)
    clear()
    print("Anda telah membeli Paket 3 :", dataSnack["paket 3"])
    print("Sisa Gold Anda G", dataUser["gold"])

# untuk beli member vip (platinum member)
def bvip():
    belivip = dataUser["gold"] - 450
    dataUser["gold"] = belivip
    dataUser["status"] = "Platinum"
    clear()
    print("Pembelian Berhasil!")
    time.sleep(2)
    clear()
    print("Selamat Anda telah menjadi Platinum Member!")
    print("Status Member Anda saat ini adalah", dataUser["status"])
    print("Status Member Anda berlaku selama 1 Bulan")
    print("Sisa Gold Anda G", dataUser["gold"])

# diskon harga untuk platinum member
def diskon1():
    diskonsnack1 = dataHarga["paket1"] * (30/100)
    dataUser["gold"] = diskonsnack1
    print("Anda Berhasil Membeli Paket 1!")
    print("Sisa Gold Anda G", dataUser["gold"])

def diskon2():
    diskonsnack2 = dataHarga["paket2"] * (30/100)
    dataUser["gold"] = diskonsnack2
    print("Anda Berhasil Membeli Paket 2!")
    print("Sisa Gold Anda G", dataUser["gold"])

def diskon3():
    diskonsnack3 = dataHarga["paket3"] * (30/100)
    dataUser["gold"] = diskonsnack3
    print("Anda Berhasil Membeli Paket 3!")
    print("Sisa Gold Anda G", dataUser["gold"])

# untuk isi e-money
def tpmoney(emoney):
    isi = int(emoney) + dataUser["e-money"]
    dataUser["e-money"] = isi
    clear()
    print("Anda Berhasil Top-Up!")
    time.sleep(1)
    clear()
    print("E-Money Anda Rp.", dataUser["e-money"])

# Menu Awal
def menuawal():
    print("""
======================== SNACK ENTHUSIAST STORE ========================
|                            1. Login                                  |
|                            2. Exit                                   |
========================================================================
        """)
    pilihan = input("Masukkan Pilihan Anda : ")
    if pilihan == "1":
        print("Silahkan Masukkan Data Anda")
        while True:
            try:
                us = input("Masukkan Username : ")
                pw = pwinput.pwinput("Masukkan Password : ")
                indeks = dataUser.get("username").index(us)
                if us == dataUser.get("username")[indeks] and pw == dataUser.get("password")[indeks] and dataUser.get("umur")[indeks] <= 16:
                    clear()
                    print("Login Sukses")
                    time.sleep(1)
                    clear()
                    print("Selamat Datang", dataUser["username"][indeks])
                    print("Be carefull! Anda masih dibawah umur, gunakan aplikasi dibawah pengawasan orang tua :)")
                    menu_utama()
                    break
                elif us == dataUser.get("username")[indeks] and pw == dataUser.get("password")[indeks] and dataUser.get("umur")[indeks] == 17:
                    clear()
                    print("Login Sukses")
                    time.sleep(1)
                    clear()
                    print("Selamat Datang Kakak", dataUser["username"][indeks])
                    menu_utama()
                    break
                elif us == dataUser.get("username")[indeks] and pw == dataUser.get("password")[indeks] and dataUser.get("umur")[indeks] > 17:
                    clear()
                    print("Login Sukses")
                    time.sleep(1)
                    clear()
                    if dataUser.get("username")[indeks] == "putri":
                        print("Selamat Datang Ibu", dataUser["username"][indeks])
                        menu_utama()
                        break
                    elif dataUser.get("username")[indeks] == "rian":
                        print("Selamat Datang Bapak", dataUser["username"][indeks])
                        menu_utama()
                        break
                else:
                        clear()
                        print("Maaf Username/Password Anda Salah!")
                        time.sleep(2)
                        clear()
                        menuawal()
            except ValueError:
                clear()
                print("Username/Password tidak sesuai!")
                time.sleep(2)

    elif pilihan == "2":
        print("\nThank You, Have a Nice Day!\n")
        raise SystemExit
    else:
        clear()
        print("Maaf Input Anda Salah!")
        time.sleep(1)
        clear()
        return menuawal()

def menu_utama():
    print("""
======================== SNACK ENTHUSIAST STORE ========================
|                           1. Cek E-Money                             |
|                           2. Cek Stok Snack                          |
|                           3. Beli Gold                               |
|                           4. Beli Member VIP                         |
|                           5. Beli Snack                              |
|                           6. Top-up E-Money                          |
|                           7. Kembali Menu Awal                       |
========================================================================
        """)
    ulang = "yes"
    while ulang == "yes":
        try:
            pilih = int(input("Masukkan Pilihan : "))
        except ValueError:
            clear()
            print("Maaf pilihan harus berupa angka!")
            time.sleep(2)
            clear()
            menu_utama()

        if pilih == 1:
            print(f"""{" Cek E-Money "}""".center(50,"="))
            cmgs()
            while True:
                ulang = input("\nKembali ke Menu Utama? (ok/no) --> ")
                if ulang == "no":
                    print("\nThank You, Have a Nice Day!\n")
                    raise SystemExit
                elif ulang != "ok":
                    clear()
                    print("Maaf inputan Anda tidak sesuai!")
                    time.sleep(2)
                    clear()
                    continue
                elif ulang == "ok":
                    menu_utama()

        elif pilih == 2:
            print(f"""{" Cek Stok Snack "}""".center(50,"="))
            csnack()
            print(tabel_snack)
            while True:
                ulang = input("\nKembali ke Menu Utama? (ok/no) --> ")
                if ulang == "no":
                    print("\nThank You, Have a Nice Day!\n")
                    raise SystemExit
                elif ulang != "ok":
                    clear()
                    print("Maaf inputan Anda tidak sesuai!")
                    time.sleep(2)
                    clear()
                    continue
                elif ulang == "ok":
                    menu_utama()

        elif pilih == 3:
            print("""
======================== Beli Gold ========================
|                1. Beli 75G  -> Rp.15000                 |
|                2. Beli 150G -> Rp.30000                 |
|                3. Beli 350G -> Rp.75000                 |
|                4. Beli 815G -> Rp.250000                |
===========================================================
        """)
            while True:
                try:
                    bg = int(input("Masukkan Pilihan : "))
                    if bg == 1:
                        ybg = input("Apakah Anda yakin ingin membeli? (ya/tidak) --> ")
                        if ybg == "ya" and dataUser["e-money"] <= 15000:
                            clear()
                            print("Maaf E-Money Anda tidak cukup, silahkan melakukan pengisian ulang.")
                            time.sleep(4)
                            clear()
                            menu_utama()
                        elif ybg == "ya":
                            bgold75()
                            while True:
                                ulang = input("\nKembali ke Menu Utama? (ok/no) --> ")
                                if ulang == "no":
                                    print("\nThank You, Have a Nice Day!\n")
                                    raise SystemExit
                                elif ulang != "ok":
                                    clear()
                                    print("Maaf inputan Anda tidak sesuai!")
                                    time.sleep(2)
                                    clear()
                                    continue
                                elif ulang == "ok":
                                    menu_utama()
                        elif ybg == "tidak":
                            clear()
                            print("Terima Kasih, Silahkan Pilih Menu")
                            time.sleep(2)
                            clear()
                            menu_utama()

                    elif bg == 2:
                        ybg = input("Apakah Anda yakin ingin membeli? (ya/tidak) --> ")
                        if ybg == "ya" and dataUser["e-money"] <= 30000:
                            clear()
                            print("Maaf E-Money Anda tidak cukup, silahkan melakukan pengisian ulang.")
                            time.sleep(4)
                            clear()
                            menu_utama()
                        elif ybg == "ya":
                            bgold150()
                            while True:
                                ulang = input("\nKembali ke Menu Utama? (ok/no) --> ")
                                if ulang == "no":
                                    print("\nThank You, Have a Nice Day!\n")
                                    raise SystemExit
                                elif ulang != "ok":
                                    clear()
                                    print("Maaf inputan Anda tidak sesuai!")
                                    time.sleep(2)
                                    clear()
                                    continue
                                elif ulang == "ok":
                                    menu_utama()
                        elif ybg == "tidak":
                            clear()
                            print("Terima Kasih, Silahkan Pilih Menu")
                            time.sleep(2)
                            clear()
                            menu_utama()

                    elif bg == 3:
                        ybg = input("Apakah Anda yakin ingin membeli? (ya/tidak) --> ")
                        if ybg == "ya" and dataUser["e-money"] <= 75000:
                            clear()
                            print("Maaf E-Money Anda tidak cukup, silahkan melakukan pengisian ulang.")
                            time.sleep(4)
                            clear()
                            menu_utama()
                        elif ybg == "ya":
                            bgold350()
                            while True:
                                ulang = input("\nKembali ke Menu Utama? (ok/no) --> ")
                                if ulang == "no":
                                    print("\nThank You, Have a Nice Day!\n")
                                    raise SystemExit
                                elif ulang != "ok":
                                    clear()
                                    print("Maaf inputan Anda tidak sesuai!")
                                    time.sleep(2)
                                    clear()
                                    continue
                                elif ulang == "ok":
                                    menu_utama()
                        elif ybg == "tidak":
                            clear()
                            print("Terima Kasih, Silahkan Pilih Menu")
                            time.sleep(2)
                            clear()
                            menu_utama()
                          
                    elif bg == 4:
                        ybg = input("Apakah Anda yakin ingin membeli? (ya/tidak) --> ")
                        if ybg == "ya" and dataUser["e-money"] <= 250000:
                            clear()
                            print("Maaf E-Money Anda tidak cukup, silahkan melakukan pengisian ulang.")
                            time.sleep(4)
                            clear()
                            menu_utama()
                        elif ybg == "ya":
                            bgold815()
                            while True:
                                ulang = input("\nKembali ke Menu Utama? (ok/no) --> ")
                                if ulang == "no":
                                    print("\nThank You, Have a Nice Day!\n")
                                    raise SystemExit
                                elif ulang != "ok":
                                    clear()
                                    print("Maaf inputan Anda tidak sesuai!")
                                    time.sleep(2)
                                    clear()
                                    continue
                                elif ulang == "ok":
                                    menu_utama()
                        elif ybg == "tidak":
                            clear()
                            print("Terima Kasih, Silahkan Pilih Menu")
                            time.sleep(2)
                            clear()
                            menu_utama()
                    else:
                        clear()
                        print("Inputan salah, Silahkan Pilih Menu")
                        time.sleep(2)
                        clear()
                        menu_utama()

                except ValueError:
                    clear()
                    print("Maaf inputan Anda tidak sesuai!")
                    menu_utama()
                    time.sleep(2)
                    clear()
                    continue

        elif pilih == 4:
            print(f"""{" Beli Member VIP "}""".center(50,"="))
            while True:
                try:
                    vvip = input("Apakah Anda yakin ingin membeli Member VIP 450G? (ya/tidak) --> ")
                    if vvip == "ya" and dataUser["gold"] <= 450:
                        clear()
                        print("Maaf Gold Anda tidak cukup!")
                        time.sleep(2)
                        clear()
                        menu_utama()
                    elif vvip == "ya":
                        bvip()
                        while True:
                            ulang = input("\nKembali ke Menu Utama? (ok/no) --> ")
                            if ulang == "no":
                                print("\nThank You, Have a Nice Day!\n")
                                raise SystemExit
                            elif ulang != "ok":
                                clear()
                                print("Maaf inputan Anda tidak sesuai!")
                                clear()
                                continue
                            elif ulang == "ok":
                                menu_utama()
                    elif vvip == "tidak":
                        clear()
                        print("Terima Kasih, Silahkan Pilih Menu")
                        time.sleep(2)
                        clear()
                        menu_utama()            

                except ValueError:
                    clear()
                    print("Maaf inputan Anda tidak sesuai!")
                    menu_utama()
                    time.sleep(2)
                    clear()
                    continue
        
        elif pilih == 5:
            print("""
======================= Beli Snack =======================
|                   1. Bronze Member                     |
|                   2. Platinum Member                   |
==========================================================
        """)
            while True:
                try:
                    bs = int(input("Masukkan pilihan : "))
                    if bs == 1:
                        print("""
======================= Beli Snack =======================
|               1. Beli Paket 1 -> 600G                  |
|               2. Beli Paket 2 -> 550G                  |
|               3. Beli Paket 3 -> 500G                  |
==========================================================
                    """)
                        while True:
                            try:
                                bp = int(input("Masukkan pilihan paket yang ingin Anda beli : "))
                                if bp == 1:
                                    print("\nPaket 1 : Tteokbokki + Mozarella (1pcs), Seblak Seuhah (1pcs), Baso Aci Level 5 (1pcs)")
                                    bp1 = input("Apakah Anda yakin ingin membeli Paket 1? (ya/tidak) --> ")
                                    if bp1 == "ya" and dataUser.get("gold") <= 600:
                                        clear()
                                        print("Maaf Gold Anda tidak cukup!")
                                        time.sleep(2)
                                        clear()
                                        menu_utama()
                                    elif bp1 == "ya":
                                        bpaket1()
                                        while True:
                                            ulang = input("\nKembali ke Menu Utama? (ok/no) --> ")
                                            if ulang == "no":
                                                print("\nThank You, Have a Nice Day!\n")
                                                raise SystemExit
                                            elif ulang != "ok":
                                                clear()
                                                print("Maaf inputan Anda tidak sesuai!")
                                                clear()
                                                continue
                                            elif ulang == "ok":
                                                menu_utama()
                                    elif bp1 == "tidak":
                                        clear()
                                        print("Terima kasih, silahkan pilih menu")
                                        time.sleep(2)
                                        clear()
                                        menu_utama()

                                elif bp == 2:
                                    print("\nPaket 2 : Cimol Pidis Jiwi (1pcs), Cireng Isi Ayam (1pcs), Cilok (1pcs)")
                                    bp2 = input("Apakah Anda yakin ingin membeli Paket 2? (ya/tidak) --> ")
                                    if bp2 == "ya" and dataUser.get("gold") <= 550:
                                        clear()
                                        print("Maaf Gold Anda tidak cukup!")
                                        time.sleep(2)
                                        clear()
                                        menu_utama()
                                    elif bp2 == "ya":
                                        bpaket1()
                                        while True:
                                            ulang = input("\nKembali ke Menu Utama? (ok/no) --> ")
                                            if ulang == "no":
                                                print("\nThank You, Have a Nice Day!\n")
                                                raise SystemExit
                                            elif ulang != "ok":
                                                clear()
                                                print("Maaf inputan Anda tidak sesuai!")
                                                clear()
                                                continue
                                            elif ulang == "ok":
                                                menu_utama()
                                    elif bp2 == "tidak":
                                        clear()
                                        print("Terima kasih, silahkan pilih menu")
                                        time.sleep(2)
                                        clear()
                                        menu_utama()
                                
                                elif bp == 3:
                                    print("\nPaket 2 : Cimol Pidis Jiwi (1pcs), Cireng Isi Ayam (1pcs), Cilok (1pcs)")
                                    bp3 = input("Apakah Anda yakin ingin membeli Paket 2? (ya/tidak) --> ")
                                    if bp3 == "ya" and dataUser.get("gold") <= 500:
                                        clear()
                                        print("Maaf Gold Anda tidak cukup!")
                                        time.sleep(2)
                                        clear()
                                        menu_utama()
                                    elif bp3 == "ya":
                                        bpaket1()
                                        while True:
                                            ulang = input("\nKembali ke Menu Utama? (ok/no) --> ")
                                            if ulang == "no":
                                                print("\nThank You, Have a Nice Day!\n")
                                                raise SystemExit
                                            elif ulang != "ok":
                                                clear()
                                                print("Maaf inputan Anda tidak sesuai!")
                                                clear()
                                                continue
                                            elif ulang == "ok":
                                                menu_utama()
                                    elif bp3 == "tidak":
                                        clear()
                                        print("Terima kasih, silahkan pilih menu")
                                        time.sleep(2)
                                        clear()
                                        menu_utama()
                                        
                            except ValueError:
                                clear()
                                print("Inputan anda tidak sesuai, coba lagi!")
                                time.sleep(1)
                                clear

                    elif bs == 2 and dataUser.get("status") == "Platinum":
                        print("Anda mendapatkan voucher 30% (berlaku selama Platinum Member aktif)\n")
                        print("""
======================= Beli Snack =======================
|               1. Beli Paket 1 -> 420G                  |
|               2. Beli Paket 2 -> 385G                  |
|               3. Beli Paket 3 -> 500G                  |
==========================================================
                    """)
                        while True:
                            try:
                                bs2 = int(input("Masukkan pilihan paket yang ingin Anda beli : "))
                                if bs2 == 1:
                                    print("\nPaket 1 : Tteokbokki + Mozarella (1pcs), Seblak Seuhah (1pcs), Baso Aci Level 5 (1pcs)")
                                    bpa = input("Apakah Anda yakin ingin membeli Paket 1? (ya/tidak) --> ")
                                    if bpa == "ya" and dataUser.get("status") == "Platinum" and dataUser.get("gold") <= 420:
                                        clear()
                                        print("Maaf Gold Anda tidak cukup!")
                                        time.sleep(2)
                                        clear()
                                        menu_utama()
                                    elif bpa == "ya" and dataUser.get("status") == "Platinum":
                                        diskon1()
                                        while True:
                                            ulang = input("\nKembali ke Menu Utama? (ok/no) --> ")
                                            if ulang == "no":
                                                print("\nThank You, Have a Nice Day!\n")
                                                raise SystemExit
                                            elif ulang != "ok":
                                                clear()
                                                print("Maaf inputan Anda tidak sesuai!")
                                                clear()
                                                continue
                                            elif ulang == "ok":
                                                menu_utama()
                                    elif bpa == "tidak":
                                        clear()
                                        print("Terima kasih, silahkan pilih menu")
                                        time.sleep(2)
                                        clear()
                                        menu_utama()

                                elif bs2 == 2:
                                    print("\nPaket 2 : Cimol Pidis Jiwi (1pcs), Cireng Isi Ayam (1pcs), Cilok (1pcs)")
                                    bpa2 = input("Apakah Anda yakin ingin membeli Paket 2? (ya/tidak) --> ")
                                    if bpa2 == "ya" and dataUser.get("status") == "Platinum" and dataUser.get("gold") <= 385:
                                        clear()
                                        print("Maaf Gold Anda tidak cukup!")
                                        time.sleep(2)
                                        clear()
                                        menu_utama()
                                    elif bpa2 == "ya" and dataUser.get("status") == "Platinum":
                                        diskon1()
                                        while True:
                                            ulang = input("\nKembali ke Menu Utama? (ok/no) --> ")
                                            if ulang == "no":
                                                print("\nThank You, Have a Nice Day!\n")
                                                raise SystemExit
                                            elif ulang != "ok":
                                                clear()
                                                print("Maaf inputan Anda tidak sesuai!")
                                                clear()
                                                continue
                                            elif ulang == "ok":
                                                menu_utama()
                                    elif bpa2 == "tidak":
                                        clear()
                                        print("Terima kasih, silahkan pilih menu")
                                        time.sleep(2)
                                        clear()
                                        menu_utama()

                                elif bs2 == 3:
                                    print("\nPaket 3 : Makaroni Original (1pcs), Makaroni Jagung Bakar (1pcs), Makaroni Pedas (1pcs)")
                                    bpa3 = input("Apakah Anda yakin ingin membeli Paket 2? (ya/tidak) --> ")
                                    if bpa3 == "ya" and dataUser.get("status") == "Platinum" and dataUser.get("gold") <= 350:
                                        clear()
                                        print("Maaf Gold Anda tidak cukup!")
                                        time.sleep(2)
                                        clear()
                                        menu_utama()
                                    elif bpa3 == "ya" and dataUser.get("status") == "Platinum":
                                        diskon1()
                                        while True:
                                            ulang = input("\nKembali ke Menu Utama? (ok/no) --> ")
                                            if ulang == "no":
                                                print("\nThank You, Have a Nice Day!\n")
                                                raise SystemExit
                                            elif ulang != "ok":
                                                clear()
                                                print("Maaf inputan Anda tidak sesuai!")
                                                clear()
                                                continue
                                            elif ulang == "ok":
                                                menu_utama()
                                    elif bpa3 == "tidak":
                                        clear()
                                        print("Terima kasih, silahkan pilih menu")
                                        time.sleep(2)
                                        clear()
                                        menu_utama()

                            except ValueError:
                                clear()
                                print("Inputan anda tidak sesuai, coba lagi!")
                                time.sleep(1)
                                clear
                    else:
                        clear()
                        print("Maaf anda belum menjadi Platinum Member")
                        time.sleep(2)
                        clear()
                        menu_utama()

                except ValueError:
                    clear()
                    print("Inputan anda tidak sesuai, coba lagi!")
                    time.sleep(1)
                    clear
            
        elif pilih == 6:
            while True:
                try:
                    print(f"""{" Top-up E-Money "}""".center(50,"="))
                    emoney = int(input("\nMasukkan Nominal Rp."))
                    if emoney < 4000:
                        clear()
                        print("Maaf nominal harus diatas Rp.5000")
                        time.sleep(2)
                        clear()
                    else:
                        tpmoney(emoney)
                        while True:
                            ulang = input("\nKembali ke Menu Utama? (ok/no) --> ")
                            if ulang == "no":
                                print("\nThank You, Have a Nice Day!\n")
                                raise SystemExit
                            elif ulang != "ok":
                                clear()
                                print("Maaf inputan Anda tidak sesuai!")
                                time.sleep(2)
                                clear()
                                continue
                            elif ulang == "ok":
                                menu_utama()
                except ValueError:
                    clear()
                    print("Inputan anda tidak sesuai, coba lagi!")
                    time.sleep(1)
                    clear

        elif pilih == 7:
            menuawal()

menuawal()