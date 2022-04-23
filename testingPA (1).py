from prettytable import PrettyTable
import csv

# user
passReg = "9080"

userBiasa = {"user" : ["wahyu", "riyandi", "rissa"],
            "pCodeUser" : ["farmer1", "farmer2", "farmer2"]}

superUser = {"userAdmin" : ["admin1", "admin2"],
            "pCodeAdmin" : ["superuser1", "superuser2"]}

dataTernak = [["Sapi", "Kambing", "Ayam"],
            ["12 Ekor", "10 Ekor", "90 Ekor"],
            ["1A", "2A", "3A"]]

tableT = PrettyTable(["Nomor", "Jenis Hewan", "Jumlah Hewan", "Nomor Kandang"])
def tabelTernak():
    i = 0 
    tableT.clear_rows()
    for a in range(0,len(dataTernak[0])):
        tableT.add_row([i+1, dataTernak[0][i], dataTernak[1][i], dataTernak[2][i]])
        i+=1
        
    print(tableT)


def registerAkun():
    ul = "ya"
    while (ul == "ya"):
        print('=' * 52)
        adminBaru = input("Masukkan Username Yang Anda Inginkan : ")
        if adminBaru in superUser.get("userAdmin"):
            print("Maaf Username Yang Anda Pilih Sudah Ada\nSilahkan Masukkan User Yang Lain")
            registerAkun()
        else:
            pcAdBaru = input("Masukkan Passcode Anda : ")
            superUser.get("userAdmin").append(adminBaru)
            superUser.get("pCodeAdmin").append(pcAdBaru)
            print("Anda Telah Berhasil Register!!")
            print("Silahkan Coba Akun Baru")
            login()
        break

def menu():
    print("="*52)
    print("="*5, "MENU MANIPULASI DATA PETERNAKAN ".center(40), "="*5)
    print("="*52)
    print("(1.) Tampilkan Data Ternak")
    print("(2.) Tambah Data Ternak")
    print("(3.) Ubah Data Ternak")
    print("(4.) Hapus Data Ternak")
    print("(5.) Laporan Data Ternak CSV")
    print("(6.) Keluar")
    print()
    print("="*52)
    print("="*5, "TENTUKAN PILIHAN".center(40), "="*5)
    print("="*52)
    pils = input("> Masukkan Pilihan : ")
    if pils == "1":
        tabelTernak()
        menu()
    
    elif pils == "2":
        hb = input("> Masukkan Hewan Baru : ")
        dataTernak[0].append(hb)
        jb = input("> Masukkan Jumlah Baru : ")
        dataTernak[1].append(jb)
        nkb = input("> Masukkan Nomor Kandang Baru : ")
        dataTernak[2].append(nkb)
        tabelTernak()
        menu()
    
    elif pils == "6":
        exit()


def login():
    print("="*52)
    print("="*5, "APLIKASI MANIPULASI DATA PETERNAKAN ".center(40), "="*5)
    print("="*52)
    print("(1.) Login (Admin / User)")
    print("(2.) Register Admin Baru")
    print("(3.) Keluar")
    print()
    print("="*52)
    print("="*5, "TENTUKAN PILIHAN".center(40), "="*5)
    print("="*52)
    opt = input("Masukkan Pilihan : ")
    if opt == "1":
        print("> Login sebagai User/Admin? ")
        pil = int(input("Jika Admin Ketik 1, Jika User Ketik 2 : "))#.upper().lower()
        if pil == 1:
            adPut = input("Masukkan Username Admin : ")
            paspud = input("Masukkan Passcode : ")
            search2 = superUser.get("userAdmin").index(adPut)
            if adPut == superUser.get("userAdmin")[search2] and paspud == superUser.get("pCodeAdmin")[search2]:
                menu()
            else:
                login()

        elif pil == 2:
            usPut = input("Masukkan Username : ")
            pasPut = input("Masukkan Passcode : ")
            search = userBiasa.get("user").index(usPut)
            if usPut == userBiasa.get("user")[search] and pasPut == userBiasa.get("pCodeUser")[search]:
                    print("Login Berhasil")
                    print("Anda Login Sebagai User, Anda Hanya Dapat Melihat Isi Data!")
                    tabelTernak()
            else:
                    print("Username atau Passcode Anda Salah!, Coba Lagi!")

    elif opt == "2":
            pinr = input("Masukkan Pin Untuk Registrasi Akun Baru : ")
            if pinr == passReg:
                registerAkun()

    elif opt == "3":
            exit()
login()